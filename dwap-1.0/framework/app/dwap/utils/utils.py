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
from selenium.common.exceptions import SessionNotCreatedException
import sys
import os
import os.path
import json

from .ujson import Json
from .ufiles import Files

try:
    from termcolor import colored
except ModuleNotFoundError as e:
    print(e)
    print("\nrun 'pip3 install termcolor' to solve it")
    sys.exit(0)

class Dictionary():
    def __init__():
        return
    
    dwap_env = dict()
    dwap_env['origin_path'] = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])))
    dwap_env['path_to_app'] = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), 'framework', 'app')
    dwap_env['path_to_modules'] = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), 'framework', 'app', 'dwap', 'modules')
    dwap_env['print_network_logs'] = False
    dwap_env['enviroment'] = ''


class Utils(object):
    def __init__():
        return

    def getArgs(idx):
        try:
            return sys.argv[idx]
        except IndexError:
            return ''


    def getEnviroment():
        return Utils.getArgs(1)


    def cmds_program(chrome_options):
        enviroment = Utils.getEnviroment()
        if enviroment == 'test':
            Dictionary.dwap_env['enviroment'] = 'test'
            if Utils.getArgs(2) == '--network':
                Dictionary.dwap_env['print_network_logs'] = True
            print("~  runing in " + Dictionary.dwap_env['enviroment'].upper() + " mode.               ")
            print("~                                     ")
        elif enviroment == 'run':
            Dictionary.dwap_env['enviroment'] = 'dev'
            args = Utils.getArgs(2).split('=')
            if len(args) == 2:
                if args[0] == '--keep':
                    if args[1] == 'chrome':
                        chrome_options.add_experimental_option("detach", True)
                        print("~  with chrome keep open.    ")
                        print("~                            ")
            if Utils.getArgs(2) == '--network':
                Dictionary.dwap_env['print_network_logs'] = True
            args = Utils.getArgs(2).split('%')
            if len(args) == 2:
                if (args[0] == '--'):
                    Dictionary.dwap_env['enviroment'] = args[1]
            print("~  runing in " + Dictionary.dwap_env['enviroment'].upper() + " mode.             ")
            print("~                                      ")
            print("~                                      ")
        elif enviroment == 'help':
            print("~  Usage: dwap <cmd> or dwap <cmd> --[options]=<value>                 ")
            print("~                                                                      ")
            print("~  Commands <cmd>:                                                     ")
            print("~ -------------------                                                  ")
            print("~  * run      Run de WhatsApp framework as default                     ")
            print("~  * test     Run de WhatsApp framework as testing mode                ")
            print("~  * help     Show dwap help                                           ")
            print("~  * set      Set all dwap settings                                    ")
            print("~  * <cmd> --[options]=<value>:   with <value>,  x_value     Example: dwap test --test_wpp=true")
            print("~                                                y_value     For more options write 'dwap --options help'")
            print("~                                                z_value               ")
            print("~                                                                      ")
            print("~                                                                      ")
            print("~                                                                      ")
            print("~                                                                      ")
            print("~  All Example Commands:                                               ")
            print("~ -------------------------                                            ")
            print("~  * dwap run                                                          ")
            print("~  * dwap run --keep=chrome                                            ")
            print("~  * dwap run --network                                                ")
            print("~  * dwap test                                                         ")
            print("~  * dwap test --network                                               ")
            print("~  * dwap set --route                                                  ")
            print("~  * dwap run --%prod                                                  ")
            print("~  * dwap run --%beta                                                  ")
            print("~  * dwap help                                                         ")
            print("~                                                                      ")
            print("~                                                                      ")
            print("~                                                                      ")
            print("~  More Info:  https://www.dwap.com/help                               ")
            print("~                                                                      ")
            sys.exit(0)
        elif enviroment == 'set':
            args = Utils.getArgs(2)
            if args == '--route':
                path = os.getcwd()
                if Utils.existServerJSInPath(path):
                    Utils.setDefaultRoute(Dictionary.dwap_env['path_to_app'], path)
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
                Utils.commandNotFound()
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
        exceptions = []

        ## chromedriver_74
        try:
            chrome_driver = os.path.join(Dictionary.dwap_env['path_to_modules'], 'chromedriver_74')
            chrome_version_options = Options()
            chrome_version_options.add_argument("--headless")
            versionDriver = webdriver.Chrome(options=chrome_version_options, executable_path=chrome_driver)
            browser_version = versionDriver.capabilities['version']
            versionDriver.quit()
            return browser_version.split('.')[0]
        except SessionNotCreatedException as e:
            exceptions.append(e)

        ## chromedriver_75
        try:
            chrome_driver = os.path.join(Dictionary.dwap_env['path_to_modules'], 'chromedriver_75')
            chrome_version_options = Options()
            chrome_version_options.add_argument("--headless")
            versionDriver = webdriver.Chrome(options=chrome_version_options, executable_path=chrome_driver)
            browser_version = versionDriver.capabilities['browserVersion']
            versionDriver.quit()
            return browser_version.split('.')[0]
        except SessionNotCreatedException as e:
            exceptions.append(e)

        ## chromedriver_76
        try:
            chrome_driver = os.path.join(Dictionary.dwap_env['path_to_modules'], 'chromedriver_76')
            chrome_version_options = Options()
            chrome_version_options.add_argument("--headless")
            versionDriver = webdriver.Chrome(options=chrome_version_options, executable_path=chrome_driver)
            browser_version = versionDriver.capabilities['browserVersion']
            versionDriver.quit()
            return browser_version.split('.')[0]
        except SessionNotCreatedException as e:
            exceptions.append(e)

        ## chromedriver_77
        try:
            chrome_driver = os.path.join(Dictionary.dwap_env['path_to_modules'], 'chromedriver_77')
            chrome_version_options = Options()
            chrome_version_options.add_argument("--headless")
            versionDriver = webdriver.Chrome(options=chrome_version_options, executable_path=chrome_driver)
            browser_version = versionDriver.capabilities['browserVersion']
            versionDriver.quit()
            return browser_version.split('.')[0]
        except SessionNotCreatedException as e:
            exceptions.append(e)

        ## chromedriver_78
        try:
            chrome_driver = os.path.join(Dictionary.dwap_env['path_to_modules'], 'chromedriver_78')
            chrome_version_options = Options()
            chrome_version_options.add_argument("--headless")
            versionDriver = webdriver.Chrome(options=chrome_version_options, executable_path=chrome_driver)
            browser_version = versionDriver.capabilities['browserVersion']
            versionDriver.quit()
            return browser_version.split('.')[0]
        except SessionNotCreatedException as e:
            exceptions.append(e)

        ## chromedriver_79
        try:
            chrome_driver = os.path.join(Dictionary.dwap_env['path_to_modules'], 'chromedriver_79')
            chrome_version_options = Options()
            chrome_version_options.add_argument("--headless")
            versionDriver = webdriver.Chrome(options=chrome_version_options, executable_path=chrome_driver)
            browser_version = versionDriver.capabilities['browserVersion']
            versionDriver.quit()
            return browser_version.split('.')[0]
        except SessionNotCreatedException as e:
            exceptions.append(e)

        for e in exceptions:
            print(e)

        if exceptions:
            raise Exception('Too many exceptions in getChromeVersion()')


    def setDefaultRoute(path, path_to_serverJs):
        path_to_config_file = path + '/data/config.json'

        if not Files.existDirectory(path + '/data'):
            os.mkdir(path + '/data')

        if not Files.existThisFileInDirectory(path + '/data', 'config.json'):
            data = {}
            data['route'] = path_to_serverJs
            Json.openFileAndWriteJson(path_to_config_file, data)
        else:
            data = Json.openJson(path_to_config_file)
            data['route'] = path_to_serverJs
            Json.writeJson(path_to_config_file, data)

        return


    def existServerJSInPath(path):
        return Files.existThisFileInDirectory(path, "server.js")


    def getServerScript():
        path_to_config_file = Dictionary.dwap_env['path_to_app'] + '/data'
        if Files.existThisFileInDirectory(path_to_config_file, 'config.json'):
            config_json_data = Json.openJson(path_to_config_file + '/config.json')
            js_file = Files.openFileAsReadMode(config_json_data['route'] + '/server.js')
            js_conf_file = Files.openFileAsReadMode(config_json_data['route'] + '/WhatsAppModels.js')
            return js_conf_file.read() + js_file.read()
        else:
            print("~                                                        ")
            print("~  File 'config.json' not found in /data/ directory      ")
            print("~                                                        ")
            sys.exit(0)
        return


    def print_consolelog_chrome(driver, printScriptNetwork):
        for entry in driver.get_log('browser'):
            level = entry['level']
            if entry['level'] == 'WARNING':
                level = colored(entry['level'], 'yellow')
            elif entry['level'] == 'SEVERE':
                level = colored(entry['level'], 'red')
            print('[' + level + '] ' + entry['message'])

        ## getting network request logs
        if (printScriptNetwork == True):
            browser_log = driver.get_log('performance')
            events = [json.loads(entry['message'])['message'] for entry in browser_log]
            events = [event['params'] for event in events if 'Network.response' in event['method']]
            for req in events:
                if (req['type'] == "Script"):
                    print('[' + str(req['response']['status']) + '] ' + req['response']['url'] + ' | fromDiskCache?: ' + str(req['response']['fromDiskCache']))


    def getConfScript():
        path_to_config_file = Dictionary.dwap_env['path_to_app'] + '/data'
        if Files.existThisFileInDirectory(path_to_config_file, 'config.json'):
            config_json_data = Json.openJson(path_to_config_file + '/config.json')
            config_json_file = Json.openJson(config_json_data['route'] + '/config.json')
            script = ''
            for localStorage in config_json_file[Dictionary.dwap_env['enviroment'] + '.localStorage']:
                name_localStorage = localStorage['name']
                value_localStorage = localStorage['value']
                script += 'console.log("Setting localStorage {name: \'' + name_localStorage + '\', value: \'' + value_localStorage + '\'}");localStorage.setItem(\'' + name_localStorage + '\', \'' + value_localStorage + '\');'
            return script
        else:
            print("~                                                        ")
            print("~  File 'config.json' not found in /data/ directory      ")
            print("~                                                        ")
            sys.exit(0)
        return
