#!/usr/bin/env python3
"""
Author : Tania Chakraborty (taniac101)
Date   : 2020-02-05
Purpose: Spanish article
"""
from typing import Any

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Choose the correct Spanish article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text

    if text[-1] in 'oO':
        print(f"Me gusto el {text}.")
    elif text[-1] in 'aA':
        print(f'Me gusto la {text}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
