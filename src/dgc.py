# -*- coding: utf-8 -*-
import PyQt4.Qt as q
import so

class widget(q.QWidget):
	
	def __init__(self, parent=None):
		super(widget,self).__init__(parent)

class imglabel(q.QLabel):
	
	def __init__(self, parent=None):
		super(imglabel,self).__init__(parent)

	def mousePressEvent(self, e):
		self.obj = so.objs[so.selectedobject]
		self.setPixmap(self.obj.pixmap)
		print self.obj
		e.accept()

class listwidget(q.QListWidget): pass
