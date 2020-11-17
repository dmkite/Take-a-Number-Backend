""" Handler for /ping endpoint"""
from cyclone.web import RequestHandler
from twisted.internet import defer
from src.lib.logger import Logger
from src.lib.error_handling import handle_error
from src.lib.base import BaseHandler

class PingHandler(BaseHandler):
	"""Verify the system is working"""
	@handle_error
	@defer.inlineCallbacks
	def get(self):
		self.log('pinged')
		yield self.write({
			'response': 'Backend running.'
		})
