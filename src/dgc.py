# -*- coding: utf-8 -*-
import so
from lang import qlang
q = so.q

textobjs = []

def ato(obj):
	global textobjs
	textobjs.append(obj)

class widget(q.QWidget):
	
	def __init__(self, title, parent=None):
		super(widget,self).__init__(parent)
		self.title = title
		self.updatetext()
		ato(self)

	def updatetext(self):
		self.setWindowTitle(qlang(self.title))

class imglabel(q.QLabel):
	
	def __init__(self, pos, parent=None):
		super(imglabel,self).__init__(parent)
		self.pos = pos

	def mousePressEvent(self, e):
		if so.objs[self.obj].canbereplaced(so.selectedobject) and \
		   so.objs[so.selectedobject].canreplace(self.obj):
			self.setobj(so.selectedobject)
		e.accept()
	
	def enterEvent(self, e):
		self.setStyleSheet('QLabel{border: 1px solid black;}')
		e.accept()
	
	def leaveEvent(self, e):
		self.setStyleSheet('')

	def setobj(self, id):
		self.obj = id
		self.setPixmap(so.objs[self.obj].pixmap)
		so.grid[self.pos[1]][self.pos[0]] = self.obj

class listwidget(q.QListWidget): pass

class lwitem(q.QListWidgetItem):

	def __init__(self, title, obj, parent=None):
		super(lwitem,self).__init__(qlang(title),parent)
		self.obj = obj
		self.title = title
		ato(self)

	def updatetext(self):
		self.setText(qlang(self.title))

class button(q.QPushButton):

	def __init__(self, title, parent=None):
		super(button,self).__init__(qlang(title),parent)
		self.title = title
		ato(self)

	def updatetext(self):
		self.setText(qlang(self.title))

class groupbox(q.QGroupBox):

	def __init__(self, title, parent=None):
		super(groupbox,self).__init__(qlang(title),parent)
		self.title = title
		ato(self)

	def updatetext(self):
		self.setTitle(qlang(self.title))
