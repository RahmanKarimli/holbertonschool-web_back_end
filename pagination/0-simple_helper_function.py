#!/usr/bin/env python3
'''
Module defines simple helper function
'''
from typing import Tuple


def index_range(page, page_size):
    '''
    Function that returns a tuple of size two
    containing a start index and an end index
    '''
    return ((page * page_size) - page_size, page * page_size)

print(index_range(2, 3))