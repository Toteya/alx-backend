#!/usr/bin/env python3
"""
2-hypermedia_pagination
"""
import csv
import math
from typing import Dict
from typing import List


def index_range(page: int, page_size: int) -> tuple[int, int]:
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

        return self.dataset()[start: end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ Returns a dictionary with information about the results
        """
        # print(f"DATA: {len(self.dataset())}")
        total_pages = math.ceil(len(self.dataset()) / page_size)
        data = self.get_page(page, page_size)
        page_size = len(data)

        next_page = None
        prev_page = None
        if page < total_pages:
            next_page = page + 1
        if page > 1:
            prev_page = page - 1

        hyper_data = {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages

        }
        return hyper_data
