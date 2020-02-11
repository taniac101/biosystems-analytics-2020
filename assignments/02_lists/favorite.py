#!/usr/bin/env python3
"""
Author : Tania Chakraborty (taniac101)
Date   : 2020-02-06
Purpose: Second homework - favorite things
"""
from typing import Any

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='My Favorite Things',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='str',
                        nargs='+',
                        help='Some things')

    parser.add_argument('-s',
                        '--sep',
                        help='A separator',
                        default=',')

    return parser.parse_args()


# -------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.items
    sep = args.sep
    fav = ''

    if len(items) == 1:
        print("{}\nThis is one of my favorite things.".format(items[0]))
    elif len(items) == 2 and sep is ',':
        print("{}\nThese are a few of my favorite things.".format(', ' .join(items)))
    elif len(items) == 2 and sep is not ',':
        fav = sep.join(items)
        print("{}\nThese are a few of my favorite things.".format(fav))
    elif len(items) > 2 and sep is ',':
        print("{}\nThese are a few of my favorite things.".format(', ' .join(items)))
    else:
        fav = sep.join(items)
        print("{}\nThese are a few of my favorite things.".format(fav))


# --------------------------------------------------
if __name__ == '__main__':
    main()
