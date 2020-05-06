#!/usr/bin/env python3
"""
Author : Tania Chakraborty (taniac101)
Date   : 2020-05-04
Purpose: CSV Filter
"""

import argparse
import os
import sys
import csvchk
import csv
from pprint import pprint
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Filter delimited records',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-c',
                        '--col',
                        help='Column for filter',
                        metavar='col',
                        default=None)
    parser.add_argument('-d',
                        '--delimiter',
                        help='Input delimiter',
                        metavar='delim',
                        type=str,
                        default=',')
    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default=None,
                        required=True)
    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='OUTFILE',
                        type=argparse.FileType('wt'),
                        default='out.csv')
    parser.add_argument('-v',
                        '--val',
                        help='Value for filter',
                        metavar='val',
                        default=None,
                        required=True)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    num_written = 0
    reader = csv.DictReader(args.file, delimiter=args.delimiter)
    writer = csv.DictWriter(args.outfile, fieldnames=reader.fieldnames, delimiter=',')
    writer.writeheader()
    col_names = ', '.join(reader.fieldnames)
    if args.col is not None:
        if args.col not in reader.fieldnames:
            sys.exit(f'--col "{args.col}" not a valid column!\nChoose from {col_names}')
        else:
            for rec in reader:
                for key, value in rec.items():
                    if args.col.lower() in key:
                        if re.search(args.val, value, re.IGNORECASE):
                            num_written += 1
                            writer.writerow(rec)
    else:
        for rec in reader:
            if re.search(args.val, str(rec), re.IGNORECASE):
                num_written += 1
                writer.writerow(rec)

    print(f'Done, wrote {num_written} to "{args.outfile.name}".')

# --------------------------------------------------
if __name__ == '__main__':
    main()
