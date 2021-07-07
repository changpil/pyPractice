# This is Chang
"""
Init: create “1”, “2”, “3” folder
    Check  all the files and Put the file name in list
    Loop
        for each file
        open the file
        Check the file
            line: line[0] - - a file can empty.
        If line[0] in (“1”, “2”, “3”) then
            Put the file in the folder
"""
import os
import glob
import collections
import shutil


def accessFiles():
    dirs = ['1', '2', '3']
    ds = set(os.listdir())
    for d in dirs:
        if d not in ds:
            os.mkdir(d)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    sf = glob.glob(dir_path)

    moveFiles = collections.defaultdict([])
    for _file in sf:
        with open(_file, 'r') as f:
            for line in f:
                try:
                    if line[0] in dirs:
                        moveFiles[line[0]].append(_file)
                finally:
                    break

    for folder, filelist in moveFiles.items():
        for f in filelist:
            shutil.move(f, os.path.join(dir_path, folder))
