import datetime

from functools import lru_cache


class SimpleCacheValue:

    def __init__(self, key, value, timeout):
        self.key = key
        self.value = value
        self.timeout = timeout
        self.expires_in = self.get_expiry_date(self.timeout)

    def __str__(self):
        return self.key

    def get_expiry_date(self, seconds):
        x = datetime.datetime.now() + datetime.timedelta(seconds=seconds)
        return x.timestamp()


class SimpleCacheStorage(dict):

    NOT_SET_VALUE = '__simple_cache_storage_key_value_unset__'

    def get(self, key):
        return dict.__getitem__(
            self,
            key,
            self.NOT_SET_VALUE
        )

    def set(self, key, value, timeout):
        dict.__setitem__(
            self,
            key,
            SimpleCacheValue(key, value, timeout)
        )


class SimpleCache:

    def __init__(self):
        self.storage = SimpleCacheStorage()

    def set(self, key, value, timeout):
        self.storage.set(key, value, timeout)

    def get(self, key):

        entry = self.storage.get(key)

        if entry == self.storage.NOT_SET_VALUE:
            return self.storage.NOT_SET_VALUE

        if datetime.datetime.now().timestamp() > entry.expires_in:
            self.remove(key)
            return None

        return entry.value

    def remove(self, key):
        entry = self.storage.get(key)
        if entry != self.storage.NOT_SET_VALUE:
            self.storage.pop(key)

    def clear(self):
        self.storage = {}


cache = SimpleCache()
