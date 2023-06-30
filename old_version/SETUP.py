import os
from constants import data_path, block_path, ts_dp_path

if not os.path.exists(data_path):
    os.mkdir(data_path)
if not os.path.exists(block_path):
    os.mkdir(block_path)
if not os.path.exists(ts_dp_path):
    os.mkdir(ts_dp_path)
