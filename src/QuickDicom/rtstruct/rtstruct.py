
import pydicom

# del rtstruct.ROIContourSequence[roi_index]
# del rtstruct.RTROIObservationsSequence[roi_index]

class RTStruct:
    def __init__(self, file_name) -> None:
        self.header = pydicom.dcmread(file_name)
        
    def renameROI(self, target_roi: str, new_name: str):
        try:
            for roi in self.header.StructureSetROISequence:
                # If the ROI name is target_roi rename it to new_name
                if roi.ROIName.lower() == target_roi.lower():
                    roi.ROIName = new_name
        except:
            raise ValueError('Error!')

    def getRoiId(self, target_roi):
        try:
             for roi in self.header.StructureSetROISequence:
                if roi.ROIName == target_roi:
                    return roi.ROINumber
        except:
            raise ValueError('Error!')
        
    def keepROI(self, target_roi):
        try:
            ROI_id = self.getRoiId(target_roi)
            for ROIContourSequence in self.header.ROIContourSequence:
                if ROIContourSequence.ReferencedROINumber != ROI_id:
                    del ROIContourSequence
        except:
            raise ValueError("Error!")
        try:
            for ObservationsSequence in self.header.RTROIObservationsSequence:
                if ObservationsSequence.ReferencedROINumber != ROI_id:
                    del ObservationsSequence
        except:
            raise ValueError('Error!')

    def deleteROI(self, target_roi):
        try:
            ROI_id = self.getRoiId(target_roi)
            for ROIContourSequence in self.header.ROIContourSequence:
                if ROIContourSequence.ReferencedROINumber == ROI_id:
                    del ROIContourSequence
        except:
            raise ValueError("Error!")
        try:
            for ObservationsSequence in self.header.RTROIObservationsSequence:
                if ObservationsSequence.ReferencedROINumber == ROI_id:
                    del ObservationsSequence
        except:
            raise ValueError('Error!')
                
    def saveFile(self, file_name):
        try:
            pydicom.dcmwrite(file_name, self.header)
        except:
            raise ValueError('Error!')
   
