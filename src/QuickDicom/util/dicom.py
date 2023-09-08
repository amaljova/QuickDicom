'''
@ author: Amal Joseph Varghese
@ email: amaljova@gmail.com
@ github: https://github.com/amaljova
@ date:
'''

import pandas as pd


def getMissingSlices(df: pd.DataFrame):
    present = set(df.InstanceNumber)
    expected = set(range(1, int(df.InstanceNumber.max()) +1 ))
    absent = list(expected - present)
    absent.sort()
    return absent