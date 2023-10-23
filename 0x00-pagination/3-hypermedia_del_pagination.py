#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

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
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """ Returns a dictionary with page data """

        assert type(index) == int and index > 0
        assert type(page_size) == int and page_size > 0

        data = []
        next_index = index
        for i in range(page_size):
            indexed_dataset = self.indexed_dataset()
            while True:
                if next_index in indexed_dataset:
                    break
                next_index += 1
            data.append(indexed_dataset[next_index])
            next_index += 1

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data,
        }
