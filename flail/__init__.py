# flail/__init__.py
"""
Flail - Decorators with more injuries

Flail allows any decorator to be transformed into something that looks a little
bit like a ball-and-chain attached to the thing that's being decorated.

Example:
    >>> from flail import _
    >>> _.d = lambda x: x
    >>> @_.__.__.__.d
    >>> def my_fabulous_method():
    >>>      ...

Example:
    >>> from flail import 𞸁
    >>> 𞸁.d = lambda x: x
    >>> @𞸁.ﺻﺻﺻﺻﺻﺻﺻﺻ.d
    >>> def my_fabulous_method():
    >>>      ...
"""

__all__ = ['_']

__version__ = '0.1.0'

_ = type('',(),dict(__getattr__=lambda s,_:s))()


def __getattr__(name):
    """
    Allows any identifier to be the chain of the flail
    """
    return _
