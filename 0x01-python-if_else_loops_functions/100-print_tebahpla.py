#!/usr/bin/env python3

def print_tebahpla():
    for i in range(ord('z'), ord('A') - 1, -1):
        print(chr(i) if i % 2 == 0 else chr(i).upper(), end='')

print_tebahpla()

