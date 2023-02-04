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

def calc(from_t, to_t):
    gas = 0
    _FileList = os.listdir(ts_dp_path)
    print(_FileList)
    for f in _FileList:
        _f = File('{base_path}{f}'.format(base_path=ts_dp_path, f=f))
        __f = _f.read()
        for t in __f:
            # get all deploys mapped to timestamp and query gas consumed if timestamp in desired range.

            # timestamp
            #print(t)

            # list of deploys
            #print(__f[t])

            if not __f[t] == []:
                for deploy in __f[t]:
                    # get deploy
                    # convert timestamp
                    # compare to from_t and to_t
                    # if in range: add gas to total consumption
    return gas


'''
test
'''
def test():
    calc(0, 0)
test()
