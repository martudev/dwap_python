#!/usr/bin/env python3

import sys
import os
import os.path
import pickle


def openFileAsReadMode(path_to_file):
    return open(path_to_file, 'r')


def openFileAsWriteMode(path_to_file):
    return open(path_to_file, 'w')


def openFileAsWriteModeAndCreateIfNotExist(path_to_file):
    return open(path_to_file, 'w+')


def existThisFileInDirectory(path, file_name):
    return os.path.exists(path + "/" + file_name)


def existDirectory(path):
    return os.path.exists(path)
