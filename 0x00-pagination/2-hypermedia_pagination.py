#!/usr/bin/env python3
""" This module contains a class named Server. """
import csv
import math
from typing import List, Dict, Tuple


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Finds the correct indexes to paginate dataset correctly """

        assert type(page) == int and page > 0
        assert type(page_size) == int and page > 0

        indexes = index_range(page, page_size)
        self.dataset()
        return self.__dataset[indexes[0]:indexes[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ Returns a dictionary with page data """

        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
