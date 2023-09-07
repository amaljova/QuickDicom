'''
@ author: Amal Joseph Varghese
@ email: amaljova@gmail.com
@ github: https://github.com/amaljova
@ date: 13 June 2023
'''


from .dicomInfo import dcmFile
from pathlib import Path
from tqdm import tqdm



def getPathsToScan(base:Path, history = []) -> set:
    '''Get all the new files'''
    present = set(Path(base).rglob("*"))
    history = set([Path(f_path) for f_path in history])
    return  present - history


def getData(base: Path, history = []) -> list:
    '''Give a path, this function will return list of DICOM files metadata
    (Not all metadata, but whatever have specified in the dicomInfo.py)'''
    data_list = []
    # for file in tqdm(Path(base).rglob("*")):
    for file in tqdm(getPathsToScan(base, history)):
        if file.is_file():
            try:
                data_list.append(dcmFile(file).getAllInfo())
            except Exception as e:
                print(e)
    print("Done!")
    return data_list

