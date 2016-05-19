#!/usr/bin/env python

import glob
import subprocess

file_list = [ # convert filepaths into dotted python module notation
    file_.replace('/', '.').split('.py')[0] \
    for file_ in glob.glob("lightmoon/tests/test_*.py")
]

if __name__ == '__main__':
    for test_file in file_list:
        subprocess.call(['python', '-m', test_file])
