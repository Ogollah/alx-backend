#!/usr/bin/env python3
"""Pagination module
"""
from typing import Tuple, List, Dict
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a range of indexes for a pagination param."""
    start = (page - 1) * page_size
    end = start + page_size
    return start, end


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes a new Server instance."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get data based on ranges of index."""
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]

    def calculate_total_pages(self, page_size: int) -> int:
        """Calculates the total number of pages."""
        return math.ceil(len(self.__dataset) / page_size)

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Prepares and returns a dictionary of values."""
        start, end = index_range(page, page_size)
        csv_data = self.get_page(page, page_size)
        total_pages = self.calculate_total_pages(page_size)

        res = {
            'page_size': len(csv_data),
            'page': page,
            'data': csv_data,
            'next_page': page + 1 if end < len(self.__dataset) else None,
            'prev_page': None if start < 1 else page - 1,
            'total_pages': total_pages,
        }
        return res
