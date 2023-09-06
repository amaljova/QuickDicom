from .dicomInfo import dcmFile
from .collectData import getData


def getAllInfo(file_name):
    return dcmFile(file_name).getDcmDbPath()


def getDcmDbPath(file_name):
    return dcmFile(file_name).getDcmDbPath()
