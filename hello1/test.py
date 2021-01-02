#!/usr/bin/env python3
''' Tests for hello.py'''

import os
from subprocess import getstatusoutput, getoutput

prg = "./hello.py"


def test_exists():
    '''exists'''

    assert os.path.isfile(prg)


def test_runnable():
    '''is runnable'''

    output = getoutput(f'python {prg}')
    assert output.strip() == "Hello World"


"""
def test_executable():
    '''is executable'''

    output = getoutput(prg)
    assert output.strip() == "Hello World!"
"""


def test_usage():
    '''test_usage'''

    for flag in ['-h', '--help']:
        rv, output = getstatusoutput(f'python {prg} {flag}')

        assert rv == 0
        assert output.lower().startswith("usage")


def test_input():
    '''test input'''

    for names in ['universe', 'multiverse']:
        for flag in '-n', '--name':

            output = getoutput(f'python {prg} {flag} {names}')
            assert output.strip() == f"Hello {names}"
