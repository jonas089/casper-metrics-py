from utils.casper import Client
from utils.File import File, Tree
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
    headers = []
    for i in range(_from, to + 1):
        headers.append(cli.get_block(i))
    path = '{base_path}{fname}'.format(base_path=base_path, fname=fname)
    f = File('{path}'.format(path=path))
    f.create()
    f.write(headers)

def auto_download():
    start_time = time.time()
    _start_height = start_height
    _end_height = start_height + steps
    while _end_height<end_height:
        print("Downloading({_start_height}/{_end_height})".format(_start_height=_start_height, _end_height=_end_height))
        download_blocks(_start_height, _end_height)

        if _start_height == start_height and (str(_start_height)[len(str(start_height)) - 1] == '0'):
            _start_height += 1
        _start_height += steps
        _end_height += steps

# Analyze data in Header files
def prep_header_TREE():
    T = Tree(base_path)
    files = T.filter_from(0)
    with_path = []
    for f in files:
        with_path.append('{base_path}/{f}'.format(base_path=base_path,f=f))
    return with_path
