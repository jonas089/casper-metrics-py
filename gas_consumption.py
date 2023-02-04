from utils.File import File
from constants import ts_dp_path
from utils.csprtime import to_date_time, to_unix
import os, pycspr
from utils.casper import Client
from config import node_ip
cli = Client(node_ip, 8888, 7777, 9999)
'''
    This file parses a LOCAL tsdp dataset ( see subsets.py ) to retrieve deploy hashs in a monthly fashion:
    [
        '2022-05':{hash1, hash2, hashn},
        '2022-06':{...},
        ...
    ]

    Deploys are then queried using pycspr and gas consumption metrics are applied similar to V1 of Casper-Metrics

    TBD:
        1. Test tsdp generation in ./data/tsdp/... => DONE
        2. Code this function
        3. Test this function
'''

def calc(from_t, to_t):
    successfull_deploys_gas_consumed = 0
    failed_deploys_gas_consumed = 0
    _FileList = os.listdir(ts_dp_path)
    print(_FileList)
    for f in _FileList:
        _f = File('{base_path}{f}'.format(base_path=ts_dp_path, f=f))
        __f = _f.read()
        for t in __f:
            # get all deploys mapped to timestamp and query gas consumed if timestamp in desired range.

            # timestamp
            #print(t)

            # list of deploys
            #print(__f[t])

            if not __f[t] == []:
                for deploy in __f[t]:
                    d = cli.get_deploy(deploy)
                    # initialize for lifetime reasons
                    gas_consumed = 0
                    try:
                        gas_consumed = d['execution_results'][0]['result']['Success']['cost']
                    except Exception as Failed:
                        gas_consumed = d['execution_results'][0]['result']['Failure']['cost']
                    # convert timestamp
                    # compare to from_t and to_t
                    # if in range: add gas to total consumption
    return (successfull_deploys_gas_consumed, failed_deploys_gas_consumed)


'''
test
'''
def test():
    calc(0, 0)
test()



