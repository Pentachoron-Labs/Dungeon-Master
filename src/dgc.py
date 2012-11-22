# -*- coding: utf-8 -*-
import so
q = so.q

class widget(q.QWidget):
	
	def __init__(self, parent=None):
		super(widget,self).__init__(parent)

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
