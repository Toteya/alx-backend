#!/usr/bin/env python3
"""
3-lru_cache
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Cache system: based on LRU caching policy
    Inherits BaseCaching
    """

    def __init__(self):
        """ Initialises cache instant
        """
        self._keys = []
        super().__init__()

    def put(self, key, item):
        """ Stores to cache the key and item provided
        """
        if key is None or item is None:
            return

        self.cache_data.update({key: item})
        self.update_score(key)

        if len(self.cache_data) > self.MAX_ITEMS:
            lru_key = self._keys[0]
            self.cache_data.pop(lru_key)
            self._keys.remove(lru_key)
            print("DISCARD: {}".format(lru_key))
            # print(self._keys)

    def get(self, key):
        """ Returns from cache the item corresponding the given key
        """
        if key in self.cache_data.keys():
            self.update_score(key)
        return self.cache_data.get(key)

    def update_score(self, key):
        """ Updates the cache score for the LRU caching algorithm
        """
        if key in self._keys:
            self._keys.remove(key)
        self._keys.append(key)
        # print(self._keys)
