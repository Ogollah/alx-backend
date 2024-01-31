#!/usr/bin/env python3
'''
FIFO Caching module
'''
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''FIFO Cache class
    '''

    def __init__(self) -> None:
        '''Constructor method to initialize the FIFO Cache.
        '''
        super().__init__()

    def put(self, key, item):
        '''Adds item to cache_data with the provided key.

        If the number of items exceeds the maximum limit
        it discards the oldest item.
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Discard the oldest item
                oldest_key = next(iter(self.cache_data))
                print("DISCARD: {}".format(oldest_key))
                del self.cache_data[oldest_key]

    def get(self, key):
        '''Retrieves the item from cache_data with the provided key.

        Returns None if the key is not found in the cache.
        '''
        return self.cache_data.get(key)
