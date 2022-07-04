#!/usr/bin/python3


def lookup(obj):
    """List available attributes and methods of an object

    Args:
        obj: object to list its attributes and methods

    Returns:
        a list object
    """
    return dir(obj)
