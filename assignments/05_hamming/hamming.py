#!/usr/bin/env python3
"""
Author : Tania Chakraborty (taniac101)
Date   : 2020-02-29
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Calculate Hamming Distance between Words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('r'))

    parser.add_argument('-m',
                        '--min',
                        help='Minimum value of Hamming distance',
                        metavar='int',
                        type=int)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for line in args.input:
        column_a, column_b = line.rstrip().split()
        h_dist = sum(1 for a, b in zip(column_a, column_b)
                     if a != b) + abs(len(column_a) - len(column_b))
        if args.min:
            if h_dist >= args.min:
                print(f'{h_dist:8}:{column_a:20}{column_b:20}', end='\n')
        else:
            print(f'{h_dist:8}:{column_a:20}{column_b:20}', end='\n')



# --------------------------------------------------
if __name__ == '__main__':
    main()
