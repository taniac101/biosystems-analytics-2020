#!/usr/bin/env python3
"""
Author : Tania Chakraborty (taniac101)
Date   : 2020-05-04
Purpose: CSV Filter
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Filter delimited records',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-c',
                        '--col',
                        help='Column for filter',
                        metavar='col',
                        type=str,
                        default=None)
    parser.add_argument('-d',
                        '--delimiter',
                        help='Input delimiter',
                        metavar='delim',
                        default=',')
    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default=None,
                        required=True)
    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='OUTFILE',
                        type=argparse.FileType('wt'),
                        default='out.csv')
    parser.add_argument('-v',
                        '--val',
                        help='Value for filter',
                        metavar='val',
                        default=None)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print(args)


# --------------------------------------------------
if __name__ == '__main__':
    main()
