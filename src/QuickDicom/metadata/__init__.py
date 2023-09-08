'''
@ author: Amal Joseph Varghese
@ email: amaljova@gmail.com
@ github: https://github.com/amaljova
@ date:
'''

from .dicomInfo import dcmFile
from .collectData import getData


def getAllInfo(file_name):
    return dcmFile(file_name).getDcmDbPath()


def getDcmDbPath(file_name):
    return dcmFile(file_name).getDcmDbPath()
