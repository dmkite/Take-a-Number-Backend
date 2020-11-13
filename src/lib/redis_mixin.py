import cyclone

class RedisMixin(object):
    redis_conn = None

    @classmethod
    def setup(self):
        # may expand settings in future
        redis_conf = {
            'dbid': 1
        }
        RedisMixin.redis_conn = cyclone.redis.lazyConnectionPool(**redis_conf)