from cyclone.escape import recursive_unicode
from cyclone.web import RequestHandler
from src.lib.logger import Logger

class BaseHandler(RequestHandler, Logger):
    def ok_response(self, response):
        self.set_header('Content-Type', 'application/json')
        msg = {
            'stat': 'OK',
            # Make sure there aren't any bytestrings in response,
            # as those aren't JSONizable.
            'response': recursive_unicode(response)}
        # buf = strutil.enc_json(msg)
        # self.finish(buf)
        self.write(msg)

    def fail_response(self, msg, errors=None, **kwargs):
        self.set_header('Content-Type', 'application/json')
        msg = {
            'stat': 'FAIL',
            'message': msg}

        msg.update(kwargs)

        if errors:
            msg['errors'] = errors

        # self.finish(buf)
        self.write(msg)