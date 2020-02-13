#!/usr/bin/env python3
"""
Author : Tania Chakraborty (taniac101)
Date   : 2020-02-06
Purpose: List sorter
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Order all the things',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='str',
                        nargs='*',
                        help='The things to order')

    parser.add_argument('-r', '--reverse', nargs= '*', metavar = '', help= 'Reverse the sort order')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    if args.reverse is not None:
        for index, value in enumerate(sorted(args.item, reverse=True), start=1):
            print('{:3}: {}'.format(index, value))
    else:
        for index, value in enumerate(sorted(args.item), start=1):
            print('{:3}: {}'.format(index, value))


# --------------------------------------------------
if __name__ == '__main__':
    main()