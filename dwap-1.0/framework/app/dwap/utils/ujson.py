#!/usr/bin/env python3

import sys
import os
import os.path
import pickle
import json

def openJson(path_to_file):
    with open(path_to_file) as json_file:  
        return json.load(json_file)

def writeJson(path_to_file, file):
    with open(path_to_file, 'w') as outfile:
        json.dump(file, outfile, sort_keys=True, indent=4)
        return