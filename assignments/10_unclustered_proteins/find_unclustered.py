#!/usr/bin/env python3
"""
Author : Tania Chakraborty (taniac101)
Date   : 2020-04-09
Purpose: Find Unclustered Proteins
"""

import argparse
import re
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find proteins not clustered by CD-HIT',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-c',
                        '--cdhit',
                        metavar='cdhit',
                        help='Output file from CD-HIT (clustered proteins)',
                        type=argparse.FileType('r'),
                        default=None,
                        required=True)
    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='outfile',
                        type=argparse.FileType('wt'),
                        default='unclustered.fa')
    parser.add_argument('-p',
                        '--proteins',
                        help='Proteins FASTA',
                        metavar='proteins',
                        type=argparse.FileType('r'),
                        default=None,
                        required=True)
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    protein_ids = set()
    num_ids_written, num_total_unclustered = 0, 0
    for line in args.cdhit:
        if not line.startswith('>'):
            cd_id = re.search(r'>(\d+)', line).group()
            protein_ids.add(cd_id)
    for rec in SeqIO.parse(args.proteins, 'fasta'):
        prot_ids = '>' + re.sub(r'\|.*', '', rec.id)
        num_total_unclustered += 1
        if prot_ids not in protein_ids:
            print(f'>{prot_ids}', file=args.outfile)
            num_ids_written += 1
    print(f'Wrote {num_ids_written} of {num_total_unclustered:,d} '
          f'unclustered proteins to "{args.outfile.name}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
