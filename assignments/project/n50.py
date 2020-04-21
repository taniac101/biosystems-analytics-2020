#!/usr/bin/env python3
"""
Author : Tania Chakraborty (taniac101)
Date   : 2020-04-06
Purpose: Project- N50 of some sequences from a fasta file
"""

import argparse
from itertools import groupby
import numpy
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Calculate N50 score of sequences',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input_file',
                        metavar='FILE',
                        help='Input FASTA file(s)',
                        type=argparse.FileType('rt'))
    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='n50.txt')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    contig_lengths = []
    sequences = (x[1] for x in groupby(args.input_file, lambda line: line.startswith('>')))
    for line in sequences:
        next(line).strip('>').rstrip('\n')
        sequence_length = len(''.join(s.strip() for s in next(sequences)))
        contig_lengths.append(sequence_length)
    all_contig_lengths = sorted(contig_lengths, reverse=True)
    half_of_total_length = int(sum(contig_lengths) / 2)
    total_length_rev_order = numpy.cumsum(all_contig_lengths)
    min_value = min(total_length_rev_order[total_length_rev_order >= half_of_total_length])
    index_at_min_value = numpy.where(total_length_rev_order == min_value)
    n50 = all_contig_lengths[int(index_at_min_value[0])]
    print(f'Filename: {args.input_file.name}\nTotal Size = {sum(all_contig_lengths):,d}\n'
          f'Total Contigs = {len(contig_lengths)}\nN50 Score: {n50:,d}', file=args.outfile)
    print(f'Done, details are in "{args.outfile.name}". The N50 Score is {n50:,d}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
