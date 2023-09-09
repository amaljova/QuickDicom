'''
@ author: Amal Joseph Varghese
@ email: amaljova@gmail.com
@ github: https://github.com/amaljova
@ date:
'''

import pydicom

class RTStruct:
    def __init__(self, file_name) -> None:
        self.header = pydicom.dcmread(file_name)
        
    def getRoiId(self, target_roi):
        for StructureSet in self.header.StructureSetROISequence:
            if StructureSet.ROIName == target_roi:
                return StructureSet.ROINumber
            
    def keepROI(self, target_roi):
        roi_id = self.getRoiId(target_roi)
        for StructureSet in self.header.StructureSetROISequence:
            if StructureSet.ROINumber == roi_id:
                self.header.StructureSetROISequence = pydicom.sequence.Sequence([StructureSet])
                break

        for ContourSequence in self.header.ROIContourSequence:
            if ContourSequence.ReferencedROINumber == roi_id:
                self.header.ROIContourSequence = pydicom.sequence.Sequence([ContourSequence])
                break

        for ObservationsSequence in self.header.RTROIObservationsSequence:
            if ObservationsSequence.ReferencedROINumber == roi_id:
                self.header.RTROIObservationsSequence = pydicom.sequence.Sequence([ObservationsSequence])
                break

    def renameROI(self, target_roi: str, new_name: str):
        for roi in self.header.StructureSetROISequence:
            # If the ROI name is target_roi rename it to new_name
            if roi.ROIName == target_roi:
                roi.ROIName = new_name
           
    def saveFile(self, file_name):
            pydicom.dcmwrite(file_name, self.header)


    # def keepStructureSetROISequence(self, roi_id: str):
    #     for i, StructureSet in enumerate(self.header.StructureSetROISequence):
    #         if StructureSet.ROINumber != roi_id:
    #             del self.header.StructureSetROISequence[i]

    # def keepROIContourSequence(self, roi_id: str):
    #     for i, ContourSequence in enumerate(self.header.ROIContourSequence):
    #         if ContourSequence.ReferencedROINumber != roi_id:
    #             del self.header.ROIContourSequence[i]

    # def keepRTROIObservationsSequence(self, roi_id: str):
    #     for i, ObservationsSequence in enumerate(self.header.RTROIObservationsSequence):
    #         if ObservationsSequence.ReferencedROINumber != roi_id:
    #             del self.header.RTROIObservationsSequence[i]

    # def changeROINumber_StructureSetROISequence(self, roi_id: str):
    #     for i, StructureSet in enumerate(self.header.StructureSetROISequence):
    #         if StructureSet.ROINumber == roi_id:
    #             StructureSet.ROINumber = pydicom.valuerep.IS('1')

    # def changeROINumber_ROIContourSequence(self, roi_id: str):
    #     for i, ContourSequence in enumerate(self.header.ROIContourSequence):
    #         if ContourSequence.ReferencedROINumber == roi_id:
    #             ContourSequence.ReferencedROINumber = pydicom.valuerep.IS('1')

    # def changeROINumber_RTROIObservationsSequence(self, roi_id: str):
    #     for i, ObservationsSequence in enumerate(self.header.RTROIObservationsSequence):
    #         if ObservationsSequence.ReferencedROINumber == roi_id:
    #             ObservationsSequence.ReferencedROINumber = pydicom.valuerep.IS('1')
    #             ObservationsSequence.ObservationNumber = pydicom.valuerep.IS('1')

    # def keepROI(self, target_roi):
    #     roi_id = self.getRoiId(target_roi)
    #     self.keepStructureSetROISequence(roi_id)
    #     self.keepROIContourSequence(roi_id)
    #     self.keepRTROIObservationsSequence(roi_id)

    #     self.changeROINumber_StructureSetROISequence(roi_id)
    #     self.changeROINumber_ROIContourSequence(roi_id)
    #     self.changeROINumber_RTROIObservationsSequence(roi_id)

    # def deleteROI(self, target_roi):
    #     roi_id = self.getRoiId(target_roi)

    #     for i, StructureSet in enumerate(self.header.StructureSetROISequence):
    #         if StructureSet.ROINumber != roi_id:
    #             del self.header.StructureSetROISequence[i]

    #     for i, ContourSequence in enumerate(self.header.ROIContourSequence):
    #         if ContourSequence.ReferencedROINumber == roi_id:
    #             del self.header.ROIContourSequence[i]

    #     for i, ObservationsSequence in enumerate(self.header.RTROIObservationsSequence):
    #         if ObservationsSequence.ReferencedROINumber == roi_id:
    #             del self.header.RTROIObservationsSequence[i]
 