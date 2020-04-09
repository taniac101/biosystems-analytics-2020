#!/usr/bin/env python3
"""
Author : Tania Chakraborty (taniac101)
Date   : 2020-04-09
Purpose: Find Unclustered Proteins
"""

import argparse
import os
import sys
from itertools import groupby
from Bio import SeqIO
import re

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find proteins not clustered by CD-HIT',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-c', '--cdhit', metavar='cdhit',
                        help='Output file from CD-HIT (clustered proteins)',
                        type=argparse.FileType('r'),
                        default=None,
                        required=True)
    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='outfile',
                        type=argparse.FileType('w'),
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
    for line in args.cdhit:
        cluster_reader = (x[1] for x in groupby(line, lambda line: line.startswith('>')))
    print(cluster_reader)

# --------------------------------------------------
if __name__ == '__main__':
    main()
