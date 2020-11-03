from tornado.httpserver import HTTPServer
from tornado.web import Application
from tornado.options import define, options
from tornado.ioloop import IOLoop

define('port', default=4000, help='port to list on')

def main():
	app = Application()
	http_server = HTTPServer(app)
	http_server.listen(options.port)	
	print('Listening on http://localhost:{}'.format(options.port'))
	IOLoop.current().start()
