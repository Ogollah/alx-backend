#!/usr/bin/env python3
'''
LRU Caching module
'''
from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    '''Least Recently Used (LRU) Cache class
    '''

    def __init__(self) -> None:
        '''Constructor method to initialize the LRU Cache.
        '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''Adds an item to cache_data with the provided key.
        '''
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                    removed_key, _ = self.cache_data.popitem(last=True)
                    # Discard the removed item
                    print("DISCARD:", removed_key)
                self.cache_data[key] = item
                self.cache_data.move_to_end(key, last=False)
            else:
                self.cache_data[key] = item

    def get(self, key):
        '''Retrieves an item from cache_data with the provided key.
        '''
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
