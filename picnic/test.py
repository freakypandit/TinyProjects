import os
from subprocess import getoutput, getstatusoutput

prg = "./picnic.py"


def test_exists():
    '''file exists'''

    assert os.path.isfile(prg)


def test_usage():
    '''check if usable'''

    for flag in ['-h', '--help']:
        rv, output = getstatusoutput(f'python {prg} {flag}')

        assert rv == 0
        assert output.startswith("usage")


def test_one_word():
    '''test single word'''

    word = "sandwich"

    output = getoutput(f'python {prg} {word}')
    assert output.strip() == f"You are bringing {word}."


def test_two_word():
    '''test two word'''

    words = ["sandwich", "cake"]
    output = getoutput(f'python {prg} {words[0]} {words[1]}')
    assert output.strip() == "You are bringing sandwich and cake."


def test_more_words():
    '''more than two words'''
    words = ["sandwich", "cake", "waffles", "muffins"]

    args_str = ""
    for word in words:
        args_str += word + " "

    output = getoutput(f'python {prg} {args_str}')
    assert output.strip(
    ) == "You are bringing sandwich, cake, waffles, and muffins."


def test_sorted_two():
    '''sorted two'''
    output = getoutput(f'python {prg} -s soda candy')
    assert output.strip() == "You are bringing candy and soda."


def test_sorted_more():
    '''sorted more'''
    words = ["sandwich", "cake", "waffles", "muffins"]

    args_str = ""
    for word in words:
        args_str += word + " "

    output = getoutput(f'python {prg} {args_str} -s')
    assert output.strip(
    ) == "You are bringing cake, muffins, sandwich, and waffles."
