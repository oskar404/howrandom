#!/usr/bin/env python3

import base64
import json
import os
import requests


API_URL = 'https://api.random.org/json-rpc/2/invoke'
API_KEY_FILE = '.random.org.apikey'
RESULT_BIN = 'random.org.bin'
RESULT_TXT = 'random.org.txt'


def get_api_key(file):
    if os.path.isfile(file):
        with open(file) as f:
            return f.read().strip()
    return None


def get_bytes(key):
    data = {
        'jsonrpc': '2.0',
        'method': 'generateBlobs',
        'params': {
            'apiKey': key,
            'n': 1,
            'size': 128*8,
            'format': 'base64'
            },
        'id': 42
    }
    response = requests.post(API_URL, json=data)
    response.raise_for_status()
    result = response.json()
    print(json.dumps(result, indent=2))
    assert 'result' in result, f"Blob query failed: {result.get('error')}"
    rand_data = bytes(result['result']['random']['data'][0], encoding='ascii')
    return base64.decodebytes(rand_data)


def get_strings(key):
    data = {
        'jsonrpc': '2.0',
        'method': 'generateStrings',
        'params': {
            'apiKey': key,
            'n': 32,
            'length': 4,
            'characters': 'ABCDEFGHIJKLMNOPQRSTUVXYZ',
            'replacement': True
            },
        'id': 0xDEADBEEF
    }
    response = requests.post(API_URL, json=data)
    response.raise_for_status()
    result = response.json()
    print(json.dumps(result, indent=2))
    assert 'result' in result, f"Blob query failed: {result.get('error')}"
    return ''.join(result['result']['random']['data'])


def main():
    key = get_api_key(API_KEY_FILE)
    assert key, f"API Key not found: {API_KEY_FILE}"
    random_bytes = get_bytes(key)
    with open(RESULT_BIN, 'wb') as f:
        f.write(random_bytes)
    random_str = get_strings(key)
    with open(RESULT_TXT, 'w') as f:
        f.write(random_str)


if __name__ == "__main__":
    main()
