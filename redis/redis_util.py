import redis
from const import REDIS_HOST, REDIS_PORT

class Redis:

    _conn = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=5)
    _strict_conn = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=5)

    @classmethod
    def connection(cls):
        return cls._conn
    
    @classmethod
    def strict_connection(cls):
        return cls._strict_conn
    


class Redis_update:
    conn = Redis.connection()

    @classmethod
    def add_hash_key(cls, key, *args):
        cls.conn.hset(key, *args)
    
    @classmethod
    def get_hash_key(cls, key, *args):
        return cls.conn.hget(key, *args)
    
    @classmethod
    def set_key(cls, key, val):
        cls.conn.set(key, val)
    
    @classmethod
    def get_key(cls, key):
        return cls.conn.get(key)
    
    @classmethod
    def get_all(cls, key):
        return cls.conn.hgetall(key)