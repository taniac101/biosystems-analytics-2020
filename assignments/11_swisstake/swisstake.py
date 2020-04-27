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
                        type=argparse.FileType('rt'))
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
                        type=argparse.FileType('at'),
                        default='out.fa')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    skiptaxa = set(map(str.lower, args.skiptaxa))
    keywords = (set(map(str.lower, args.keyword)))
    print(skiptaxa, keywords)
    num_skipped, num_taken = 0, 0
    for rec in SeqIO.parse(args.file, "swiss"):
        if "keywords" and "taxonomy" in rec.annotations.keys():
            taxa = set(map(str.lower,(rec.annotations.get('taxonomy'))))
            kword = set(map(str.lower,(rec.annotations.get('keywords'))))
            print(taxa,kword)
            break
    taken = keywords.intersection(kword)
    skip = skiptaxa.intersection(taxa)
    print(taken,skip)
    #for i in taken:
        #SeqIO.write(i, args.outfile, 'fasta')
    #print(skipped)


# --------------------------------------------------
if __name__ == '__main__':
    main()
