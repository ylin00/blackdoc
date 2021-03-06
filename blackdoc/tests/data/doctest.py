docstring = """ a function to open files

    with a very long description

    >>> file = open(
    ...     "very_long_filepath",
    ...     mode="a",
    ... )
    >>> file
    <_io.TextIOWrapper name='very_long_filepath' mode='w' encoding='UTF-8'>

    text after the first example, spanning
    multiple lines

    >>> file.closed
    False

    >>> def myfunc2(arg1, arg2):
    ...     '''Docstring for function myfunc2 in docstring
    ...
    ...     More description of the function.
    ...     '''
    ...     pass
    >>>
"""
lines = docstring.split("\n")
code_units = (1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 1, 1)
line_labels = (
    "none",
    "none",
    "none",
    "none",
    "doctest",
    "doctest",
    "doctest",
    "doctest",
    "doctest",
    "none",
    "none",
    "none",
    "none",
    "none",
    "doctest",
    "none",
    "none",
    "doctest",
    "doctest",
    "doctest",
    "doctest",
    "doctest",
    "doctest",
    "doctest",
    "none",
)
