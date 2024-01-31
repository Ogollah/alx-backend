#!/usr/bin/env python3
"""
MRU Caching module.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary with an MRU
    removal mechanism when the limit is reached.
    """

    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item to the cache.
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                    removed_key, _ = self.cache_data.popitem(last=False)
                    # Discard the removed item
                    print("DISCARD:", removed_key)
                self.cache_data[key] = item
                self.cache_data.move_to_end(key, last=False)
            else:
                self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item from the cache with the provided key.
        """
        if key is not None:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
