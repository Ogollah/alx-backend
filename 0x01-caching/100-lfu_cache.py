#!/usr/bin/env python3
'''
LFU Caching module
'''
from collections import OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    '''Least Frequently Used (LFU) Cache class
    '''

    def __init__(self) -> None:
        '''Constructor method to initialize the LFU Cache.
        '''
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_freq = []

    def __reorder_items(self, mru_key):
        """Reorders the items in this cache based on the most
        recently used item.
        """
        max_positions = []
        mru_freq = 0
        mru_pos = 0
        insert_position = 0
        for i, key_freq in enumerate(self.keys_freq):
            if key_freq[0] == mru_key:
                mru_freq = key_freq[1] + 1
                mru_pos = i
                break
            elif len(max_positions) == 0:
                max_positions.append(i)
            elif key_freq[1] < self.keys_freq[max_positions[-1]][1]:
                max_positions.append(i)
        max_positions.reverse()
        for pos in max_positions:
            if self.keys_freq[pos][1] > mru_freq:
                break
            insert_position = pos
        self.keys_freq.pop(mru_pos)
        self.keys_freq.insert(insert_position, [mru_key, mru_freq])

    def put(self, key, item):
        '''Adds an item to cache_data with the provided key.
        '''
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                    discarded_key, _ = self.keys_freq[-1]
                    self.cache_data.pop(discarded_key)
                    self.keys_freq.pop()
                    print("DISCARD:", discarded_key)
                self.cache_data[key] = item
                insert_position = len(self.keys_freq)
                for i, key_freq in enumerate(self.keys_freq):
                    if key_freq[1] == 0:
                        insert_position = i
