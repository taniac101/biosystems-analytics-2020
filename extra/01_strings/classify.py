#!/usr/bin/env python3
"""
Author : Tania Chakraborty (taniac101)
Date   : 2020-02-04
Purpose: Classify the input
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Classify a given string',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Some text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text

    if text.isupper():
        print(f'{text} is uppercase.')
    elif text.islower():
        print(f'{text} is lowercase.')
    elif text.istitle():
        print(f'{text} is title case.')
    elif text.isdigit():
        print(f'{text} is a digit.')
    elif text.isspace():
        print("input is space.")
    else:
        print(f'{text} is unclassified.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
