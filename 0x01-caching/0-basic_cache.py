#!/usr/bin/env python3
"""
0-basic_cache
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Caching system
    Inherits BaseCaching
    """

    def put(self, key, item):
        """ stores item and key to cache
        """
        if not (key is None or item is None):
            self.cache_data.update({key: item})
    
    def get(self, key):
        """ Returns the item for the given key
        """
        return self.cache_data.get(key)