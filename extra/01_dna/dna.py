#!/usr/bin/env python3
"""
Author : Tania Chakraborty (taniac101)
Date   : 2020-02-04
Purpose: Count frequency of individual nucleotide in string
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Count DNA nucleotides',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('DNA',
                        metavar='str',
                        help='A positional argument')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    dna = args.DNA.lower()

    count_a = dna.count("a")
    count_c = dna.count("c")
    count_g = dna.count("g")
    count_t = dna.count("t")

    all_counts = [count_a, count_c, count_g, count_t]
    print(' '.join(map(str, all_counts)))


# --------------------------------------------------
if __name__ == '__main__':
    main()
