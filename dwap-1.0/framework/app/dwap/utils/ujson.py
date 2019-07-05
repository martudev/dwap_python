#!/usr/bin/env python3

import sys
import os
import os.path
import pickle
import json
from .ufiles import Files

class Json():
    def __init__(self):
        return

    def openJson(path_to_file):
        with Files.openFileAsReadMode(path_to_file) as json_file:
            return json.load(json_file)


    def writeJson(path_to_file, file):
        with Files.openFileAsWriteModeAndCreateIfNotExist(path_to_file) as outfile:
            json.dump(file, outfile, sort_keys=True, indent=4)
            outfile.close()
            return


    def openFileAndWriteJson(path_to_file, file):
        Files.writeJson(path_to_file, file)
        return
