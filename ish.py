from __future__ import print_function

import sys
import string
import numbers
import functools
import unicodedata

try:
    from deep_neural_network.face_classifier import detect_and_predict_face_emotion
except ImportError:
    detect_and_predict_face_emotion = None

try:
    basestring
except NameError:
    basestring = (str, bytes)

ENCODINGS = (
    # Unicode with BOM
    'utf-8-sig', 'utf-32', 'utf-16',
    # Unicode without BOM
    'utf-8', 'utf-32le', 'utf-32be', 'utf-16le', 'utf-16be',
    # Arabic
    'iso-8859-6', 'cp720', 'cp1256',
)

STRIP_CHARS = string.whitespace + string.punctuation

BOOL_STRINGS = {}
BOOL_STRINGS.update((s, True) for s in (
    'true', 'yes', 'on', 'yeah', 'yup', 'yarp',
    'oui',  # French
    'ja',   # German, Danish, Dutch, Afrikaans, Swedish, Norwegian
    'sim',  # Portuguese
    'sea',  # Irish
    'jes',  # Esperanto
    u'\u0646\u0639\u0645', # Arabic
))
BOOL_STRINGS.update((s, False) for s in (
    'false', 'no', 'off', 'nope', 'nah', 'narp',
    'non',   # French
    'nein',  # German
    'nej',   # Danish
    'nee',   # Dutch
    u'\u0644\u0623', # Arabic
))

EMOTIONAL_STRINGS = {
    'happy':      3,
    'happy-face': 3,
    'joyful':     3,

    'angry':      0,
    'anger':      0,
    'grrr':       0,

    'sad':        4,
    'depressed':  4,
    'emo':        4,

    'surprise':   5,
    'shock':      5,
    'omg':        5,
    'omfg':       5,
    'amazeballs': 5,

    'neutral':    6,
}


class UnIshable(Exception):
    def __init__(self, value):
        super(UnIshable, self).__init__('{!r} can not be ished!'.format(value))


class Maybe(ValueError):
    def __init__(self, value):
        super(Maybe, self).__init__('Maybe! ({!r} is not recognised)'.format(value))


def lookup_decoded_string(s, mapping):
    return mapping[unicodedata.normalize('NFKC', s).strip(STRIP_CHARS).lower()]

def lookup_encoded_string(s, mapping):
    for encoding in ENCODINGS:
        try:
            return lookup_decoded_string(s.decode(encoding), mapping)
        except (UnicodeDecodeError, KeyError):
            pass
    raise KeyError(s)

def lookup_string(s, mapping):
    if isinstance(s, bytes):
        return lookup_encoded_string(s, mapping)
    return lookup_decoded_string(s, mapping)


class BaseIsh(object):
    def __init__(self, value):
        self._value = value

    def __repr__(self):
        return '{!r}-{!r}'.format(self._value, ish)


class BoolIsh(BaseIsh):
    def _check_string(self, s):
        try:
            return bool(int(s))
        except ValueError:
            try:
                return lookup_string(s, BOOL_STRINGS)
            except KeyError:
                raise Maybe(s)

    def __eq__(self, other):
        result = bool(other)

        if result and isinstance(other, basestring):
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


class EmotionIsh(BaseIsh):
    def __init__(self, value):
        if detect_and_predict_face_emotion:
            super(EmotionIsh, self).__init__(value)
            try:
                self._type = lookup_string(value, EMOTIONAL_STRINGS)
            except KeyError:
                raise UnIshable(value)
        else:
            raise UnIshable(value)

    def _is_image(self, img):
        try:
            shape = img.shape
            if len(shape) == 3 and shape[2] == 3:
                return True
            if len(shape) == 2:
                return True
        except Exception:
            return False

    def __eq__(self, other):
        if self._is_image(other):
            return detect_and_predict_face_emotion(other) == self._type
        raise Maybe(other)


class Ish(object):
    _module = sys.modules[__name__]

    UnIshable = UnIshable
    Maybe = Maybe

    def __rsub__(self, other):
        if isinstance(other, bool):
            return BoolIsh(other)
        if isinstance(other, numbers.Real):
            return NumberIsh(other)
        if isinstance(other, basestring):
            return EmotionIsh(other)
        raise UnIshable(other)

    def __repr__(self):
        return 'ish'


ish = ish.ish = sys.modules[__name__] = Ish()


if __name__ == '__main__':
    print('Yup' == True-ish)
    print('Nope' == True-ish)
    print('False' == False-ish)
    print('Yeah' == False-ish)
    print('Whatever' == True-ish)
