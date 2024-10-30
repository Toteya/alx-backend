#!/usr/bin/env python3
"""
1-fifo_cache
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Caching system - uses FIFO caching policy
    Inherits BaseCaching
    """

    def __init__(self):
        """ Initialise cahing system instance
        """
        super().__init__()

    def put(self, key, item):
        """ Stores key and value to cache
        """
        if not (key is None or item is None):
            self.cache_data.update({key: item})

        if len(self.cache_data) > super().MAX_ITEMS:
            key_first = next(iter(self.cache_data))
            self.cache_data.pop(key_first)
            print("DISCARD: {}".format(key_first))

    def get(self, key):
        """ Returns from cache the item corresponding the given key
        """
        return self.cache_data.get(key)
