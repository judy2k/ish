# Ish

[![Build Status](https://travis-ci.org/judy2k/ish.svg?branch=master)](https://travis-ci.org/judy2k/ish)
[![Coverage Status](https://coveralls.io/repos/judy2k/ish/badge.svg?branch=master&service=github)](https://coveralls.io/github/judy2k/ish?branch=master)
[![Code Health](https://landscape.io/github/judy2k/ish/master/landscape.svg?style=flat)](https://landscape.io/github/judy2k/ish/master)

Ish is a stupid library that allows you to test if a variable is `true-ish` or
`false-ish`.

It exports a single variable called `ish`, which can be subtracted from `True`
or `False` to create a TrueIsh or FalseIsh object. This can be compared with
the value to see if it either:

1. Evaluates to `True`
2. Is a string containing the English, French, German, Danish, Swedish, Dutch,
   Afrikaans, Norwegian, Portuguese, Irish, Esperanto, Arabic or Hungarian for
   either `Yes` or `No` (or a handful of slang words with the same meaning).

If it is a string containing none of these known words, it raises
a `ValueError`

```python
if 'Yup' == True-ish:
    print 'True-ish!'
```

It also does some things I haven't documented yet.

## Compatibility

Ish is compatible with Python 2.7, 3.3+ and PyPy.

## Running Tests

Install [tox](). Run `tox` in the top-level directory. This should run the
tests against all supported Python versions.

## Contributing to Ish

Contributions are received with love and enthusiasm! That said, if you would
like to contribute to ish, please follow some basic guidelines:

* We like `PEP-8`. Not in an aggressive way, but you should follow PEP-8 98%
  of the time.
* Run the tests before you commit, and make sure they pass.
* Please write some unit tests for any added functionality.

:heart:
