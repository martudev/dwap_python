#!/usr/bin/env python3
# author: Martin Amengual
# github: UNKNOW
# blog: UNKNOW
# Web: UNKNOW
# youtube: UNKNOW
# License: MIT License
# https://github.com/{github}/thinkdiff/blob/master/LICENSE

# --------------------------
#      Utils
# --------------------------

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import sys
import os
import os.path

from .ujson import *

dwap_env = dict()

dwap_env['origin_path'] = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])))
dwap_env['path_to_app'] = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), 'framework', 'app')
dwap_env['path_to_modules'] = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), 'framework', 'app', 'dwap', 'modules')


def getArgs(idx):
    try:
        return sys.argv[idx]
    except IndexError:
        return ''


def getEnviroment():
    return getArgs(1)


def cmds_program():
    enviroment = getEnviroment()
    if enviroment == 'test':
        print("~  runing in TEST mode.               ")
        print("~                                     ")
    elif enviroment == 'run':
        print("~  runing in default mode.             ")
        print("~                                      ")
    elif enviroment == 'help':
        print("~  Usage: dwap <cmd> or dwap <cmd> --[options]=<value>.                ")
        print("~                                                                      ")
        print("~  Commands <cmd>:                                                     ")
        print("~ -------------------                                                  ")
        print("~  * run      Run de WhatsApp framework as default                     ")
        print("~  * test     Run de WhatsApp framework as testing mode                ")
        print("~  * help     Show dwap help                                           ")
        print("~  * <cmd> --[options]=<value>:   with <value>,  x_value     Example: dwap test --test_wpp=true")
        print("~                                                y_value     For more options write 'dwap --options help'")
        print("~                                                z_value               ")
        print("~                                                                      ")
        print("~                                                                      ")
        print("~  Options [options]:                                                  ")
        print("~ --------------------                                                 ")
        print("~  * test_wpp      Run de WhatsApp framework as default           Example: dwap test --test_wpp=true")
        print("~                                                                      ")
        print("~                                                                      ")
        print("~  All Example Commands:                                                   ")
        print("~ -------------------------                                            ")
        print("~  * dwap run                                                          ")
        print("~  * dwap test                                                         ")
        print("~  * dwap test --test_wpp=true                                         ")
        print("~  * dwap change --default=[name_of_folder]                            ")
        print("~  * dwap set --default=[name_of_folder]                               ")
        print("~  * dwap help                                                         ")
        print("~                                                                      ")
        print("~                                                                      ")
        sys.exit(0)
    elif enviroment == 'change':
        args = getArgs(2).split('=')
        if args[0] == '--default':
            if '=' in getArgs(2):
                if len(args[1]) >= 1:
                    changeDefaultFolder(dwap_env['path_to_app'], args[1])
                    print("~                                                     ")
                    print("~  Done! changed default folder to '" + args[1] + "'")
                    print("~                                                     ")
                    sys.exit(0)
                else:
                    print("~                                                     ")
                    print("~  Not name of folder! please write a folder name     ")
                    print("~                                                     ")
                    sys.exit(0)
            else:
                commandNotFound()
                sys.exit(0)
        else:
            commandNotFound()
            sys.exit(0)
    elif enviroment == 'set':
        args = getArgs(2).split('=')
        if args[0] == '--default':
            if '=' in getArgs(2):
                if len(args[1]) > 1:
                    setDefaultFolder(dwap_env['path_to_app'], args[1])
                    print("~                                                     ")
                    print("~  Done! seted default folder to '" + args[1] + "'")
                    print("~                                                     ")
                    sys.exit(0)
                else:
                    print("~                                                     ")
                    print("~  Not name of folder! please write a folder name     ")
                    print("~                                                     ")
                    sys.exit(0)
            else:
                commandNotFound()
                sys.exit(0)
    elif enviroment == 'revert':
        args = getArgs(2).split('=')
        if args[0] == '--default':
            revertDefaultFolder(dwap_env['path_to_app'])
            print("~                                              ")
            print("~  Done! reverted default folder.              ")
            print("~                                              ")
            sys.exit(0)
        else:
            commandNotFound()
            sys.exit(0)
    else:
        print("~  Usage: dwap <cmd> --options [options, ...].                         ")
        print("~                                                                      ")
        print("~  with <cmd>,   run     Run de WhatsApp framework as default          ")
        print("~                test    Run de WhatsApp framework as testing mode     ")
        print("~                help    Show dwap help                                ")
        print("~                                                                      ")
        sys.exit(0)


def commandNotFound():
    print("~                                       ")
    print("~  Command not found.  See dwap help    ")
    print("~                                       ")
    return


def getChromeVersion():
    chrome_driver = os.path.join(dwap_env['path_to_modules'], 'chromedriver_74')
    chrome_version_options = Options()
    chrome_version_options.add_argument("--headless")  # lo hacemos para minimizar el chrome ya que solo queremos obtener la version
    versionDriver = webdriver.Chrome(options=chrome_version_options, executable_path=chrome_driver)  # 'chromedriver_74' => 'version' | 'chromedriver_75' => 'browserVersion'
    browser_version = versionDriver.capabilities['version']
    versionDriver.close()
    return browser_version.split('.')[0]


def changeDefaultFolder(path, name_folder):
    path_to_file = path + '/data/config.json'
    config = openJson(path_to_file)
    config['default-folder'] = name_folder
    writeJson(path_to_file, config)
    return


def setDefaultFolder(path, name_folder):
    path_to_file = path + '/data/config.json'
    config = openJson(path_to_file)
    config['default-folder'] = name_folder
    writeJson(path_to_file, config)

    path_to_file = path + '/data/config.backup.json'
    config = openJson(path_to_file)
    config['default-folder'] = name_folder
    writeJson(path_to_file, config)
    return


def revertDefaultFolder(path):
    path_to_file = path + '/data/config.backup.json'
    config = openJson(path_to_file)
    name_folder = config['default-folder']

    path_to_file = path + '/data/config.json'
    config = openJson(path_to_file)
    config['default-folder'] = name_folder
    writeJson(path_to_file, config)
    return
