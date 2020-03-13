#!/usr/bin/env python3
"""
Author : Tania Chakraborty (taniac101)
Date   : 2020-02-27
Purpose: Codons to Amino Acids
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA to Amino Acids',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str', metavar='str', help='DNA/RNA sequence')
    parser.add_argument('-c',
                        '--codons',
                        help='A file with codon translations',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default=None)
    parser.add_argument('-o',
                        '--outfile',
                        help='A file with codon translations',
                        metavar='FILE',
                        type=argparse.FileType('w'),
                        default='out.txt')
    args = parser.parse_args()
    if not args.codons:
        parser.error("Codon File Not Provided")
    else:
        return parser.parse_args()


# --------------------------------------------------
def main():
    args = get_args()
    k = 3
    input_codons = [args.str.lower()[i:i + k]
                    for i in range(0, len(args.str.lower()), k)]
    codon_table = {line[0:3].lower(): line[4] for line in args.codons}
    for i in input_codons:
        aa = codon_table.get(i) if i in codon_table else '-'
        print('{}'.join(aa), end='', file=args.outfile)
    print(f'Output written to "{args.outfile.name}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
