import sys

class Error:
    def __init__(self, message):
        print("~                                                        ")
        print("~  " + message + "      ")
        print("~                                                        ")
        sys.exit(0)