'''
@ author: Amal Joseph Varghese
@ email: amaljova@gmail.com
@ github: https://github.com/amaljova
@ date: 7 September 2023
'''


from pathlib import Path
from QuickDicom.logging import logger


def getPathsToScan(target_dir:Path, history = []) -> set:
    '''Get all the new files
    Give target Directory and history, the files paths to be avoided.
    If no history, all files in the target_dir will be returned.
    '''
    logger.info("Getting File Paths to scan ...")
    present = set(Path(target_dir).rglob("*"))
    history = set([Path(f_path) for f_path in history])
    logger.info("Collected File Paths to scan.")
    return  present - history


