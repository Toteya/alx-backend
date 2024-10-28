#!/usr/bin/env python3
"""
simple_helper_function
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """ Takes page and page_size and returns the start index and end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
