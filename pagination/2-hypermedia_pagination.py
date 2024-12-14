#!/usr/bin/env python3
'''
Pagination: Simple Task
'''
import csv
import math
from typing import List
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    Function that returns a tuple of size two
    containing a start index and an end index
    '''
    return ((page * page_size) - page_size, page * page_size)


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
        """Returns a list of rows corresponding to the requested page"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        indexes = index_range(page, page_size)
        data = self.dataset()

        try:
            return data[indexes[0]:indexes[1]]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        '''Hypermedia pagination'''
        total_len = len(self.dataset())
        total_pages = math.ceil(total_len / page_size)
        next_page = page + 1
        prev_page = page - 1
        if page + 1 > total_pages:
            next_page = None
        if page - 1 == 0:
            prev_page = None

        return {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
