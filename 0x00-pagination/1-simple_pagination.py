#!/usr/bin/env python3
import csv
import math
from typing import List
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Takes page and page_size and returns the start index and end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


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
        """ Returns the correct page of the dataset based on given parameters
        """
        assert all(isinstance(x, int) for x in [page, page_size])
        assert page > 0 and page_size > 0

        data_range = index_range(page, page_size)
        start = data_range[0]
        end = data_range[1]
        data_len = len(self.dataset())
        if start >= data_len or end >= data_len:
            return []

        return self.dataset()[start: end]
