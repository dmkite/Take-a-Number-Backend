import functools
from twisted.internet import defer

def handle_error(method):
    """Returns an error code if a request causes an exception to be thrown"""
    @functools.wraps(method)
    @defer.inlineCallbacks
    def wrapper(self, *args, **kwargs):
        try:
            yield method(self, *args, **kwargs)
        except Exception as e:
            self.log()
            self.fail_response(e)
    return wrapper