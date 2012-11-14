# -*- coding: utf-8 -*-
import so
from lang import lang,qlang
q = so.q
class gameobj(object):
	'''Base class for game objects.'''
	def __init__(self,id,haswidgetitem=True,cost=0):
		'''Super this!'''
		self.id = id
		if haswidgetitem:
			self.icon = q.QIcon('rsc/img/%s.gif' %id)
		self.pixmap = q.QPixmap('rsc/img/%s.gif' %id)
		self.haswidgetitem = haswidgetitem
		self.cost = cost
		
	def __str__(self):
		return 'Game object "%s" at %d' %(self.id, id(self))

	def canbereplaced(self,id):
		'''Called to check if this object can be replaced with the selected object.
		id is the string ID of the selected object.'''
		return True

	def canreplace(self,id):
		'''Called to check if this object can replace the selected tile.
		id is the string ID of the tile's object.'''
		return True

class blank(gameobj):

	def __init__(self):
		super(blank,self).__init__('blank')
		self.icon = None

class empty(gameobj):

	def __init__(self):
		super(empty,self).__init__('empty',cost=10)
		self.icon = None

class goal(gameobj):

	def __init__(self):
		super(goal,self).__init__('goal',haswidgetitem=False)

	def canbereplaced(self,id):
		return False
