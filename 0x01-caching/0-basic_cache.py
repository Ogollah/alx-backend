#!/usr/bin/env python3
'''Basic Cahesing
'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''Class inheriting from BaseCaching
    '''

    def put(self, key, item):
        '''Adds item to cache data with the provided key
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''Retrieves item from cache_data with provided key
        '''
        return self.cache_data.get(key)
