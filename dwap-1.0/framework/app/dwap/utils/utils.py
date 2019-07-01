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

try:
    from termcolor import colored
except ModuleNotFoundError as e:
    print(e)
    print("\nrun 'pip3 install termcolor' to solve it")
    sys.exit(0)

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


def cmds_program(chrome_options):
    enviroment = getEnviroment()
    if enviroment == 'test':
        print("~  runing in TEST mode.               ")
        print("~                                     ")
    elif enviroment == 'run':
        print("~  runing in default mode.             ")
        print("~                                      ")
        print("~                                      ")
        args = getArgs(2).split('=')
        if len(args) == 2:
            if args[0] == '--keep':
                if args[1] == 'chrome':
                    chrome_options.add_experimental_option("detach", True)
                    print("~  with chrome keep open.    ")
                    print("~                            ")
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
        print("~  * route         Change a route directory in settings           Example: dwap change --route")
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
        print("~                                                                      ")
        print("~  More Info:  https://www.dwap.com/help                               ")
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
                new_path = revertDefaultRoute(dwap_env['path_to_app'])
                if new_path is None:
                    print("~                                        ")
                    print("~  Error! /data/ folder not exist.   Run dwap change --route to create /data/ folder")
                    print("~                                        ")
                else:
                    print("~                                               ")
                    print("~  Done! changed default route to '" + new_path + "'")
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
    versionDriver.quit()
    return browser_version.split('.')[0]


def changeDefaultRoute(path, path_to_serverJs):
    path_to_config_file = path + '/data/config.json'
    path_to_cbackup_file = path + '/data/config.backup.json'

    if not existDirectory(path + '/data'):
        os.mkdir(path + '/data')

    first_time_config_file = False
    if not existThisFileInDirectory(path + '/data', 'config.json'):
        data = {}
        data['route'] = path_to_serverJs
        openFileAndWriteJson(path_to_config_file, data)
        first_time_config_file = True
    else:
        data = openJson(path_to_config_file)
        data['route'] = path_to_serverJs
        writeJson(path_to_config_file, data)

    if not existThisFileInDirectory(path + '/data', 'config.backup.json') and first_time_config_file:
        data = {}
        data['route'] = path_to_serverJs
        openFileAndWriteJson(path_to_cbackup_file, data)

    return


def setDefaultRoute(path, path_to_serverJs):
    path_to_config_file = path + '/data/config.json'
    path_to_cbackup_file = path + '/data/config.backup.json'

    if not existDirectory(path + '/data'):
        os.mkdir(path + '/data')

    if not existThisFileInDirectory(path + '/data', 'config.json'):
        data = {}
        data['route'] = path_to_serverJs
        openFileAndWriteJson(path_to_config_file, data)
    else:
        data = openJson(path_to_config_file)
        data['route'] = path_to_serverJs
        writeJson(path_to_config_file, data)

    if not existThisFileInDirectory(path + '/data', 'config.backup.json'):
        data = {}
        data['route'] = path_to_serverJs
        openFileAndWriteJson(path_to_cbackup_file, data)
    else:
        data = openJson(path_to_cbackup_file)
        data['route'] = path_to_serverJs
        writeJson(path_to_cbackup_file, data)

    return


def revertDefaultRoute(path):
    path_to_config_file = path + '/data/config.json'
    path_to_cbackup_file = path + '/data/config.backup.json'

    if not existDirectory(path + '/data'):
        return None

    path_route = None
    if existThisFileInDirectory(path + '/data', 'config.backup.json'):
        data = openJson(path_to_cbackup_file)
        path_route = data['route']

    if existThisFileInDirectory(path + '/data', 'config.json'):
        data = openJson(path_to_config_file)
        data['route'] = path_route
        writeJson(path_to_config_file, data)

    return path_route


def existServerJSInPath(path):
    return existThisFileInDirectory(path, "server.js")


def getServerScript():
    path_to_config_file = dwap_env['path_to_app'] + '/data'
    if existThisFileInDirectory(path_to_config_file, 'config.json'):
        config_json_data = openJson(path_to_config_file + '/config.json')
        js_file = openFileAsReadMode(config_json_data['route'] + '/server.js')
        return js_file.read()
    else:
        print("~                                                        ")
        print("~  File 'config.json' not found in /data/ directory      ")
        print("~                                                        ")
        sys.exit(0)
    return


def print_consolelog_chrome(driver):
    for entry in driver.get_log('browser'):
        level = entry['level']
        if entry['level'] == 'WARNING':
            level = colored(entry['level'], 'yellow')
        elif entry['level'] == 'SEVERE':
            level = colored(entry['level'], 'red')
        print('[' + level + '] ' + entry['message'])


def getConfScript():
    path_to_config_file = dwap_env['path_to_app'] + '/data'
    if existThisFileInDirectory(path_to_config_file, 'config.json'):
        config_json_data = openJson(path_to_config_file + '/config.json')
        config_json_file = openJson(config_json_data['route'] + '/config.json')
        script = ''
        for localStorage in config_json_file['localStorage']:
            name_localStorage = localStorage['name']
            value_localStorage = localStorage['value']
            script += 'console.log(\'Setting localStorage {name: \'' + name_localStorage + '\', value: \'' + value_localStorage + '\'}\');localStorage.setItem(\'' + name_localStorage + '\', \'' + value_localStorage + '\');'
        return script
    else:
        print("~                                                        ")
        print("~  File 'config.json' not found in /data/ directory      ")
        print("~                                                        ")
        sys.exit(0)
    return
