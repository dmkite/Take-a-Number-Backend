""" Handler for /ping endpoint"""
from cyclone.web import RequestHandler
import json

class PingHandler(RequestHandler):
	"""Verify the system is working"""
	def get(self):
		self.write('Backend running')
