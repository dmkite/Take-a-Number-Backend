from cyclone.web import RequestHandler
from twisted.internet import defer
from src.lib import const
# from src.lib.redis_mixin import RedisMixin
from src.lib.error_handling import handle_error
from src.lib.base import BaseHandler

class QueueHandler(BaseHandler):

    def _get_queue(self):
        len = self.application.redis_conn.llen(const.QUEUE_KEY)
        if not len:
            return []
        else:
            return self.application.redis_conn.lget(const.QUEUE_KEY)

    @handle_error
    @defer.inlineCallbacks
    def get(self):
        """Return the full queue"""
        queue = self._get_queue
        if not queue:
            self.application.redis_conn.lset(
                const.QUEUE_KEY, 0, '')
        # import pdb; pdb.set_trace()
        yield self.ok_response(None)
    


    @handle_error
    @defer.inlineCallbacks
    def post(self):
        tel = self.get_argument('tel')
        name = self.get_argument('nam')
        iat = 
        queue = self._get_queue()
        queue.append()

