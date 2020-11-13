from unittest import TestCase
from twisted.internet import defer
from io import BytesIO
from http.client import HTTPResponse

from src.api.ping_handler import PingHandler
from take_a_number import Application
from cyclone.httpserver import HTTPRequest

class MockConnection(object):
    """Mock connection object for use with a cyclone Request"""

    def __init__(self):
        self.xheaders = True
        self.buffer = b''
        self._finish_callback = defer.Deferred()

    def write(self, chunk):
        self.buffer += chunk

    def notifyFinish(self):
        return self._finish_callback

    def finish(self):
        if self._finish_callback:
            self._finish_callback.callback(None)

class FakeSocket():
    """Fake socket interface to trick HTTPResponse into reading a string."""

    def __init__(self, response_str):
        self._file = BytesIO(response_str)

    def makefile(self, *args, **kwargs):
        return self._file

class RequestHandlerBase(TestCase):
    def parse_response(self, response_text):
        """
        Given a raw HTTP response, create a httplib.HTTResponse out of it.
        """
        source = FakeSocket(response_text)
        response = HTTPResponse(source)
        response.begin()

        res = response.read()
        return (res, response.status)

    @defer.inlineCallbacks
    def request(self, method, path, body=None):
        app = Application()
        connection = MockConnection()
        req = HTTPRequest(
            method='GET',
            path='/ping',
            remote_ip=None,
            protocol="http",
            connection=connection)
        req.body = body
        req.headers = headers or {}
        application(req)
        yield connection.notifyFinish()
        (body,status) = self.parse_response(connection.buffer)
        defer.returnValue((body, status))

class TestPingHandler(RequestHandlerBase, TestCase):
    @defer.inlineCallbacks
    def test_get(self):
        (body, status) = yield self.request("GET", "/ping")
