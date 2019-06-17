#!/usr/bin/env python3

import sys
import os
import os.path
import pickle
import json

path_to_file = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), 'framework', 'app', 'data', 'config.json')

data = ''
with open(path_to_file) as json_file:  
    data = json.load(json_file)
    data['test'] = []
    data['test'].append({  
        'name': 'Scott',
        'website': 'stackabuse.com',
        'from': 'Nebraska'
    })

with open(path_to_file, 'w') as outfile:
    json.dump(data, outfile, sort_keys=True, indent=4)