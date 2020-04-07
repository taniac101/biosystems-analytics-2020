#!/usr/bin/env python3
"""
Author : taniac
Date   : 2020-04-06
Purpose: Rock the Casbah
"""

import argparse
import os
import sys
from itertools import groupby

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
    sequences = args.input_files()
    seq_lengths = get_seq_lengths(sequences)
    n50 = calc_n50(seq_lengths)
    print('N50: %s kb' % (n50 / 1000))
    print('Size: %s' % (sum(chrom_lengths)))

# --------------------------------------------------
def get_seq_length(sequences):
    seq_lengths = []
    with open(genome_fasta, 'r') as input_handle:
        fasta_reader = (x[1] for x in groupby(input_handle, lambda line: line.startswith('>')))
        for header in fasta_reader:
            next(header).strip('>').rstrip('\n')
            length = len(''.join(s.strip() for s in next(fasta_reader)))
            seq_lengths.append(length)
        return seq_lengths

# --------------------------------------------------
def calc_n50(seq_lengths):
    half_size = sum(seq_lengths) / 2
    total_seq_lengths = 0
    for seq_length in sorted(seq_lengths, reverse=True):
        total_seq_lengths += seq_length
        if total_seq_lengths >= half_size:
            return seq_length

# --------------------------------------------------
if __name__ == '__main__':
    main()
