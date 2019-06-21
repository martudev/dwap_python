#!/usr/bin/env python3

import sys
import os
import os.path
import pickle
import json
from .ufiles import *


def openJson(path_to_file):
    with openFileAsReadMode(path_to_file) as json_file:
        return json.load(json_file)


def writeJson(path_to_file, file):
    with openFileAsWriteModeAndCreateIfNotExist(path_to_file) as outfile:
        json.dump(file, outfile, sort_keys=True, indent=4)
        outfile.close()
        return


def openFileAndWriteJson(path_to_file, file):
    writeJson(path_to_file, file)
    return