'''



{'api_version': '1.4.9', 'deploy': {'hash': '700931c8bcf82bd2f0be62e600a39f8c9b0fc8aee6d3f2508c5b8eeb302e0a92',
 'header': {'account': '0203377e3632adb02f6af0a474afad5ac592e10953454aa4d1eae11b90beb7104076', 'timestamp': '2021-05-08T04:03:24.452Z', 'ttl': '1h', 'gas_price': 1, 'body_hash': '242fa50ec9b474f8daecd7ec9141ee09ed46970e5d6cab6f8b0f3902b6079ea3', 'dependencies': [], 'chain_name': 'casper'}, 'payment': {'ModuleBytes': {'module_bytes': '', 'args': [['amount', {'cl_type': 'U512', 'bytes': '021027', 'parsed': '10000'}]]}}, 'session': {'Transfer': {'args': [['amount', {'cl_type': 'U512', 'bytes': '0500c817a804', 'parsed': '20000000000'}], ['target', {'cl_type': {'ByteArray': 32}, 'bytes': 'a053e4ff499bdbd72da79907751974191c67ba819231c2fbc66516afafe6ccd1', 'parsed': 'a053e4ff499bdbd72da79907751974191c67ba819231c2fbc66516afafe6ccd1'}], ['id', {'cl_type': {'Option': 'U64'}, 'bytes': '00', 'parsed': None}]]}}, 'approvals': [{'signer': '0203377e3632adb02f6af0a474afad5ac592e10953454aa4d1eae11b90beb7104076', 'signature': '0295ea83744966568e6eb1d79e11ad22e1be2ef430e66ab503ed5e7c387fa0e13c3fc98d5fbf1b0983ec9a90f208654dcc96b1d5cfcb10a8ef223f9d8cbc6fd969'}]}, 'execution_results': [{'block_hash': '14e69fab00e6448a3a4d303cc63dfd1df22062876b34104c93070ec27da1b9a8', 'result': {'Success': {'effect': {'operations': [{'key': 'uref-d85d8a032aa7af1da61b8f98d13b9b971e1e7fe68fff8cddafd6cd53eda7306c-000', 'kind': 'Write'}, {'key': 'account-hash-a053e4ff499bdbd72da79907751974191c67ba819231c2fbc66516afafe6ccd1', 'kind': 'Write'}, {'key': 'balance-fe327f9815a1d016e1143db85e25a86341883949fd75ac1c1e7408a26c5b62ef', 'kind': 'Read'}, {'key': 'transfer-d85d8a032aa7af1da61b8f98d13b9b971e1e7fe68fff8cddafd6cd53eda7306c', 'kind': 'Write'}, {'key': 'balance-bc205cb525f7f76e911a75e7ccf444f41fafe1a03bb8ac9b1bd37d8f79f910b7', 'kind': 'Write'}, {'key': 'deploy-700931c8bcf82bd2f0be62e600a39f8c9b0fc8aee6d3f2508c5b8eeb302e0a92', 'kind': 'Write'}, {'key': 'hash-d2469afeb99130f0be7c9ce230a84149e6d756e306ef8cf5b8a49d5182e41676', 'kind': 'Read'}, {'key': 'hash-7cc1b1db4e08bbfe7bacf8e1ad828a5d9bcccbb33e55d322808c3a88da53213a', 'kind': 'Read'}, {'key': 'balance-d85d8a032aa7af1da61b8f98d13b9b971e1e7fe68fff8cddafd6cd53eda7306c', 'kind': 'Write'}, {'key': 'balance-855db3849aa8a36845865440003e82ac773d1a7fa76041e2c4fa3786990a41fa', 'kind': 'Write'}], 'transforms': [{'key': 'hash-7cc1b1db4e08bbfe7bacf8e1ad828a5d9bcccbb33e55d322808c3a88da53213a', 'transform': 'Identity'}, {'key': 'account-hash-a053e4ff499bdbd72da79907751974191c67ba819231c2fbc66516afafe6ccd1', 'transform': {'WriteAccount': 'account-hash-a053e4ff499bdbd72da79907751974191c67ba819231c2fbc66516afafe6ccd1'}}, {'key': 'hash-d2469afeb99130f0be7c9ce230a84149e6d756e306ef8cf5b8a49d5182e41676', 'transform': 'Identity'}, {'key': 'balance-bc205cb525f7f76e911a75e7ccf444f41fafe1a03bb8ac9b1bd37d8f79f910b7', 'transform': {'WriteCLValue': {'cl_type': 'U512', 'bytes': '05006c7db15f', 'parsed': '410999680000'}}}, {'key': 'transfer-d85d8a032aa7af1da61b8f98d13b9b971e1e7fe68fff8cddafd6cd53eda7306c', 'transform': {'WriteTransfer': {'deploy_hash': '700931c8bcf82bd2f0be62e600a39f8c9b0fc8aee6d3f2508c5b8eeb302e0a92', 'from': 'account-hash-f23a07530ec17998d229dc654ef86e010f1571e996eb871712c6053a89b154a9', 'to': 'account-hash-a053e4ff499bdbd72da79907751974191c67ba819231c2fbc66516afafe6ccd1', 'source': 'uref-bc205cb525f7f76e911a75e7ccf444f41fafe1a03bb8ac9b1bd37d8f79f910b7-007', 'target': 'uref-d85d8a032aa7af1da61b8f98d13b9b971e1e7fe68fff8cddafd6cd53eda7306c-004', 'amount': '20000000000', 'gas': '0', 'id': None}}}, {'key': 'balance-d85d8a032aa7af1da61b8f98d13b9b971e1e7fe68fff8cddafd6cd53eda7306c', 'transform': {'WriteCLValue': {'cl_type': 'U512', 'bytes': '0500c817a804', 'parsed': '20000000000'}}}, {'key': 'uref-d85d8a032aa7af1da61b8f98d13b9b971e1e7fe68fff8cddafd6cd53eda7306c-000', 'transform': {'WriteCLValue': {'cl_type': 'Unit', 'bytes': '', 'parsed': None}}}, {'key': 'balance-855db3849aa8a36845865440003e82ac773d1a7fa76041e2c4fa3786990a41fa', 'transform': {'AddUInt512': '10000'}}, {'key': 'balance-fe327f9815a1d016e1143db85e25a86341883949fd75ac1c1e7408a26c5b62ef', 'transform': 'Identity'}, {'key': 'deploy-700931c8bcf82bd2f0be62e600a39f8c9b0fc8aee6d3f2508c5b8eeb302e0a92', 'transform': {'WriteDeployInfo': {'deploy_hash': '700931c8bcf82bd2f0be62e600a39f8c9b0fc8aee6d3f2508c5b8eeb302e0a92', 'transfers': ['transfer-d85d8a032aa7af1da61b8f98d13b9b971e1e7fe68fff8cddafd6cd53eda7306c'], 'from': 'account-hash-f23a07530ec17998d229dc654ef86e010f1571e996eb871712c6053a89b154a9', 'source': 'uref-bc205cb525f7f76e911a75e7ccf444f41fafe1a03bb8ac9b1bd37d8f79f910b7-007', 'gas': '10000'}}}]}, 'transfers': ['transfer-d85d8a032aa7af1da61b8f98d13b9b971e1e7fe68fff8cddafd6cd53eda7306c'], 'cost': '10000'}}}]}







'''
