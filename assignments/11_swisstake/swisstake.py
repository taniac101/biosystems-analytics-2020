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
from operator import itemgetter


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Filter SwissProt file for keywords, taxa',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        help='SwissProt file',
                        type=argparse.FileType('r'))
    parser.add_argument('-k',
                        '--keyword',
                        help='Keyword to take',
                        metavar='keyword',
                        type=str,
                        nargs='*',
                        default=None,
                        required=True)
    parser.add_argument('-s',
                        '--skiptaxa',
                        help='Taxa to skip',
                        metavar='taxa',
                        type=str,
                        nargs='*',
                        default=None)
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
    t, k = set(), set()
    skiptaxa = set(map(str.lower, args.skiptaxa))
    keywords = set(map(str.lower, args.keyword))
    for rec in SeqIO.parse(args.file, "swiss"):
        taxa = set(map(str.lower,(rec.annotations.get('taxonomy'))))
        t.update(taxa)
        skip = set(map(str.lower, (rec.annotations.get('keywords'))))
        k.update(skip)
    taken = keywords.intersection(k)
    skipped = t - skiptaxa.intersection(t)
    print(f'Done, skipped {len(skipped)} and taken {len(taken)}.'
          f' See output in {args.outfile.name}.')
# --------------------------------------------------
if __name__ == '__main__':
    main()
