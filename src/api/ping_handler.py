""" Handler for /ping endpoint"""
from cyclone.web import RequestHandler
from twisted.internet import defer

class PingHandler(RequestHandler):
	"""Verify the system is working"""
	@defer.inlineCallbacks
	def get(self):
		self.write({
			'response': 'Backend running.'
		})
