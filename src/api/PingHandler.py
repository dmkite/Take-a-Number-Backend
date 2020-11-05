from tornado.web import RequestHandler

class PingHandler(RequestHandler):
	"""Verify the system is working"""
	
	def get(self):
		self.write('Backend running')
