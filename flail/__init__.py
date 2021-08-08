# flail/__init__.py

__all__ = ['_']

__version__ = '0.1.0'

_ = type('',(),dict(__getattr__=lambda s,_:s))()





