The ``5-text_indentation`` module
=================================

Using ``text_indentation``
--------------------------

This module defines a function ``text_indentation(text)`` that prints a text with 2 new lines after each '.', '?', and ':' character.

Importing the function from the module:
--------------------------------------
    >>> text_indentation = __import__("5-text_indentation").text_indentation

Checks module docstring:
------------------------
    >>> docstr = __import__("5-text_indentation").__doc__
    >>> len(docstr) > 1
    True

Checks for function docstring:
------------------------------
    >>> funct = __import__("5-text_indentation").text_indentation.__doc__
    >>> len(funct) > 1
    True

Examples:
---------

>>> text_indentation("Hello. World?")
Hello.
<BLANKLINE>
World?

>>> text_indentation("This is a test")
This is a test

>>> text_indentation("")
<BLANKLINE>
