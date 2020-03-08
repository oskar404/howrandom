#!/usr/bin/env python3
"""Implement Middle Square algorithm to generate data

For more information: https://en.wikipedia.org/wiki/Middle-square_method

NB! The algorithm is sensitive to seed and randomness is not high
"""


RESULT_BIN = 'middlesquare.bin'
RESULT_TXT = 'middlesquare.txt'


def get_bytes():
    """Generate bytes i.e. numbers between 0 and 255"""
    seed = 4242
    number = seed
    data = []
    for _ in range(128):
        # zfill adds padding of zeroes
        number = int(str(number * number).zfill(8)[2:6])
        data.append(number % 256)
    print(f"random: {data}")
    return bytes(data)


def get_strings():
    """Generate bytes i.e. numbers between 0 and 255"""
    seed = 6868
    number = seed
    raw_data = []
    for _ in range(128):
        # zfill adds padding of zeroes
        number = int(str(number * number).zfill(8)[2:6])
        raw_data.append(ord('A') + number % (ord('Z') - ord('A') + 1))
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
