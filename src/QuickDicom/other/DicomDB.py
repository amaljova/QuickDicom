'''
@ author: Amal Joseph Varghese
@ email: amaljova@gmail.com
@ github: https://github.com/amaljova
@ date: 15 June 2023
'''


from box import Box
import json

# File
class File:
    def __init__(self, file_info: Box) -> None:
        self.FilePath = file_info.FilePath

# Image Slice
class ImageSlice(File):
    def __init__(self, file_info: Box) -> None:
        super().__init__(file_info)
        self.InstanceNumber = file_info.InstanceNumber

# RTSTRUCT File
class RTStructFile(File):
    def __init__(self, file_info: Box) -> None:
        super().__init__(file_info)
        self.StructureSetLabel = file_info.StructureSetLabel
        self.ReferencedSeriesUID = file_info.ReferencedSeriesUID
        self.ROIs = file_info.ROIs

# Series
class Series:
    def __init__(self, file_info: Box) -> None:
        self.Modality = file_info.Modality
        self.SOPClassUID = file_info.SOPClassUID
        self.SeriesDescription = file_info.SeriesDescription
        self.SeriesNumber = file_info.SeriesNumber
        self.SeriesDate = file_info.SeriesDate
        self.SeriesTime = file_info.SeriesTime
        self.files = dict()

    def createFile(self, file_info: Box) -> None:
        sop_uid = file_info.SOPInstanceUID
        self.files[sop_uid] = File(file_info)
        # if not sop_uid in self.files:
        #     self.files[sop_uid] = File(file_info)
        # else:
        #     print("Duplicate")        

# Series Modality is any Tomographic Imaging
class Image(Series):
    def __init__(self, file_info: Box) -> None:
        super().__init__(file_info)
        self.SliceThickness = file_info.SliceThickness
        self.Exposure = file_info.Exposure
        self.Kvp = file_info.Kvp
        self.mA = file_info.mA
        self.PixelSpacingx = file_info.PixelSpacingx
        self.PixelSpacingy = file_info.PixelSpacingy
        self.ConvolutionKernel = file_info.ConvolutionKernel
        self.FieldofViewShape = file_info.FieldofViewShape
        self.SpiralPitchFactor = file_info.SpiralPitchFactor
        self.FieldofViewDimension = file_info.FieldofViewDimension
        self.allavailable = False

    def createImageSlice(self, file_info: Box) -> None:
        sop_uid = file_info.SOPInstanceUID
        self.files[sop_uid] = ImageSlice(file_info)
        # if not sop_uid in self.files:
        #     self.files[sop_uid] = ImageSlice(file_info)
        # else:
        #     print("Duplicate")

    def checkAllAvailable(self) -> bool:
        InstanceNumbers = [file.InstanceNumber for file in self.files.values()]
        total_files = len(InstanceNumbers)
        return True if max(InstanceNumbers) == total_files else False

    def setAllAvailability(self) -> None:
        try:
            if self.checkAllAvailable():
                self.allavailable = True
        except:
            pass

# Series Modality == RTSTRUCT
class RTStruct(Series):
    def __init__(self, file_info: Box) -> None:
        super().__init__(file_info)
    #     self.files = dict()
    def createRTStructFile(self, file_info: Box) -> None:
        sop_uid = file_info.SOPInstanceUID
        self.files[sop_uid] = RTStructFile(file_info)
        # if not sop_uid in self.files:
        #     self.files[sop_uid] = RTStructFile(file_info)
        # else:
        #     print("Duplicate")

# Series Modality == REG
class Reg(Series):
    def __init__(self, file_info: Box) -> None:
        super().__init__(file_info)

# Study   
class Study:
    def __init__(self, file_info: Box) -> None:
        self.StudyID = file_info.StudyID
        self.StudyDescription = file_info.StudyDescription
        self.StudyDate = file_info.StudyDate
        self.StudyTime = file_info.StudyTime
        self.ReferringPhysicianName = file_info.ReferringPhysicianName
        self.Manufacturer = file_info.Manufacturer
        self.ManufacturersModelName = file_info.ManufacturersModelName
        self.DeviceSerialNumber = file_info.DeviceSerialNumber
        self.ImageType = file_info.ImageType
        self.serieses= dict()
        self.RTStructAvailable = False

    def getOrCreateImage(self, file_info: Box) -> Image:
        series_uid = file_info.SeriesInstanceUID
        if not series_uid in self.serieses:
            self.serieses[series_uid] = Image(file_info)
        return self.serieses[series_uid]
           
    def getOrCreateRTStruct(self, file_info: Box) -> RTStruct:
        series_uid = file_info.SeriesInstanceUID
        if not series_uid in self.serieses:
            self.serieses[series_uid] = RTStruct(file_info)
        return self.serieses[series_uid]
         
    def getOrCreateReg(self, file_info: Box) -> Reg:
        series_uid = file_info.SeriesInstanceUID
        if not series_uid in self.serieses:
            self.serieses[series_uid] = Reg(file_info)
        return self.serieses[series_uid]        

    def setSeries(self, file_info: Box) -> None:
        if file_info.Modality in ["CT", "PT", "MR"]:
            series = self.getOrCreateImage(file_info)
            series.createImageSlice(file_info)

        elif file_info.Modality == "RTSTRUCT":
            series = self.getOrCreateRTStruct(file_info)
            series.createRTStructFile(file_info)

        elif file_info.Modality == "REG":
            series = self.getOrCreateReg(file_info)
            series.createFile(file_info)

    def setRTStructAvailability(self) -> None:
        self.RTStructAvailable = True


