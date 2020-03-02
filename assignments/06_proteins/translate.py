#!/usr/bin/env python3
"""
Author : Tania Chakraborty (taniac101)
Date   : 2020-02-27
Purpose: Codons to Amino Acids
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA to Amino Acids',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        help='DNA/RNA sequence')
    parser.add_argument('-c',
                        '--codons',
                        help='A file with codon translations',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default=None)
    parser.add_argument('-o',
                        '--outfile',
                        help='A file with codon translations',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.txt')
    args = parser.parse_args()
    if not args.codons:
        parser.error()
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    input_sequence  = args.str.lower()
    k = 3
    input_codons= [input_sequence[i:i + k] for i in range(0, len(input_sequence), k)]
    codon_table = {}
    for line in args.codons:
        (key, value) = line.split()
        codon_table[(key.lower())] = value
    for i in input_codons:
        aa = codon_table.get(i) if i in codon_table else '-'
        print('{}'.join(aa), end = '', file = args.outfile)
    print(f'Output written to "{args.outfile.name}".')




# --------------------------------------------------
if __name__ == '__main__':
    main()