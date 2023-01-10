# will later be lib.py
import SETUP
from headers import auto_download, prep_header_FileList, num_deploys_per_month
from constants import block_path
import time, os
#auto_download()
from utils.File import File, FileList
''' File FileList test
T = FileList('./')
print(T.filenames)
print(T.filter_from('constants'))
'''

# auto_download()

print(prep_header_FileList())
print(num_deploys_per_month('2021-04', 'transfer_hashes '))
