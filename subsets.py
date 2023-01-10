from utils.File import File, FileList
from constants import block_path, ts_dp_path
from headers import prep_header_FileList
from utils.csprtime import to_date_time, to_unix
def timestamp_deploy_subset():
    f = prep_header_FileList()
    _fc = 0
    data = {}
    for _f in f:
        file = File('{f}'.format(f=_f))
        for block in file.read():
            timestamp = block['header']['timestamp']
            if not data.has_key(to_unix(timestamp)):
                data[timestamp] = 
