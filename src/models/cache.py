import redis


class Cache(object):

    def __init__(self, host, port, db, expire):
        self.redis = redis.Redis(
            host=host,
            port=port,
            db=db,
        )
        self.expire = expire

    def exists(self, key):
        return self.redis.exists(key) > 0

    def get(self, key):
        return self.redis.get(key).decode("utf-8")

    def set(self, key, value):
        return self.redis.set(key, value, self.expire)
