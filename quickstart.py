from headers import auto_download, num_deploys_per_month
from subsets import generate_timestamp_deploy_subset
from gas_consumption import consumed_gas_in_range
''' Quickstart '''
#
# Warning: tsdp is not yet cleared automatically, so make sure to delete it when changing params.
#
auto_download()
generate_timestamp_deploy_subset('transfer_hashes')
YYMM='2021-05'
print("Total Deploys: ", num_deploys_per_month(YYMM, 'transfer_hashes'))
print("Consumed Gas (succ, fail): ", consumed_gas_in_range(YYMM))


#
# Warning: might be 0 deploys in 2021-05.
#
generate_timestamp_deploy_subset('deploy_hashes')
YYMM='2021-05'
print("Total Deploys: ", num_deploys_per_month(YYMM, 'deploy_hashes'))
print("Consumed Gas (succ, fail): ", consumed_gas_in_range(YYMM))

''' End of Quickstart '''


''' Quickstart desired Output:

Total Deploys processed:  5488
Total Deploys:  507
[Building] tsdp dataset 2021-05: 100%|█████████████████████████████████████████| 151/151 [08:51<00:00,  3.52s/it]
Consumed Gas (succ, fail):  (884123004560, 131214727109)


'''
