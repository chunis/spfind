#!/usr/bin/python3
# -*- coding: utf-8 -*-


import os
import sys
import shutil
import subprocess


def openfile(file):
    #desktop.open(file)
    if sys.platform.startswith('darwin'):
        subprocess.call(('open', file))
    elif os.name == 'nt':
        os.startfile(file)
    elif os.name == 'posix':
        subprocess.call(('xdg-open', file))
        #if file.endswith('.pdf'):
        #    subprocess.call(('mupdf', file))
        #else:
        #    subprocess.call(('xdg-open', file))

def copyfile(src, dst):
    shutil.copy(src, dst)

def movefile(src, dst):
    shutil.move(src, dst)
