#!/usr/bin/env python3
"""
Author : Tania Chakraborty (taniac101)
Date   : 2020-04-06
Purpose: Project- N50 of some sequences from a fasta file
"""

import argparse
import os
import sys
from itertools import groupby
from Bio import SeqIO

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Calculate N50 score of sequences',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input_files',metavar='FILE',
                        help='Input FASTA file(s)',
                        type=argparse.FileType('r'),
                        nargs='+')
    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('w'),
                        default='n50.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    seq_lengths = []
    for fh in args.input_files:
        sequence_reader = (x[1] for x in groupby(fh, lambda line: line.startswith('>')))
        for header in sequence_reader:
            next(header).strip('>').rstrip('\n')
            length = len(''.join(s.strip() for s in next(sequence_reader)))
            seq_lengths.append(length)
    half_length = sum(seq_lengths) / 2
    total_sequence_lengths = 0
    for i in sorted(seq_lengths, reverse=True):
        total_sequence_lengths += i
        if total_sequence_lengths >= half_length:
            n50 = i
    #print(f'File: {args.input_files}{n50}')
    print(sorted(seq_lengths, reverse = True),half_length,total_sequence_lengths,n50)


# --------------------------------------------------
if __name__ == '__main__':
    main()
