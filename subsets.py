from utils.File import File, FileList
from constants import block_path, ts_dp_path
from headers import prep_header_FileList
from utils.csprtime import to_date_time, to_unix
def timestamp_deploy_subset():
    f = prep_header_FileList()
    for _f in f:
        file = File('{f}'.format(f=_f))
        for block in file.read():
            timestamp = block['header']['timestamp']
            print(to_unix(timestamp))
