#!/usr/bin/env python3
"""
Author : Tania Chakraborty (taniac101)
Date   : 2020-04-26
Purpose: Parsing SwissProt records
"""

import argparse
import os
import sys
from Bio import SeqIO

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Filter SwissProt file for keywords, taxa',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        help='SwissProt file')
    parser.add_argument('-k',
                        '--keyword',
                        help='Keyword to take',
                        metavar='keyword',
                        type=str,
                        default=None,
                        required=True)
    parser.add_argument('-s',
                        '--skiptaxa',
                        help='Taxa to skip',
                        metavar='taxa',
                        type=str,
                        nargs='+',
                        default=' ')
    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.fa')

    return parser.parse_args()

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    counts_skipped, counts_taken = 0, 0
    skiptaxa = set(map(str.lower, args.skiptaxa))
    keywords = set(args.keyword.split('""'))
    for rec in SeqIO.parse(args.file, "swiss"):
        if "keywords" and "taxonomy" in rec.annotations.keys():
            taxa = set(map(str.lower,(rec.annotations.get('taxonomy'))))
            kword = set(map(str.lower, (rec.annotations.get('keywords'))))
            if skiptaxa.intersection(taxa):
                counts_skipped += 1
            elif keywords.intersection(kword):
                SeqIO.write(rec, args.outfile, 'fasta')
                counts_taken += 1
            else:
                counts_skipped += 1
    print(f'Done, skipped {counts_skipped} and took {counts_taken}. '
          f'See output in "{args.outfile.name}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
