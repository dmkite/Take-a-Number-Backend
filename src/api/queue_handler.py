from cyclone.web import RequestHandler
from twisted.internet import defer
from src.lib import const
# from src.lib.redis_mixin import RedisMixin
from src.lib.error_handling import handle_error
from src.lib.base import BaseHandler

class QueueHandler(BaseHandler):
    @handle_error
    @defer.inlineCallbacks
    def get(self):
        """Return the full queue"""
        queue = 'g'#yield self.redis_conn.get(const.QUEUE_KEY)
        import pdb; pdb.set_trace()
        yield self.ok_response(queue)

    def post():
        pass  