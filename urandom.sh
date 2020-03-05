#!/usr/bin/env bash
# Generate random data from /dev/urandom

head -c 128 </dev/urandom > urandom.bin
tr -dc A-Z < /dev/urandom | head -c 128 > urandom.txt