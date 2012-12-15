# -*- coding: utf-8 -*-
'''This package contains the classes, data, and AI programming for the "players".'''
class player(object):

	def __init__(self):
		pass

class party(object):

	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.players = []
		#Todo: stuff
		self.players.append(player())
