from cyclone.web import RequestHandler
from twisted.internet import defer
from src.lib import const
from src.lib.redis_mixin import RedisMixin

class QueueHandler(RequestHandler, RedisMixin):
    @defer.inlineCallbacks
    def get():
        """Return the full queue"""
        queue = self.redis_conn.get(const.QUEUE_KEY)
        yield self.ok_response(queue)

    def post():
        pass