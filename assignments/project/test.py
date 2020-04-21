#!/usr/bin/env python3
"""tests for n50.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput
from Bio import SeqIO
from Bio.SeqUtils import GC
from numpy import mean
from itertools import chain
from shutil import rmtree

prg = './n50.py'
file1 = './file1.fa'
file2 = './file2.fa'
file3 = './file3.fa'
file4 = './file4.fa'


# --------------------------------------------------
def random_string():
    """generate a random string"""

    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))


# --------------------------------------------------
def test_exists():
    """usage"""

    for file in [prg, file1, file2, file3, file4]:
        assert os.path.isfile(file)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(prg, flag))
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_file():
    """die on bad file"""

    bad = random_string()
    rv, out = getstatusoutput(f'{prg} {bad}')
    assert rv != 0
    assert re.match('usage:', out, re.I)
    assert re.search(f"No such file or directory: '{bad}'", out)
# --------------------------------------------------
def test_file1():
    """run on file 1 with default outfile"""
    out_file = 'n50.txt'
    in_file = 'file1.fa'
    try:
        if os.path.isfile(out_file):
            os.remove(out_file)

        rv, out = getstatusoutput(f' {prg} {in_file}')
        assert rv == 0
        assert out == f'Done, details are in "{out_file}".'
        assert os.path.isfile(out_file)

        # correct number of seqs
        seqs = list(SeqIO.parse(in_file, 'fasta'))
        assert len(seqs) == 456
    finally:
        if os.path.isfile(out_file):
            os.remove(out_file)

# --------------------------------------------------
def test_file2():
    """run on file 2 with default outfile"""
    out_file = 'n50.txt'
    in_file = 'file2.fa'
    try:
        if os.path.isfile(out_file):
            os.remove(out_file)

        rv, out = getstatusoutput(f' {prg} {in_file}')
        assert rv == 0
        assert out == f'Done, details are in "{out_file}".'
        assert os.path.isfile(out_file)

        # correct number of seqs
        seqs = list(SeqIO.parse(in_file, 'fasta'))
        assert len(seqs) == 1500
    finally:
        if os.path.isfile(out_file):
            os.remove(out_file)

# --------------------------------------------------
def test_file3():
    """run on file 1 with default outfile"""
    out_file = 'n50.txt'
    in_file = 'file3.fa'
    try:
        if os.path.isfile(out_file):
            os.remove(out_file)

        rv, out = getstatusoutput(f' {prg} {in_file}')
        assert rv == 0
        assert out == f'Done, details are in "{out_file}".'
        assert os.path.isfile(out_file)

        # correct number of seqs
        seqs = list(SeqIO.parse(in_file, 'fasta'))
        assert len(seqs) == 4563
    finally:
        if os.path.isfile(out_file):
            os.remove(out_file)

# --------------------------------------------------
def test_file4():
    """run on file 1 with default outfile"""
    out_file = 'n50.txt'
    in_file = 'file4.fa'
    try:
        if os.path.isfile(out_file):
            os.remove(out_file)

        rv, out = getstatusoutput(f' {prg} {in_file}')
        assert rv == 0
        assert out == f'Done, details are in "{out_file}".'
        assert os.path.isfile(out_file)

        # correct number of seqs
        seqs = list(SeqIO.parse(in_file, 'fasta'))
        assert len(seqs) == 9888
    finally:
        if os.path.isfile(out_file):
            os.remove(out_file)