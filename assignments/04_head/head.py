#!/usr/bin/env python3
"""
Author : Tania Chakraborty (taniac101)
Date   : 2020-02-20
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('FILE',
                        type=argparse.FileType('r'),
                        help='Input file',
                        metavar='FILE')
    parser.add_argument('-n',
                        '--num',
                        help='Number of lines',
                        metavar='int',
                        type=int,
                        default=10)
    args = parser.parse_args()
    if args.num <= 0:
        parser.error(f'--num "{args.num}" must be greater than 0')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()

    with args.FILE as fh:
        n_lines = fh.readlines()[0:args.num]
        print(''.join(n_lines))


# --------------------------------------------------
if __name__ == '__main__':
    main()
