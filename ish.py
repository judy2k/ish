from __future__ import print_function

import sys
import string
import numbers
import functools
import unicodedata

STRIP_CHARS = string.whitespace + string.punctuation

BOOL_STRINGS = {}
BOOL_STRINGS.update(
    (s, True)
    for s in (
        "true",
        "yes",
        "on",
        "yeah",
        "yup",
        "yarp",
        "oui",  # French
        "ja",  # German, Danish, Dutch, Afrikaans, Swedish, Norwegian
        "sim",  # Portuguese
        "sea",  # Irish
        "jes",  # Esperanto
        u"\u0646\u0639\u0645".lower(),  # Arabic
        "igen",  # Hungarian
        "igaz",  # Hungarian
    )
)

BOOL_STRINGS.update(
    (s, False)
    for s in (
        "false",
        "no",
        "off",
        "nope",
        "nah",
        "narp",
        "non",  # French
        "nein",  # German
        "nej",  # Danish, Swedish
        "nee",  # Dutch
        "geen",  # Afrikaans
        "nei",  # Norwegian
        "não",  # Portugese
        "níl",  # Irish
        "ne",  # Esperanto
        u"\u0644\u0623".lower(),  # Arabic
        "nem",  # Hungarian
        "hamis",  # Hungarian
    )
)


class UnIshable(Exception):
    def __init__(self, value):
        super(UnIshable, self).__init__("{!r} can not be ished!".format(value))


class Maybe(ValueError):
    def __init__(self, value):
        super(Maybe, self).__init__("Maybe! ({!r} is not recognised)".format(value))


class BaseIsh:
    def __init__(self, value):
        self._value = value

    def __repr__(self):
        return "{!r}-{!r}".format(self._value, ish)


class BoolIsh(BaseIsh):
    def _check_string(self, s):
        try:
            return bool(int(s))
        except ValueError:
            pass
        try:
            return BOOL_STRINGS[
                unicodedata.normalize("NFKC", s).strip(STRIP_CHARS).lower()
            ]
        except KeyError:
            pass
        raise Maybe(s)

    def __eq__(self, other):
        result = bool(other)

        if result and isinstance(other, str):
            result = self._check_string(other)

        return result == self._value


@functools.total_ordering
class NumberIsh(BaseIsh):
    def __init__(self, value, precision=0.2):
        super(NumberIsh, self).__init__(value)

        self._min = min(value - precision, value * (1 - precision))
        self._max = max(value + precision, value * (1 + precision))

    def _to_number(self, obj):
        try:
            return float(obj)
        except (TypeError, ValueError):
            try:
                return int(obj)
            except (TypeError, ValueError):
                raise Maybe(obj)

    def __eq__(self, other):
        return self._min <= self._to_number(other) <= self._max

    def __lt__(self, other):
        return self._min < self._to_number(other)


class Ish:
    _module = sys.modules[__name__]

    UnIshable = UnIshable
    Maybe = Maybe

    def __rsub__(self, other):
        if isinstance(other, bool):
            return BoolIsh(other)
        if isinstance(other, numbers.Real):
            return NumberIsh(other)
        raise UnIshable(other)

    def __repr__(self):
        return "ish"


ish = ish.ish = sys.modules[__name__] = Ish()


if __name__ == "__main__":
    print("Yup" == True - ish)
    print("Nope" == True - ish)
    print("False" == False - ish)
    print("Yeah" == False - ish)
    print("Whatever" == True - ish)
