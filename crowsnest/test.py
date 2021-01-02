#!use/bin/env python 3

import os
from subprocess import getoutput, getstatusoutput

consonents = [
    'brigantine', 'clipper', 'dreadnought', 'frigate', 'galleon', 'haddock',
    'junk', 'ketch', 'longboat', 'mullet', 'narwhal', 'porpoise', 'quay',
    'regatta', 'submarine', 'tanker', 'vessel', 'whale', 'xebec', 'yatch',
    'zebrafish'
]
vowels = ['aviso', 'eel', 'iceberg', 'octopus', 'upbound']
prg = './crownest.py'

template = "Ahoy Captain! {} {} off the larboard bow."


def test_exists():
    '''check if exist'''

    assert os.path.isfile(prg)


"""
def test_runnable():
    '''check if runnable through interpretor'''

    output = getoutput(f'python {prg} name')
    assert output.strip().startswith("Ahoy Captain!")
"""


def test_usage():
    '''check if usable'''

    for flag in ['-h', '--help']:
        rv, output = getstatusoutput(f'python {prg} {flag}')

        assert rv == 0
        assert output.startswith("usage")


def test_vowels():
    '''test for vowels'''

    for vowel in vowels:
        output = getoutput(f'python {prg} -i {vowel}')
        assert output.strip() == template.format('an', vowel)


def test_vowels_capital():
    '''test for capital vowels'''

    for vowel in vowels:
        output = getoutput(f'python {prg} -i {vowel.capitalize()}')
        assert output.strip() == template.format('an', vowel.capitalize())


def test_consonents():
    '''test for vowels'''

    for const in consonents:
        output = getoutput(f'python {prg} -i {const}')
        assert output.strip() == template.format('a', const)


def test_consonents_capital():
    '''test for capital vowels'''

    for const in consonents:
        output = getoutput(f'python {prg} -i {const.capitalize()}')
        assert output.strip() == template.format('a', const.capitalize())
