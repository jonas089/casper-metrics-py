# Casper Metrics Explorer

a tool built to analyse block headers and deploy results on the Casper Blockchain.

## 1. Headers

Every Block has a header associated with it which roughly describes the deploys included in it. \
Blocks are downloaded from a node_ip ( see config ) and stored in ./data/blocks/*

## 2. Deploys

Block headers can be parsed to count deploys in a given Block or perform other useful operations. \
Deploy hashs in Blocks can be queried using the pycspr library to further analyse execution results. \
A measure that can be taken from execution results is the average gas cost per deploy / block / time interval. \

## 3. Subsets

A subset stores temporary data in any directory ( not "blocks" ) in ./data/ \
The "blocks" directory is reserved for block headers downloaded from a peer and stored locally ( permanently ) \
Subsets are useful to avoid intense memory usage when parsing a large load of block headers.

## Quickstart
quickstart.py:
1. downloads dataset
2. creates subset
3. counts total deploys of given type
4. analyses gas consumption in deploys
according to config.py \
The larger the range of blocks, the longer this will take. \
Time it took to download blocks 0 - 150000: 90 minutes. \
Expect a few hours to download a complete dataset. \
Generating subset(s) should be much faster. \


Quickstart desired Output:
```
Total Deploys processed:  5488
Total Deploys:  507
[Building] tsdp dataset 2021-05: 100%|█████████████████████████████████████████| 151/151 [08:51<00:00,  3.52s/it]
Consumed Gas (succ, fail):  (884123004560, 131214727109)
```
