# from cyclone import redis
# from twisted.internet import defer
import redis

def Connection():
    # may expand settings in future
    redis_conf = {
        'host':'127.0.0.1',#'localhost',
        'port': 6379,
        'reconnect': False,#True,
        'dbid': 1,
        'poolsize': 1
    }
    r_conn = redis.Redis()
    return r_conn
    # return redis.lazyConnectionPool(**redis_conf)

