# -*- coding: utf-8 -*-
import so
from lang import lang,qlang
q = so.q
class gameobj(object):
	'''Base class for game objects.'''
	ID = None
	pixmap = q.QPixmap('')
	icon = None
	haswidgetitem = True
	cost = 0
	issolid = False
	def __init__(self,x,y):
		'''Super this!'''
		self.x = x
		self.y = y
		
	def __str__(self):
		return 'Game object "%s" at %d' %(self.id, id(self))

	def canbereplaced(self,id):
		'''Called to check if this object can be replaced with the selected object.
		id is the string ID of the selected object. Also functions as a
		pre-replacement hook.'''
		return True

	def canreplace(self,x,y):
		'''Called to check if this object can replace the selected tile.
		id is the string ID of the tile's object. Also functions as a
		pre-replacement hook.'''
		return True

class blank(gameobj):
	'''Dungeon wall.'''
	ID = 'blank'
	pixmap = q.QPixmap('rsc/img/blank.gif')
	icon = q.QIcon('rsc/img/blank.gif')
	issolid = True

class empty(gameobj):
	'''Empty space (costs 10 to remove the wall.)'''
	ID = 'empty'
	cost = 10

class goal(gameobj):
	'''Goal that the players must attempt to reach.'''
	ID = 'goal'
	pixmap = q.QPixmap('rsc/img/goal.gif')
	icon = q.QIcon('rsc/img/goal.gif')
	haswidgetitem=False

	def canbereplaced(self,id):
		return False

class entrance(gameobj):
	ID = 'entrance'
	cost = 10

	def canreplace(self,x,y):
		if (x in [0,19]) == (y in [0,19]): return False
		if so.entrancecoords: so.setobj(so.entrancecoords[0],so.entrancecoords[1],'blank')
		so.entrancecoords = (x,y)
		return True
