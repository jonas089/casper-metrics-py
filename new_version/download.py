import pycspr, os, pickle, time
from pycspr import NodeClient, NodeConnection
from tqdm import tqdm
from csprtime import dateTime, unixTime

# Constants
nodeIp = "65.108.127.242"
restPort = 8888
rpcPort = 7777
ssePort = 9999
# Config
basePath = './data'
tsdpPath = './tsdp'
blockRange = (0,50000);

# Casper Client
client = NodeClient(NodeConnection(nodeIp, restPort, rpcPort, ssePort))

# Helpers
def createDir():
    if not os.path.exists(basePath):
        os.mkdir(basePath)
    if not os.path.exists(tsdpPath):
        os.mkdir(tsdpPath)
createDir()

# Main
class CasperMetrics:
    def __init__(self, blockRange, steps=1000):
        self.blockRange = blockRange
        self.steps = steps

    def download(self):
        progressBar = tqdm(total=blockRange[1])
        progressBar.set_description("[Downloading]")
        n = 0
        r = [0, self.steps]
        for j in range(blockRange[0], blockRange[1]):
            processed = False
            while not processed:
                try:
                    block = client.get_block(n)
                    processed = True
                    break
                except Exception as error:
                    print("Network error: ", error)
                    time.sleep(0.5)
            fileName = "{}_{}.dat".format(r[0], r[1])
            filePath = "{}/{}".format(basePath, fileName)

            if os.path.exists(filePath):
                with open(filePath, 'rb') as file:
                    blocks = pickle.load(file)
            else:
                blocks = []
            blocks.append(block)
            with open(filePath, 'wb') as file:
                pickle.dump(blocks, file)
            
            
            n += 1
            if n == r[1] and n != blockRange[1] - 1:
                r[0] = n + 1
                r[1] = r[1] + self.steps
            progressBar.update(1)

    def filenames(self):
        names = []
        reminder = (self.blockRange[1] - self.blockRange[0]) % self.steps
        count = int(((self.blockRange[1] - self.blockRange[0]) - reminder) / self.steps)
        for i in range(0, count):
            name = "{}_{}.dat".format(str(self.blockRange[0] + i*(self.steps)+1), str(self.blockRange[0] + i*(self.steps) + self.steps))
            names.append(name)
        return names


    def tsdp(self):
        fileNames = self.filenames()
        for f in fileNames:
            filePath = "{}/{}".format(basePath, f)
            deployHashes = {}
            transferHashes = {}
            tsdpFile = "{}/{}".format(tsdpPath, f)
            if os.path.exists(tsdpFile):
                continue
            if not os.path.exists(filePath):
                continue
            blocks = []
            with open(filePath, 'rb') as blockFile:
                    blocks = pickle.loads(blockFile.read())
            for block in blocks:
                timestamp = block['header']['timestamp']
                if len(block['body']['deploy_hashes']) != 0:   
                    for d in block['body']['deploy_hashes']:
                        deployHashes[timestamp] = d
                if len(block['body']['transfer_hashes']) != 0:   
                    for d in block['body']['transfer_hashes']:
                        transferHashes[timestamp] = d
            with open(tsdpFile, 'wb') as tsdpFile:
                pickle.dump([transferHashes, deployHashes], tsdpFile)

blockchain = CasperMetrics(blockRange)
#blockchain.download()
blockchain.tsdp()

#deploy_hashes, transfer_hashes