'''
@ author: Amal Joseph Varghese
@ email: amaljova@gmail.com
@ github: https://github.com/amaljova
@ date: 13 June 2023
'''


from .dicomInfo import dcmFile
from pathlib import Path
from tqdm import tqdm



def getData(base: Path) -> list:
    '''Give a path, this function will return list of DICOM files metadata'''
    data_list = []
    for file in tqdm(Path(base).rglob("*")):
        if file.is_file():
            try:
                data_list.append(dcmFile(file).getAllInfo())
            except Exception as e:
                print(e)
    print("Done!")
    return data_list

