from cyclone import redis
from twisted.internet import defer


def Connection():
    # may expand settings in future
    redis_conf = {
        'dbid': 1
    }
    return redis.lazyConnectionPool(**redis_conf)