from utils.File import File
from constants import ts_dp_path
from utils.csprtime import to_date_time, to_unix
import os, pycspr

'''
    This file parses a LOCAL tsdp dataset ( see subsets.py ) to retrieve deploy hashs in a monthly fashion:
    [
        '2022-05':{hash1, hash2, hashn},
        '2022-06':{...},
        ...
    ]

    Deploys are then queried using pycspr and gas consumption metrics are applied similar to V1 of Casper-Metrics

    TBD:
        1. Test tsdp generation in ./data/tsdp/... => DONE
        2. Code this function
        3. Test this function
'''

def calc():
    gas = 0
    _FileList = os.listdir(ts_dp_path)
    for f in _FileList:
        _f = File('{base_path}{f}'.format(base_path=ts_dp_path, f=f))
        for t in _f.read():
            # get all deploys mapped to timestamp and query gas consumed if timestamp in desired range.


    return gas
