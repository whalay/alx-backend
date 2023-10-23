#!/usr/bin/env python3
""" This module contains a simple helper function. """
from typing import Tuple, Dict


def index_range(page: int, page_size: int, **kwargs: Dict[str, int]) -> Tuple:
    """
        This function The function should return a tuple of size two
        containing a start index and an end index corresponding to the
        range of indexes to return in a list for those particular
        pagination parameters.
    """

    if kwargs:
        page = kwargs.get('page')
        page_size = kwargs.get('page_size')

    return ((page - 1) * page_size, page * page_size)
