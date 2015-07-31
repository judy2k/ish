## Ish

Ish is a stupid library that allows you to test if a variable is `true-ish` or
`false-ish`.

It exports a single variable called `ish`, which can be subtracted from `True`
or `False` to create a TrueIsh or FalseIsh object. This can be compared with
the value to see if it either:

1. Evaluates to `True`
2. Is a string containing the English, French, German, Danish, Dutch,
   Afrikaans, Swedish, Norwegian, Portuguese, Irish, Esperanto or Arabic for
   either `Yes` or `No` (or a handful of slang words with the same meaning).

If it is a string containing none of these known words, it raises
a `ValueError`

```python
if 'Yup' == True-ish:
    print 'True-ish!'
```

It also does some things I haven't documented yet.