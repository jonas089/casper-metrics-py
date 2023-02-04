import SETUP
from headers import auto_download, prep_header_FileList, num_deploys_per_month
from gas_consumption import consumed_gas_in_range
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

'''
from subsets import generate_timestamp_deploy_subset
generate_timestamp_deploy_subset()
'''


''' Chat GPT function test
T = FileList('./data/blocks/0-150000-1000/')
filter_from = T.filter_from(2001)
filter_from_GPT = T.filter_from_GPT(2001)
assert(filter_from==filter_from_GPT)
''' # passed.

''' Gas consumption Example '''
# Example: we want to know gas consumed and amount of deploys of a given type ( transfer / deploy )
# in July 2021
months = ['2021-05']
for month in months:
    print("Total Deploys: ", num_deploys_per_month(month, 'transfer_hashes'))
    print("Consumed Gas (succ, fail): ", consumed_gas_in_range(month))
