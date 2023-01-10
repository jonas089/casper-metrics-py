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
