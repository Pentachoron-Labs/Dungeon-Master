# -*- coding: utf-8 -*-
'''Shared library. Contains several variables used by multiple files.'''
import PyQt4.Qt as q #Note: Always refer to this instead of importing the same (large) library multiple times.
import imp,os,sys,random
'''ID of selected object from the scrollpane. Generally, use so.objs[so.selectedobject] for obj data.'''
selectedobject = None
'''List of extended object modules.'''
objmods = []
'''Dict of gameobjs.'''
objs = {}
'''Grid (the current game grid) of obj IDs.'''
grid = []
def init():
	#Load object modules
	global objmods
	for i in os.listdir('rsc/extmods'):
		if i[-3:] == '.py':
			try: objmods.append(imp.load_source(i[:-3],'rsc/extmods/%s'%i))
			except Exception as e:
				print sys.excepthook(sys.exc_type,sys.exc_value,sys.exc_traceback)
	#Init objs
	x = open('rsc/objlist')
	y = 'spam'
	while True:
		y = x.readline()
		if y == '': break
		if y[:3] == '\xef\xbb\xbf': y = y[3:]
		if y[-1] == '\n': y = y[:-1]
		if y[-1] == '\r': y = y[:-1]
		z = findobjclass(y)
		if z: objs[y] = z()
	#Init grid
	for i in range(20):
		grid.append([])
		for j in range(20):
			grid.append('blank')

def findobjclass(x):
	print ('Searching for "%s"...' %x),
	import obj
	#Check obj.py
	if x in dir(obj):
		print 'default'
		return eval('obj.%s' %x)
	#Check in each of the loaded object modules.
	for i in objmods:
		if x in dir(i):
			print 'rsc/extmods/%s.py' %i
			return eval(x)
	print 'no definition found; it will not be loaded.'
