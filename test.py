# will later be lib.py
import SETUP
from headers import auto_download, prep_header_TREE
from constants import block_path
import time, os
#auto_download()
from utils.File import File, Tree
''' File Tree test
T = Tree('./')
print(T.filenames)
print(T.filter_from('constants'))
'''

# auto_download()

print(prep_header_TREE())
