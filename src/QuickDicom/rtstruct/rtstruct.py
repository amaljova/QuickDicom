
import pydicom

# Load the RTSTRUCT file
# rtstruct = pydicom.dcmread("RTSTRUCT.dcm")

# # Find the index of the first ROI
# roi_index = 0

# # Delete the item at that index from both sequences
# del rtstruct.ROIContourSequence[roi_index]
# del rtstruct.RTROIObservationsSequence[roi_index]

# # Save the modified RTSTRUCT file
# pydicom.dcmwrite("RTSTRUCT_modified.dcm", rtstruct)

class RTStruct:
    def __init__(self, file_name) -> None:
        self.header = pydicom.dcmread(file_name)
        pass
        

    def deleteROI(self):
        return self.header
        ...

    def keepROI(self):
        return self.header
        ...

    def renameROI(self):
        return self.header
        ...

