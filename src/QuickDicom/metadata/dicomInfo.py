'''
@ author: Amal Joseph Varghese
@ email: amaljova@gmail.com
@ github: https://github.com/amaljova
@ date: 13 June 2023
'''

import pydicom
from pathlib import Path



class dcmFile:
    def __init__(self, file: Path) -> None:
        self.filePath = Path(file)
        self.header = pydicom.dcmread(self.filePath, stop_before_pixels=True)

    def getFilePath(self) -> str:
        return str(self.filePath)
    
    def getPatId(self) -> str:
        # pat_id
        try:
            pat_id = self.header[(0x10, 0x20)].value
            return str(pat_id)
        except:
            return None
    
    def getPatName(self) -> str:
        # patName
        try:
            patName = self.header[(0x10, 0x10)].value
            return str(patName)
        except:
            return None
    
    def getModality(self) -> str:
        try:
            modality = self.header[(0x08, 0x60)].value
            return str(modality)
        except:
            return None

    def getStudyInstanceUID(self) -> str:
        # Study Instance UID
        try:
            stu_inst_UID = self.header[(0x20, 0x0d)].value
            return str(stu_inst_UID)
        except:
            return None


    def getSeriesInstanceUID(self) -> str:
        # Series Instance UID
        try:
            ser_inst_UID = self.header[(0x20, 0x0e)].value
            return str(ser_inst_UID)
        except:
            return None


    def getStudyDescription(self) -> str:
        # StudyDescription
        try:
            StudyDescription = self.header[(0x08, 0x1030)].value
            return str(StudyDescription)
        except:
            return None


    def getSeriesDescription(self) -> str:
        # SeriesDescription
        try:
            SeriesDescription = self.header[(0x08, 0x103e)].value
            return str(SeriesDescription)
        except:
            return None


    def getSOPClassUID(self) -> str:
        # SOP Class UID
        try:
            SOPClassUID = self.header[(0x08, 0x16)].value
            return str(SOPClassUID)
        except:
            return None


    def getSOPInstanceUID(self) -> str:
        # SOP Instance UID
        try:
            SOPInstanceUID = self.header[(0x08, 0x18)].value
            return str(SOPInstanceUID)
        except:
            return None


    def getStructureSetLabel(self) -> str:
        # Structure Set Label
        try:
            StructureSetLabel = self.header[(0x3006, 0x02)].value
            return str(StructureSetLabel)
        except:
            return None

    def getSliceThickness(self) -> float:
        # Slice Thickness
        try:
            SliceThickness = self.header[(0x18, 0x50)].value
            return float(SliceThickness)
        except:
            return None


    def getReferencedCTUID(self) -> str:
        try:
            if len(list(self.header[0x3006, 0x10])) > 0:
                refFrameOfRef = (self.header[0x3006, 0x10])[0]
                if len(list(refFrameOfRef[0x3006, 0x0012])) > 0:
                    rtRefStudy = (refFrameOfRef[0x3006, 0x0012])[0]
                    if len(list(rtRefStudy[0x3006, 0x14])) > 0:
                        rtRefSerie = (rtRefStudy[0x3006, 0x14])[0]
                        return str(rtRefSerie[0x20, 0xe].value)
        except:
            return None


    def getROIs(self)-> list:
        # ROIs
        try:
            ROIs = [i[(0x3006, 0x26)].value for i in self.header[(0x3006, 0x20)].value]
            return ROIs
        except:
                return None


    def getManufacturer(self) -> str:
        # Manufacturer
        try:
            Manufacturer = self.header[(0x08, 0x70)].value
            return str(Manufacturer)
        except:
            return None


    def getManufacturersModelName(self) -> str:
        # Manufacturer's Model Name
        try:
            ManufacturersModelName = self.header[(0x08, 0x1090)].value
            return str(ManufacturersModelName)
        except:
            return None


    def getKvp(self) -> float:
        # KVP
        try:
            Kvp = self.header[(0x18, 0x60)].value
            return float(Kvp)
        except:
            return None


    def getmA(self) -> float:
        # X-Ray Tube Current
        try:
            XRayTubeCurrent = self.header[(0x18, 0x1151)].value
            return float(XRayTubeCurrent)
        except:
            return None


    def getExposure(self):
        # Exposure
        try:
            Exposure = self.header[(0x18, 0x1152)].value
            return Exposure
        except:
            return None


    def getConvolutionKernel(self) -> str:
        # Convolution Kernel
        try:
            ConvolutionKernel = self.header[(0x18, 0x1210)].value
            return str(ConvolutionKernel)
        except:
            return None

 
    def getPixelSpacing(self) -> float:
        # Pixel Spacing
        try:
            PixelSpacing = self.header[(0x28, 0x30)].value[0]
            return float(PixelSpacing)
        except:
            return None

    def getImageType(self) -> list:
        # Image Type
        try:
            ImageType = self.header[(0x08, 0x08)].value
            return list(ImageType)
        except:
            return None


    def getDeviceSerialNumber(self) -> str:
        # DeviceSerialNumber
        try:
            DeviceSerialNumber = self.header[(0x18, 0x1000)].value
            return str(DeviceSerialNumber)
        except:
            return None

    def getStudyID(self) -> str:
        # StudyID
        try:
            StudyID = self.header[(0x20, 0x10)].value
            return str(StudyID)
        except:
            return None

    def getSeriesNumber(self) -> str:
        # SeriesNumber
        try:
            SeriesNumber = self.header[(0x20, 0x11) ].value
            return str(SeriesNumber)
        except:
            return None

    def getStudyDate(self):
        # StudyDate
        try:
            StudyDate = self.header[(0x08, 0x20)].value
            return StudyDate
        except:
            return None

    def getSeriesDate(self):
        # SeriesDate
        try:
            SeriesDate = self.header[(0x08, 0x21)].value
            return SeriesDate
        except:
            return None

    def getStudyTime(self):
        # StudyTime
        try:
            StudyTime = self.header[(0x08, 0x30)].value
            return StudyTime
        except:
            return None

    def getSeriesTime(self):
        # SeriesTime
        try:
            SeriesTime = self.header[(0x08, 0x31)].value
            return SeriesTime
        except:
            return None

    def getPatientSex(self) -> str:
        # PatientSex
        try:
            PatientSex = self.header[(0x10, 0x40)].value
            return str(PatientSex)
        except:
            return None

    def getInstanceNumber(self) -> int:
        # InstanceNumber
        try:
            InstanceNumber = self.header[(0x20, 0x13)].value
            return int(InstanceNumber)
        except:
            return None
        
    def getBodyPart(self) -> int:
        # BodyPart
        try:
            BodyPart = self.header[(0x18, 0x15)].value
            return BodyPart
        except:
            return None
        
    def getBirthDate(self) -> int:
        # BirthDate
        try:
            BirthDate = self.header[(0x10, 0x30)].value
            return BirthDate
        except:
            return None
        
    def getDataCollectionDiameter(self) -> int:
        # DataCollectionDiameter
        try:
            DataCollectionDiameter = self.header[(0x18, 0x90)].value
            return DataCollectionDiameter
        except:
            return None
        
    def getReconstructionDiameter(self) -> int:
        # ReconstructionDiameter
        try:
            ReconstructionDiameter = self.header[(0x18, 0x1100)].value
            return ReconstructionDiameter
        except:
            return None

    def getAllInfo(self) -> dict:
        info = {
            'PatID' : self.getPatId(),
            'PatName' : self.getPatName(),
            'PatientSex' : self.getPatientSex(),
            'Birthdate': self.getBirthDate(),
            'StudyID' : self.getStudyID(),
            'StudyInstanceUID' : self.getStudyInstanceUID(),
            'StudyDescription' : self.getStudyDescription(),
            'StudyDate' : self.getStudyDate(),
            'StudyTime' : self.getStudyTime(),
            'SeriesInstanceUID' : self.getSeriesInstanceUID(),
            'SeriesDescription' : self.getSeriesDescription(),
            'SeriesNumber' : self.getSeriesNumber(),
            'SeriesDate' : self.getSeriesDate(),
            'SeriesTime' : self.getSeriesTime(),
            'Modality' : self.getModality(),
            'SOPClassUID' : self.getSOPClassUID(),
            'SOPInstanceUID' : self.getSOPInstanceUID(),
            'BodyPart': self.getBodyPart(),
            'DataCollectionDiameter': self.getDataCollectionDiameter(),
            'ReconstructionDiameter': self.getReconstructionDiameter(),
            'Manufacturer' : self.getManufacturer(),
            'ManufacturersModelName' : self.getManufacturersModelName(),
            'DeviceSerialNumber' : self.getDeviceSerialNumber(),
            'ImageType' : self.getImageType(),
            'InstanceNumber' : self.getInstanceNumber(),
            'SliceThickness' : self.getSliceThickness(),
            'PixelSpacing' : self.getPixelSpacing(),
            'ConvolutionKernel' : self.getConvolutionKernel(),
            'Exposure' : self.getExposure(),
            'Kvp' : self.getKvp(),
            'mA' : self.getmA(),
            'StructureSetLabel' : self.getStructureSetLabel(),
            'ReferencedSeriesUID' : self.getReferencedCTUID(),
            'ROIs' : self.getROIs(),
            'FilePath' : self.getFilePath(),
        }
        return info
    
    def getRTSTRUCTInfo(self):
        info = {
            'PatID' : self.getPatId(),
            'PatName' : self.getPatName(),
            'PatientSex' : self.getPatientSex(),
            'StudyID' : self.getStudyID(),
            'StudyInstanceUID' : self.getStudyInstanceUID(),
            'StudyDescription' : self.getStudyDescription(),
            'StudyDate' : self.getStudyDate(),
            'StudyTime' : self.getStudyTime(),
            'SeriesInstanceUID' : self.getSeriesInstanceUID(),
            'SeriesDescription' : self.getSeriesDescription(),
            'SeriesNumber' : self.getSeriesNumber(),
            'SeriesDate' : self.getSeriesDate(),
            'SeriesTime' : self.getSeriesTime(),
            'Modality' : self.getModality(),
            'StructureSetLabel' : self.getStructureSetLabel(),
            'ReferencedSeriesUID' : self.getReferencedCTUID(),
            'SOPClassUID' : self.getSOPClassUID(),
            'SOPInstanceUID' : self.getSOPInstanceUID(),
            'ROIs' : self.getROIs(),
            'FilePath' : self.getFilePath(),
        }
        return info
    
    def getDcmDbPath(self):
        info = {
            'PatID' : self.getPatId(),
            'StudyInstanceUID' : self.getStudyInstanceUID(),
            'SeriesInstanceUID' : self.getSeriesInstanceUID(),
            'SOPInstanceUID' : self.getSOPInstanceUID()
        }
        return f"{info['PatID']}/{info['StudyInstanceUID']}/{info['SeriesInstanceUID']}/{info['SOPInstanceUID']}.dcm"
    
