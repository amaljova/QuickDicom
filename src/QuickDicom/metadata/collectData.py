'''
@ author: Amal Joseph Varghese
@ email: amaljova@gmail.com
@ github: https://github.com/amaljova
@ date: 13 June 2023
'''


from .dicomInfo import dcmFile
from QuickDicom import util
from pathlib import Path
from tqdm import tqdm



def getData(target_dir: Path, history = []) -> list:
    '''Give a path, this function will return list of DICOM files metadata
    (Not all metadata, but whatever have specified in the dicomInfo.py)'''
    data_list = []
    # for file in tqdm(Path(target_dir).rglob("*")):
    for file in tqdm(util.getPathsToScan(target_dir, history)):
        if file.is_file():
            try:
                data_list.append(dcmFile(file).getAllInfo())
            except Exception as e:
                print(e)
    print("Done!")
    return data_list

