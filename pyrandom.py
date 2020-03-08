#!/usr/bin/env python3
"""Use Python random library for generating data"""
import random


RESULT_BIN = 'pyrandom.bin'
RESULT_TXT = 'pyrandom.txt'


def get_bytes():
    random.seed(a=1, version=2)
    data = random.getrandbits(128*8).to_bytes(length=128, byteorder='big')
    print(f"random: [{data}]")
    return data


def get_strings():
    random.seed(a=1, version=2)
    raw_data = []
    for _ in range(128):
        raw_data.append(random.randrange(ord('A'), ord('Z')))
    data = ''.join([chr(x) for x in raw_data])
    print(f"random: {data}")
    return data


def main():
    random_bytes = get_bytes()
    with open(RESULT_BIN, 'wb') as f:
        f.write(random_bytes)
    random_str = get_strings()
    with open(RESULT_TXT, 'w') as f:
        f.write(random_str)


if __name__ == "__main__":
    main()
