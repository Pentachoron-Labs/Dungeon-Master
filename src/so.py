# -*- coding: utf-8 -*-
'''Shared library. Contains several variables used by multiple files.'''
import PyQt4.Qt as q #Note: Always refer to this instead of importing the same (large) library multiple times.
import imp,os,sys,random,time
'''ID of selected object from the scrollpane. Generally, use so.objs[so.selectedobject] for obj data.'''
selectedobject = None
'''List of extended object modules.'''
objmods = []
'''Dict of gameobjs.'''
objs = {}
'''Grid (the current game grid) of obj IDs.'''
grid = []
'''Image grid (reference to main.grid)'''
imggrid = []
'''Coordinates of the dungeon entrance (there can be only one.)'''
entrancecoords = None
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
		if z: objs[y] = z
	#Init grid
	for i in range(20):
		grid.append([])
		for j in range(20):
			grid[i].append('blank')

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

def getpath(grid):
	'''From a grid of obj IDs, checks if there exists a path between an
	entrance on any side (this function does find it itself) and the goal
	point. If such a path exists, the function returns the list containing
	it; if it does not, the function returns None.'''
	if not entrancecoords: return None,None,None #thereby saving us a lot of trouble
	path = []
	options = []
	#Elements marked 0 are blank, 1 are green, and 2 are walls.
	marked = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]
	#Find the walls and the goal simultaneously.
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j].issolid: marked[i][j] = 2
			if grid[i][j].ID == 'goal': goal = (j,i)
	path.append(entrancecoords)
	if len(path) == 0: return None,None,None
	marked[path[0][1]][path[0][0]] = 1
	while path[-1] != goal:
		path, options, marked = _step(path, options, marked)
		if not path: return None,None,None
	return path, options, marked

def _step(path, options, marked):
	x,y = path[-1]
	new = []
	if (y > 0) and (marked[y-1][x] == 0): new.append((x,y-1))
	if ((y+1) < len(marked)) and (marked[y+1][x] == 0): new.append((x,y+1))
	if (x > 0) and (marked[y][x-1] == 0): new.append((x-1,y))
	if ((x+1) < len(marked[0])) and (marked[y][x+1] == 0): new.append((x+1,y))
	for i in new:
		if i in options: new.remove(i)
	if new == []:
		if options == []: return None,None,None
		path.append(options.pop(0))
	else:
		path.append(new.pop(0))
		options.extend(new)
	marked[path[-1][1]][path[-1][0]] = 1
	return path,options,marked

def setobj(x,y,obj):
	'''Sets object at (x,y) to a new instance of the specified object ID.'''
	grid[y][x] = objs[obj](x,y)
	imggrid[(y*20)+x].setPixmap(objs[obj].pixmap)
