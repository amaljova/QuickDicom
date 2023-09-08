'''
@ author: Amal Joseph Varghese
@ email: amaljova@gmail.com
@ github: https://github.com/amaljova
@ date: 7 September 2023
'''


from pathlib import Path


def getPathsToScan(base:Path, history = []) -> set:
    '''Get all the new files'''
    present = set(Path(base).rglob("*"))
    history = set([Path(f_path) for f_path in history])
    return  present - history


