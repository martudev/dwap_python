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
        print("~  Usage: dwap <cmd> or dwap <cmd> --[options]=<value>                 ")
        print("~                                                                      ")
        print("~  Commands <cmd>:                                                     ")
        print("~ -------------------                                                  ")
        print("~  * run      Run de WhatsApp framework as default                     ")
        print("~  * test     Run de WhatsApp framework as testing mode                ")
        print("~  * help     Show dwap help                                           ")
        print("~  * <cmd> --[options]=<value>:   with <value>,  x_value     Example: dwap test --test_wpp=true")
        print("~                                                y_value     For more options write 'dwap --options help'")
        print("~                                                z_value               ")
        print("~  * change   Change one dwap settings                                 ")
        print("~  * set      Set all dwap settings                                    ")
        print("~  * revert   Revert one dwap settings                                 ")
        print("~                                                                      ")
        print("~                                                                      ")
        print("~  Options [options]:                                                  ")
        print("~ --------------------                                                 ")
        print("~  * test_wpp      Run de WhatsApp framework as default           Example: dwap test --test_wpp=true")
        print("~                                                                      ")
        print("~                                                                      ")
        print("~  All Example Commands:                                               ")
        print("~ -------------------------                                            ")
        print("~  * dwap run                                                          ")
        print("~  * dwap test                                                         ")
        print("~  * dwap test --test_wpp=true                                         ")
        print("~  * dwap change --route                                               ")
        print("~  * dwap set --route                                                  ")
        print("~  * dwap revert --route                                               ")
        print("~  * dwap help                                                         ")
        print("~                                                                      ")
        print("~                                                                      ")
        sys.exit(0)
    elif enviroment == 'change':
        args = getArgs(2)
        if args == '--route':
            path = os.getcwd()
            if existServerJSInPath(path):
                changeDefaultRoute(dwap_env['path_to_app'], path)
                print("~                                               ")
                print("~  Done! changed default route to '" + path + "'")
                print("~                                               ")
                sys.exit(0)
            else:
                print("~                                              ")
                print("~  Not found 'server.js' in this path          ")
                print("~                                              ")
                sys.exit(0)
        else:
            commandNotFound()
            sys.exit(0)
    elif enviroment == 'set':
        args = getArgs(2)
        if args == '--route':
            path = os.getcwd()
            if existServerJSInPath(path):
                setDefaultRoute(dwap_env['path_to_app'], path)
                print("~                                               ")
                print("~  Done! changed default route to '" + path + "'")
                print("~                                               ")
                sys.exit(0)
            else:
                print("~                                              ")
                print("~  Not found 'server.js' in this path          ")
                print("~                                              ")
                sys.exit(0)
        else:
            commandNotFound()
            sys.exit(0)
    elif enviroment == 'revert':
        args = getArgs(2)
        if args == '--route':
            path = os.getcwd()
            if existServerJSInPath(path):
                revertDefaultRoute(dwap_env['path_to_app'])
                print("~                                               ")
                print("~  Done! changed default route to '" + path + "'")
                print("~                                               ")
                sys.exit(0)
            else:
                print("~                                              ")
                print("~  Not found 'server.js' in this path          ")
                print("~                                              ")
                sys.exit(0)
        else:
            commandNotFound()
            sys.exit(0)
    else:
        print("~  Usage: dwap <cmd> --[options]=<value>                               ")
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


def changeDefaultRoute(path, path_to_serverJs):
    path_to_file = path + '/data/config.json'
    config = openJson(path_to_file)
    config['route'] = path_to_serverJs
    writeJson(path_to_file, config)
    return


def setDefaultRoute(path, path_to_serverJs):
    path_to_file = path + '/data/config.json'
    config = openJson(path_to_file)
    config['route'] = name_path_to_serverJsfolder
    writeJson(path_to_file, config)

    path_to_file = path + '/data/config.backup.json'
    config = openJson(path_to_file)
    config['route'] = path_to_serverJs
    writeJson(path_to_file, config)
    return


def revertDefaultRoute(path):
    path_to_file = path + '/data/config.backup.json'
    config = openJson(path_to_file)
    name_folder = config['route']

    path_to_file = path + '/data/config.json'
    config = openJson(path_to_file)
    config['route'] = name_folder
    writeJson(path_to_file, config)
    return

def existThisFileInDirectory(path, file_name):
    return os.path.exists(path + "/" + file_name)

def existServerJSInPath(path):
    return existThisFileInDirectory(path, "server.js")