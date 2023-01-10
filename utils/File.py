import os, pickle
class File:
    def __init__(self, path):
        self.path = '{path}'.format(path=path)
    def create(self):
        if os.path.exists('{path}.xml'.format(path=self.path)):
            return False
        open('{path}.xml'.format(path=self.path), 'x')
    def read(self):
        if not os.path.exists(self.path):
            return False
        with open(self.path, 'rb') as f:
            return pickle.load(f)
    def write(self, data):
        if not os.path.exists(self.path):
            return False
        with open(self.path, 'wb') as f:
            pickle.dump(data, f)
class FileList:
    def __init__(self, path):
        self.filenames = os.listdir(path)
    def filter_from(self, start_height):
        # custom sorting algorithm
        _From = []
        for filename in self.filenames:
            _from = ''
            brk = False
            for s in filename:
                if s != '-' and brk == False:
                    _from += s
                else:
                    brk = True
            _From.append(_from)
        _sorted_From = []
        _smallest = 99999999999
        for __f in self.filenames:
            for f in _From:
                if int(f) < _smallest:
                    _smallest = int(f)
            for _f in self.filenames:
                if _f.startswith(str(_smallest)):
                    _sorted_From.append(_f)
                    _From.remove(str(_smallest))
                    _smallest = 99999999999
        self.filenames = _sorted_From
        # files have been sorted in ascending order.
        # apply filter to sorted files.
        index = 0
        for filename in self.filenames:
            index += 1
            if filename.startswith(str(start_height)):
                return self.filenames[index - 1:]
    # creates a new set of filenames for division of deploys
    # keep in mind to prefix the path of the files when using this fn
    def new_set(start_height, end_height, steps):
        _start_height = start_height
        _end_height = start_height + steps
        set = []
        while _end_height <= end_height:
            set.append('{_start_height}-{_end_height}.xml'.format(_start_height=_start_height, _end_height=_end_height))
            if _start_height == start_height and str(_start_height)[len(start_height) - 1] == '0':
                _start_height += 1
            _start_height += steps
            _end_height += steps
        return set
