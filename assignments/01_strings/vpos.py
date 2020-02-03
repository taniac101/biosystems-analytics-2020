#!/usr/bin/env python3
"""
Author : Tania Chakraborty (taniac101)
Date   : 2020-01-30
Purpose: First Assignment_Vowel Position
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find position of vowel in string',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('vowel', metavar='vowel', help='A vowel to look for')
    parser.add_argument('text', metavar='text', help='The text to search')

    args = parser.parse_args()
    if args.vowel not in "aeiouAEIOU":
        parser.error(
            f"argument vowel: invalid choice: '{args.vowel}'"
            f"(choose from 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')")
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    vowel = args.vowel

    for i in range(len(text)):
        if text[i] is vowel:
            print(f'Found "{vowel}" in "{text}" at index {i}.')

    if vowel not in text:
        print(f'"{vowel}" is not found in "{text}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
