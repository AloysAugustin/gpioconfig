#!/usr/bin/env python

# Author: Aloys

import gpioconfig as gc
import sys, os


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: sudo python example.py pair_num success_command [failure_command]")
        sys.exit(0)

    pair = int(sys.argv[1])

    if gc.get_status(pair):
        os.system(sys.argv[2])
    elif len(sys.argv) > 3:
        os.system(sys.argv[3])


