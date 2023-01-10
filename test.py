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
# download data according to config.py
# auto_download()

# Count deploys in Blocks of Month YYMM -> specify the deploy_type (transfer_hashes or deploy_hashes)
# print(num_deploys_per_month('2021-04', 'transfer_hashes'))


from subsets import timestamp_deploy_subset
timestamp_deploy_subset()
