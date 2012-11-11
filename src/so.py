# -*- coding: utf-8 -*-
'''Shared library. Contains several variables used by multiple files.'''
import PyQt4.Qt as q
'''ID of selected object from the scrollpane. Generally, use so.objs[so.selectedobject] for obj data.'''
selectedobject = None

class gameobj(object):
	
	def __init__(self,id):
		self.id = id
		self.icon = q.QIcon('rsc/img/%s.gif' %id)
		self.pixmap = q.QPixmap('rsc/img/%s.gif' %id)
	
	def __str__(self):
		return 'Game object "%s" at %d' %(self.id, id(self))

'''Dict of gameobjs.'''
objs = {}
'''Grid (the current game grid) of obj IDs.'''
grid = []
def init():
	#Init objs
	x = open('rsc/objlist')
	y = 'spam'
	while True:
		y = x.readline()
		if y == '': break
		if y[:3] == '\xef\xbb\xbf': y = y[3:]
		if y[-1] == '\n': y = y[:-1]
		if y[-1] == '\r': y = y[:-1]
		z = gameobj(y)
		objs[y] = z
	#Init grid
	for i in range(20):
		grid.append([])
		for j in range(20):
			grid.append('blank')
