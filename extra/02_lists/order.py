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
                        nargs='+',
                        help='The things to order (default: None)')

    parser.add_argument('-r',
                        '--reverse',
                        nargs='+',
                        help='Reverse the sort order')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    if len(sys.argv) == 1:
        sys.exit('You have failed me for the last time, Commander.')

    args = get_args()
    items = args.item
    a = sorted(items)
    b = reversed(items)

    for index, value in enumerate(a, start=1):
        print('  {}: {}'.format(index, value))

    if args.reverse:
        for index, value in enumerate(b, start=1):
            print('{}: {}'.format(index, value))

    """if args.reverse == True:
        revlist = reversed(items)
        for i in range(len(revlist)):
            print('{}: {}'.format(i+1, revlist[i]))
    else:
        list = sorted(items)
        for i in range(len(list)):
            print('{}: {}'.format(i + 1, list[i]).join('\n', list))"""


# --------------------------------------------------
if __name__ == '__main__':
    main()