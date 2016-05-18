# smartTruncate

Truncate a string without cutting a sentence in the middle.

Syntax: smartTruncate(content, begin=0, length=100, addSuffix=False, suffix=' ...', addPrefix=False, prefix='... ')

Returns dictionary object of the modified string 'result'

If the string was cut, the returned dictionary includes the key 'trimmed_at_index' where it was cut
