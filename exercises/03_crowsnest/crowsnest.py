#!/usr/bin/env python3
"""
Author : root
Date   : 2020-02-04
Purpose: Rock the Casbah
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word', metavar='str', help='A word')

    return parser.parse_args()

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word

    article = ''
    if word [0] in 'aeiouAEIOU':
        article = 'an'
    else:
        article = 'a'

    print(f'Ahoy, Captain, {article} {word} off the larboard bow!')




# --------------------------------------------------
if __name__ == '__main__':
    main()
