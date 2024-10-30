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
        self._keys = []
        super().__init__()

    def put(self, key, item):
        """ Stores to cache the key and item provided
        """
        if key is None or item is None:
            return

        self.cache_data.update({key: item})
        if key in self._keys:
            self._keys.remove(key)
        self._keys.append(key)

        if len(self.cache_data) > self.MAX_ITEMS:
            # key_last = list(self.cache_data.keys())[-2]
            key_last = self._keys[-2]
            self.cache_data.pop(key_last)
            print("DISCARD: {}".format(key_last))

    def get(self, key):
        """ Returns from cache the item corresponding the given key
        """
        return self.cache_data.get(key)
