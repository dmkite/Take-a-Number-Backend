from tornado.httpserver import HTTPServer
from tornado.web import Application
from tornado.options import define, options
from tornado.ioloop import IOLoop

from todo.api import PingHandler

define('port', default=4000, help='port to list on')

handlers = [
	(r'/ping', PingHandler)
]

def main():
	app = Application(handlers)
	http_server = HTTPServer(app)
	http_server.listen(options.port)	
	print('Listening on http://localhost:{}'.format(options.port'))
	IOLoop.current().start()
