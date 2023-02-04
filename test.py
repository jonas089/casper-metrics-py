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
# download data from node according to config.py => override existing set or create new set.
# auto_download()

''' Generate a subset to calculate gas consumption from ( see subsets.py and gas_consumption.py )
# on demand more subsets and functionality can be implemented
# for now only subset is "tsdp" and is used in gas_consumption.py
from subsets import generate_timestamp_deploy_subset
generate_timestamp_deploy_subset()
'''

''' Gas consumption Example '''
# Example: we want to know gas consumed and amount of deploys of a given type ( transfer / deploy )
# in July 2021
months = ['2021-05']
for month in months:
    print("Total Deploys: ", num_deploys_per_month(month, 'transfer_hashes'))
    print("Consumed Gas (succ, fail): ", consumed_gas_in_range(month))

''' Quickstart
#
# Warning: tsdp is not yet cleared automatically, so make sure to delete it when changing params.
#
#auto_download()
#generate_timestamp_deploy_subset('transfer_hashes')
#YYMM='2021-05'
#print("Total Deploys: ", num_deploys_per_month(YYMM, 'transfer_hashes'))
#print("Consumed Gas (succ, fail): ", consumed_gas_in_range(YYMM))


#
# Warning: might be 0 deploys in 2021-05.
#
#generate_timestamp_deploy_subset('deploy_hashes')
#YYMM='2021-05'
#print("Total Deploys: ", num_deploys_per_month(YYMM, 'deploy_hashes'))
#print("Consumed Gas (succ, fail): ", consumed_gas_in_range(YYMM))
'''
