#!/usr/bin/env python3

from hotbits import RandomDataGenerator
from os import path


API_KEY_FILE = '.hotbits.apikey'
RESULT_BIN = 'hotbits.bin'
RESULT_TXT = 'hotbits.txt'


def get_api_key(file):
    if path.isfile(file):
        with open(file) as f:
            return f.read().strip()
    return None


def get_bytes(key):
    generator = RandomDataGenerator()
    data = generator.generate(length='128', apikey=key)
    print(f"random: [{','.join(map(str, data))}]")
    return bytes(data)


def get_strings(key):
    def get_char(indata):
        return chr(ord('A') + indata % (ord('Z') - ord('A') + 1))
    generator = RandomDataGenerator()
    raw_data = generator.generate(length='128', apikey=key)
    data = ''.join([get_char(x) for x in raw_data])
    print(f"random: {data}")
    return data


def main():
    key = get_api_key(API_KEY_FILE)
    if not key:
        print('Hotbits API Key not found. Fallback to pseudo random generator')
    random_bytes = get_bytes(key)
    with open(RESULT_BIN, 'wb') as f:
        f.write(random_bytes)
    random_str = get_strings(key)
    with open(RESULT_TXT, 'w') as f:
        f.write(random_str)


if __name__ == "__main__":
    main()
