from diskcache import DjangoCache as dc
import os
from bson.objectid import ObjectId
from logger.log import log


class CreateCache:

    def __init__(self, cache_name, location=os.path.dirname(__file__), cache_timeout=300, databse_timeout=0.010, shards=8, version=1, options={}):
        self.location = os.path.join(location, cache_name)
        self.params = {
            'TIMEOUT': cache_timeout,
            'DATABASE_TIMEOUT': databse_timeout,
            'SHARDS': shards,
            'OPTIONS': options,
            'LOCATION': self.location,
            'TAG': cache_name,
            'VERSION': version
        }
        self.tag = cache_name
        self.cache = dc(self.location, params=self.params)

    def create_cache(self, data):
        status = True
        try:
            self.cache.set_many(data=data, timeout=self.params.get('TIMEOUT', 1000))
            log.info('cache written successfully')
        except Exception as e:
            log.exception(e)
            status = False
        finally:
            self.cache.close()
        return status

    def get_cache(self, key):
        return self.cache.get(key=key, default=None, read=True, tag=False)

    def delete_cache(self, key):
        return self.cache.delete(key, self.params.get('VERSION', 1), True)

    def add_data(self, key, value):
        return self.cache.add(key=key, value=value, version=self.params.get('VERSION', 1),
                              timeout=self.params.get('TIMEOUT', 300))

    def has_key(self, key):
        return self.cache.has_key(key, version=self.params.get('VERSION', 1))

    def expire(self):
        """
        Call when cache needs to be cleared, removes expired cache content.
        :return: count of items removed
        """
        return self.cache.expire()


data = {
            "atm":{
            "id": str(ObjectId()),
            "data": 'ATM'
        },
            "money": {
            "id": str(ObjectId()),
            "data": 'Money'
            }}
cache = CreateCache(cache_name='test', location=os.getcwd())
cache.create_cache(data)
print([cache.get_cache(k) for k in ['a', 'atm', 'b', 'money']])


