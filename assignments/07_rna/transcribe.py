#!/usr/bin/env python3
"""
Author : Tania Chakraborty (taniac101)
Date   : 2020-03-19
Purpose: Transcribe DNA to RNA
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Transcribing DNA into RNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('file',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('r'),
                        help='Input file(s)')
    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='DIR',
                        default="out")
    args = parser.parse_args()
    if not os.path.isdir(args.outdir):
        os.makedirs(args.outdir)
    return parser.parse_args()


# --------------------------------------------------
def main():
    args = get_args()
    out_dir, sequences, files = args.outdir, 0, len(args.file)
    for fh in args.file:
        out_file = os.path.join(out_dir, os.path.basename(fh.name))
        out_fh = open(out_file, 'wt')
        for line in fh:
            sequences += len(line.split())
            rna = line.replace('T', 'U')
            print(rna, file=out_fh, end='')
        if sequences > 1 and files == 1:
            print(f'Done, wrote {sequences} sequences'
                  f' in {files} file to directory "{out_dir}".')
        elif sequences == 1 and files == 1:
            print(f'Done, wrote {sequences} sequence'
                  f' in {files} file to directory "{out_dir}".')
        elif sequences > 1 and files > 1:
            print(f'Done, wrote {sequences} sequences'
                  f' in {files} files to directory "{out_dir}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
