#!/usr/bin/env python3
"""Pagination module
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns the range of indexes for a given pagination.

    Args:
        page (int): The current page.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple representing the range of indexes.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
