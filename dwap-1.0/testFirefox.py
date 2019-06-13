#!/usr/bin/env python3
# author: Martin Amengual
# github: UNKNOW
# blog: UNKNOW
# Web: UNKNOW
# youtube: UNKNOW
# License: MIT License
# https://github.com/{github}/thinkdiff/blob/master/LICENSE 

# --------------------------
#      Execute JavaScript
# --------------------------
import sys
import os
import os.path

origin_path = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])))
path_to_app = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), 'framework', 'app')
path_to_modules = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), 'framework', 'app', 'dwap', 'modules')

sys.path.append(path_to_app)

import pickle
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.keys import Keys

def getArgs(idx):
    try:
        return sys.argv[idx]
    except IndexError:
        return

def getEnviroment():
    return getArgs(1)

def printEnviroment():
    if getEnviroment() == 'test':
        print("~  runing in TEST mode.               ")
        print("~                                     ")
    else:
       print("~  runing in default mode.            ")
       print("~                                     ")

try:

    #logo from source http://patorjk.com/software/taag/#p=display&f=Chunky&t=dwap
    print("~                                     ")
    print("~      __                             ")
    print("~  .--|  |.--.--.--.---.-.-----.      ")
    print("~  |  _  ||  |  |  |  _  |  _  |      ")
    print("~  |_____||________|___._|   __|  v1.0")
    print("~                        |__|         ")
    print("~                                     ")

    print("~                                     ")
    print("~  dwap v1.0, https://www.dwap.com    ")
    print("~                                     ")

    print("~  CTRL+C  to stop                    ")
    print("~                                     ")

    printEnviroment()

    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    #chrome_options.add_argument("--window-size=1024x1400")
    chrome_options.add_argument('--user-data-dir=' + os.path.join(origin_path, 'FireFox_User_Data'))

    # download Chrome Webdriver  
    # https://sites.google.com/a/chromium.org/chromedriver/download
    # put driver executable file in the script directory
    chrome_driver = os.path.join(path_to_modules, 'geckodriver')

    firefox_profile = FirefoxProfile()
    firefox_profile.add_extension(os.path.join(path_to_modules, 'Ignore-x.zip'))

    driver = webdriver.Firefox(firefox_options=chrome_options, firefox_profile=firefox_profile, executable_path=chrome_driver)

    driver.get("http://web.whatsapp.com")

    input('Press <ENTER> to stop server')

    driver.close()
    sys.exit(0)

except KeyboardInterrupt:
    print('\nProgram stoped...')
    sys.exit(0)