# Patient
class Patient:
    def __init__(self, file_info: Box) -> None:
        self.PatName = file_info.PatName
        self.PatientSex = file_info.PatientSex
        self.InstitutionName = file_info.InstitutionName
        self.studies= dict()
        # StudyInstanceUID: Study

    def getOrCreateStudy(self, file_info: Box) -> Study:
        study_uid = file_info.StudyInstanceUID
        if not study_uid in self.studies:
            self.studies[study_uid] = Study(file_info)
        return self.studies[study_uid]

    def setStudy(self,file_info: Box ) -> None:
            study = self.getOrCreateStudy(file_info)
            study.setSeries(file_info)


# The DICOM DataBase
class DataBase:
    def __init__(self) -> None:
        self.patients= dict()
        # PatID: Patient

    def getOrCreatePatient(self, file_info: Box) -> Patient:
        patient_id = file_info.PatID
        if not patient_id in self.patients:
            self.patients[patient_id] = Patient(file_info)
        return self.patients[patient_id]
    
    def setPatient(self,file_info: Box ) -> None:
            patient = self.getOrCreatePatient(file_info)
            patient.setStudy(file_info)

    def parse(self, dict_list: list) -> None:
        for file_info_dict in dict_list:
            file_info = Box(file_info_dict)
            self.setPatient(file_info)

    def parse_json(self, json_file: str) -> None:
        with open(json_file, "r") as f:
            json_data = json.load(f)
            self.parse(json_data)

    def from_json(self, json_file: str) -> None:
        with open(json_file, "r") as f:
            json_data = json.load(f)
        self.__parse_own_json(Box(json_data))

    def to_json(self, out_file: str) -> None:
        with open(out_file, "w") as f:
            json.dump(self,f, default=lambda o: o.__dict__)

    
    def __parse_own_json(self, json_data:Box) -> None:
        json_patients = json_data.patients
        for pat_id, pat_info in json_patients.items():
            self.patients[pat_id] = Patient(pat_info)
            for study_id, study_info in pat_info.studies.items():
                self.patients[pat_id].studies[study_id] = Study(study_info)
                for series_id, series_info in study_info.serieses.items():
                    if series_info.Modality in ["CT", "PT", "MR"]:
                        self.patients[pat_id].studies[study_id] .serieses[series_id] = Image(series_info)
                        for file_id, file_info in series_info.files.items():
                            setattr(file_info,"SOPInstanceUID",file_id )
                            self.patients[pat_id].studies[study_id] .serieses[series_id].createImageSlice(file_info)                            
                    elif series_info.Modality == "RTSTRUCT":
                        self.patients[pat_id].studies[study_id] .serieses[series_id] = RTStruct(series_info)
                        for file_id, file_info in series_info.files.items():
                            setattr(file_info,"SOPInstanceUID",file_id )
                            self.patients[pat_id].studies[study_id] .serieses[series_id].createRTStructFile(file_info)
                    elif series_info.Modality == "REG":
                        self.patients[pat_id].studies[study_id] .serieses[series_id] = Reg(series_info)
                        for file_id, file_info in series_info.files.items():
                            setattr(file_info,"SOPInstanceUID",file_id )
                            self.patients[pat_id].studies[study_id] .serieses[series_id].createFile(file_info)
    
    def checkSanity(self)-> None:
        for patID in self.patients:
            for studyID in  self.patients[patID].studies:
                for seriesID, series_info in self.patients[patID].studies[studyID].serieses.items():
                    #All images Available?
                    if series_info.Modality in ["CT", "PT", "MR"]:
                        self.patients[patID].studies[studyID].serieses[seriesID].setAllAvailability()
                    elif series_info.Modality == "RTSTRUCT":
                        #has RTSTRUCT?
                        self.patients[patID].studies[studyID].setRTStructAvailability()
                    else:
                        pass

