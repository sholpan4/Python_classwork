import json
import sys

print(sys.argv)

default_config = {'text': 'filename.txt', 'debuglevel': 'warning', 'mode': 'delayed', 'output': 'stdout'}

with open("config.json", encoding='utf-8') as fd:
    data = json.load(fd)

default_config.update(data)

def get_config(default_config):
    new_config = {}
    for i in range(1, len(default_config)-1):
        if default_config[i] == '--text':
            new_config[default_config[i].lstrip('-')] = default_config[i+1]
        elif default_config[i] == '--debuglevel':
            new_config[default_config[i].lstrip('-')] = default_config[i+1]
        elif default_config[i] == '--mode':
            new_config[default_config[i].lstrip('-')] = default_config[i+1]
        elif default_config[i] == '--output':
            new_config[default_config[i].lstrip('-')] = default_config[i+1]
    return new_config

data = get_config(sys.argv)
default_config.update(data)

print(default_config)
# print(data)
# print(get_config(sys.argv))