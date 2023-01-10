from utils.File import File, FileList
from constants import block_path, ts_dp_path
from headers import prep_header_FileList
from utils.csprtime import to_date_time, to_unix

# map timestamps and deploys -> outputs found in ./data/tsdp/
def timestamp_deploy_subset(type='transfer_hashes'):
    f = prep_header_FileList()
    _block_limit = 1000
    # max: 1000*1000 in memory
    _fc = 0
    data = {}
    for _f in f:
        file = File('{f}'.format(f=_f))
        for block in file.read():
            timestamp = block['header']['timestamp']
            if not data.has_key(to_unix(timestamp)):
                data[timestamp] = block['body'][type]
            else:
                data[timestamp] = data[timestamp] + block['body'][type]
        # after every processed block, check the size of data and increase _fc if limit is exceeded
        if len(data) >= _block_limit:
            # write current memory set to file
            new_file = File('{path}{f}'.format(path=ts_dp_path, f=str(_fc)))
            new_file.create()
            new_file.write(data)
            # start a new file
            data = {}
            _fc += 1
    # final save regardless size
    new_file = File('{path}{f}'.format(path=ts_dp_path, f=str(_fc)))
    new_file.create()
    new_file.write(data)
