#!/usr/bin/env python3
"""
Author : Tania Chakraborty (taniac101)
Date   : 2020-03-26
Purpose: Synthetic sequence creation
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create synthetic sequences',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-t','--seqtype',help='DNA or RNA',
                        metavar='str',
                        type=str,
                        default='DNA')
    parser.add_argument('-n','--numseqs:',
                        help='Number of sequences to create',
                        metavar='int',
                        type=int,
                        default=10)
    parser.add_argument('-m','--minlen',help='Minimum length',
                        metavar='int',
                        type=int,
                        default=50)
    parser.add_argument('-x','--maxlen',help='Maximum length',
                        metavar='int',
                        type=int,
                        default=75)
    parser.add_argument('-s','--seed',help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)
    parser.add_argument('-p','--pctgc',help='Percent GC',
                        metavar='float',
                        type=float,
                        default=0.5)
    parser.add_argument('-o','--outfile',help='Output filename',
                        metavar='str',
                        default='out.fa')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    str_arg = args.arg
    int_arg = args.int
    file_arg = args.file
    flag_arg = args.on
    pos_arg = args.positional

    print('str_arg = "{}"'.format(str_arg))
    print('int_arg = "{}"'.format(int_arg))
    print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))
    print('flag_arg = "{}"'.format(flag_arg))
    print('positional = "{}"'.format(pos_arg))


# --------------------------------------------------
if __name__ == '__main__':
    main()
