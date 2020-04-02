#!/usr/bin/env python3
"""
Author : TaniaChakraborty(taniac101)
Date   : 2020-03-26
Purpose: Synthetic sequence creation
"""

import argparse
import random

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create synthetic sequences',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-t',
                        '--seqtype',
                        help='DNA or RNA',
                        metavar='str',
                        type=str,
                        default='dna',
                        choices=['dna','rna'])
    parser.add_argument('-n',
                        '--numseqs',
                        help='Number of sequences to create',
                        metavar='int',
                        type=int,
                        default=10)
    parser.add_argument('-m',
                        '--minlen',
                        help='Minimum length',
                        metavar='int',
                        type=int,
                        default=50)
    parser.add_argument('-x',
                        '--maxlen',
                        help='Maximum length',
                        metavar='int',
                        type=int,
                        default=75)
    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)
    parser.add_argument('-p',
                        '--pctgc',
                        help='Percent GC',
                        metavar='float',
                        type=float,
                        default=0.5)
    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=argparse.FileType('wt'),
                        default='out.fa')
    args = parser.parse_args()
    if not 0 < args.pctgc < 1:
        parser.error(f'--pctgc "{args.pctgc}" must be between 0 and 1')
    return parser.parse_args()

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    seqtype = args.seqtype
    pctgc = args.pctgc
    maxlen = args.maxlen
    random.seed(args.seed)
    pool = create_pool(pctgc, maxlen, seqtype)
    for i in range(0, args.numseqs):
        seq_len = random.randint(args.minlen, maxlen)
        seq = ''.join(random.sample(pool, seq_len))
        num_seq = i + 1
        print(f'>{num_seq}\n{seq}', file=args.outfile)
    print(f'Done, wrote {num_seq} {seqtype.upper()}'
          f' sequences to "{args.outfile.name}".')
# --------------------------------------------------

def create_pool(pctgc, maxlen, seqtype):
    """ Create the pool of bases """
    t_or_u = 'T' if seqtype == 'dna' else 'U'
    num_gc = int((pctgc / 2) * maxlen)
    num_at = int(((1 - pctgc) / 2) * maxlen)
    pool = 'A' * num_at + 'C' * num_gc + 'G' * num_gc + t_or_u * num_at
    for _ in range(maxlen - len(pool)):
        pool += random.choice(pool)
    return ''.join(sorted(pool))

# --------------------------------------------------
if __name__ == '__main__':
    main()
