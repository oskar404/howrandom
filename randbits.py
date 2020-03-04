#!/usr/bin/env python3

from hotbits import RandomDataGenerator
from os import path


API_KEY_FILE = '.hotbits.apikey'
RESULT_FILE = 'randbits.bin'


def get_api_key(file):
    if path.isfile(file):
        with open(file) as f:
            return f.read().strip()
    return None


def main():
    key = get_api_key(API_KEY_FILE)
    if not key:
        print('Hotbits API Key not found. Fallback to pseudo random generator')
    generator = RandomDataGenerator()
    data = generator.generate(length='128', apikey=key)
    print(f"random: [{','.join(map(str, data))}]")
    print(f"storing to: {RESULT_FILE}")
    with open(RESULT_FILE, 'wb') as f:
        f.write(bytes(data))


if __name__ == "__main__":
    main()
