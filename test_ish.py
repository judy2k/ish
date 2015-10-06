import pytest
from decimal import Decimal
from fractions import Fraction

import ish
from ish import ish as ish_  # backwards compatibility
from ish import UnIshable


def test_true_ish():
    assert 'Yeah' == True-ish
    assert 'yup' == True-ish
    assert 'Yarp' == True-ish
    assert 'Yeah' == True-ish_
    assert 'yup' == True-ish_


def test_true_ish_unicode():
    assert u'\ufee6\ufecc\ufee3' == True-ish


def test_charset_detection():
    # UTF-8
    assert b'\xef\xbb\xa6\xef\xbb\x8c\xef\xbb\xa3' == True-ish
    # UTF-16
    assert b'\xff\xfe\xe6\xfe\xcc\xfe\xe3\xfe' == True-ish
    # UTF-32
    assert b'\xff\xfe\x00\x00\xe6\xfe\x00\x00\xcc\xfe\x00\x00\xe3\xfe\x00\x00' == True-ish
    # ISO-8859-6
    assert b'\xe6\xd9\xe5' == True-ish
    # CP720
    assert b'\xeb\xe3\xea' == True-ish
    # CP1256
    assert b'\xe4\xda\xe3' == True-ish


def test_extra_chars():
    assert ' Yeah!!!' == True-ish


def test_false_ish():
    assert 'Nope' == False-ish
    assert 'Narp' == False-ish
    assert 'Nah' == False-ish
    assert '' == False-ish


def test_number_ish():
    assert 0.2 == 0-ish
    assert 0.6 > 0-ish
    assert '0.2' == 0-ish
    assert 0.4 == 0.5-ish
    assert 120 == 100-ish
    assert Decimal('1.2') == 1-ish
    assert Fraction('6/5') == 1-ish


def test_maybe():
    with pytest.raises(ValueError):
        'Whatever' == True-ish


def test_error():
    with pytest.raises(UnIshable):
        None == 'flibble'-ish
