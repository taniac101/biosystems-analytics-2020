#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2020-02-17
Purpose: Rock the Casbah
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        help='Input file')

    parser.add_argument('-n',
                        '--num',
                        help='Number of lines',
                        metavar='int',
                        type=int,
                        default=10)

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for i, line in enumerate(args.file, start=1):
        print(line, end='')
        if i == args.num:
            break


# --------------------------------------------------
if __name__ == '__main__':
    main()
