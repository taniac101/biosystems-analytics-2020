#!/usr/bin/env python3
"""
Author : Tania Chakraborty (taniac101)
Date   : 2020-04-02
Purpose: Randomly subset a FASTA file
"""

import argparse
import os
import random
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Probabalistically subset FASTA files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('input_files',metavar='FILE',
                        help='Input FASTA file(s)',
                        type=argparse.FileType('r'),
                        nargs='+')
    parser.add_argument('-p','--pct',help='Percent of reads',
                        metavar='reads',
                        type=float,
                        default=0.1)
    parser.add_argument('-s','--seed',help='Random seed value',
                        metavar='seed',
                        type=int,
                        default=None)
    parser.add_argument('-o','--outdir',help='Output directory',
                        metavar='str',
                        default='out')
    args = parser.parse_args()
    if not 0 < args.pct < 1:
        parser.error(f'--pct "{args.pct}" must be between 0 and 1')
    if not os.path.isdir(args.outdir):
        os.makedirs(args.outdir)
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    random.seed(args.seed)
    num_seqs = 0
    for i, fh in enumerate(args.input_files, start=1):
        out_file = os.path.join(args.outdir, os.path.basename(fh.name))
        print(f'  {i}: {os.path.basename(fh.name)}')
        out_fh = open(out_file, 'wt')
        for rec in SeqIO.parse(fh, 'fasta'):
            if args.pct >= random.random():
                SeqIO.write(rec, out_fh, 'fasta')
                num_seqs += 1
        out_fh.close()
    file = "file" if i == 1 else "files"
    print(f'Wrote {num_seqs:,d} sequences '
          f'from {i} {file} to directory "{args.outdir}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
