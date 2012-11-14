# -*- coding: utf-8 -*-
import so
q = so.q

class widget(q.QWidget):
	
	def __init__(self, parent=None):
		super(widget,self).__init__(parent)

class imglabel(q.QLabel):
	
	def __init__(self, parent=None):
		super(imglabel,self).__init__(parent)

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

class listwidget(q.QListWidget): pass
