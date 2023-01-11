from utils.casper import Client
from utils.File import File, FileList
from config import start_height, end_height, steps, node_ip
from constants import block_path
import os, time
from tqdm import tqdm

cli = Client(node_ip, 8888, 7777, 9999)
base_path = '{block_path}{start_height}-{end_height}-{steps}/'.format(block_path=block_path, start_height=start_height, end_height=end_height, steps=steps)
if not os.path.exists(base_path):
    os.mkdir(base_path)

def download_blocks(_from, to):
    fname = '{_from}-{to}'.format(_from=_from ,to=to)
    path = '{base_path}{fname}'.format(base_path=base_path, fname=fname)
    f = File('{path}'.format(path=path))
    if os.path.exists('{path}.xml'.format(path=path)):
        time.sleep(0.1)
        return None

    headers = []
    for i in range(_from, to + 1):
        is_processed = False
        while is_processed == False:
            try:
                headers.append(cli.get_block(i))
                is_processed = True
            except Exception as ConnErr:
                print('[Warning] Connection: Failed to process Block')
                time.sleep(0.5)
    print("Headers: ", headers)
    f.create()
    f.write(headers)

def auto_download():
    start_time = time.time()
    _start_height = start_height
    _end_height = start_height + steps
    _total = ((end_height-_end_height)/steps)
    progress_bar = tqdm(total=int(_total))
    progress_bar.set_description("[Downloading] Block Headers:")
    while _end_height<=end_height:
        round_result = download_blocks(_start_height, _end_height)
        if _start_height == start_height and (str(_start_height)[len(str(start_height)) - 1] == '0'):
            _start_height += 1
        _start_height += steps
        _end_height += steps
        progress_bar.update(1)


# Analyze data in Header files
def prep_header_FileList():
    T = FileList(base_path)
    # using entire dataset
    files = T.filter_from(0)
    with_path = []
    for f in files:
        with_path.append('{base_path}{f}'.format(base_path=base_path,f=f))
    return with_path

# Count the amount of deploys for a given Month
# YYMM: 2022-05 or equiv.
def num_deploys_per_month(YYMM, type):
    f = prep_header_FileList()
    c = 0
    for _f in f:
        file = File('{f}'.format(f=_f))
        for block in file.read():
            if block['header']['timestamp'][:7] == YYMM:
                c += len(block['body'][type])
    return c

# Count the amount of blocks for a given Month
# YYMM: 2022-05 or equiv.
def num_blocks_per_month(YYMM):
    f = prep_header_FileList()
    c = 0
    for _f in f:
        file = File('{f}'.format(f=_f))
        for block in file.read():
            if block['header']['timestamp'][:7] == YYMM:
                c += 1
    return c
