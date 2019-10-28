import json
import os
from functools import lru_cache


@lru_cache(maxsize=10)
def get_properties(key=None):
    basePath = os.getcwd()
    filePath = basePath + '/assets/properties.json'
    with open(filePath, 'r') as f:
        data = json.load(f)
    if key==None:
        return data
    return data[key]


def update_current(current_id):
    basePath = os.getcwd()
    filePath = basePath + '/assets/properties.json'
    data = get_properties()
    with open(filePath, 'w') as f:
        data['current_id'] = current_id
        json.dump(data,f)
