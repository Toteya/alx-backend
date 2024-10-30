#!/usr/bin/env python3
"""
2-lifo_cache
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Cache system: uses the LIFO caching policy
    Inherits BaseCaching
    """

    def __init__(self):
        """ Initialise cahing system instance
        """
        super().__init__()

    def put(self, key, item):
        """ Stores to cache the key and item provided
        """
        if not (key is None or item is None):
            self.cache_data.update({key: item})

        if len(self.cache_data) > self.MAX_ITEMS:
            key_last = self.cache_data.popitem()
            print("DISCARD: {}".format(key_last))

    def get(self, key):
        """ Returns from cache the item corresponding the given key
        """
        return self.cache_data.get(key)
