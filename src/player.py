# -*- coding: utf-8 -*-
'''This package contains the classes, data, and AI programming for the "players".'''
import so

class player(object):

	def __init__(self):
		pass

class party(object):

	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.dir = ((x == 0)-(x == 19),(y == 0)-(y == 19)) #A quite ingenious device, if I do say so myself.
		self.players = []
		#Todo: stuff
		self.players.append(player())
		self.options = []
		self.active = True

	def act(self):
		'''Updates the list of options and executes the most viable one.'''
		result = self.circumspecta()
		so.time.sleep(1)
		if result == 'advance':
			self.x += self.dir[0]
			self.y += self.dir[1]
			self.label.move(self.x*20,self.y*20)
		else: self.active = False

	def circumspecta(self):
		'''From Latin circumspectā, "look around". Analyzes their
		current situation and returns the best option.'''
		if not so.grid[self.y+self.dir[1]][self.x+self.dir[0]].issolid: return 'advance'
		self.active = False
