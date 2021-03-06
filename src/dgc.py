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

	def closeEvent(self, event):
		if q.QMessageBox.question(self,qlang('confirmexit.title'),qlang('confirmexit.text'),q.QMessageBox.StandardButtons(81920),65536) == 16384: event.accept()
		else: event.ignore()

class imglabel(q.QLabel):
	
	def __init__(self, x, y, parent=None):
		super(imglabel,self).__init__(parent)
		self.X = x
		self.Y = y

	def mousePressEvent(self, e):
		if so.grid[self.Y][self.X].canbereplaced(so.selectedobject.ID) and \
		   so.selectedobject.canreplace(self.X,self.Y):
			so.setobj(self.X,self.Y,so.selectedobject.ID)
		e.accept()
	
	def enterEvent(self, e):
		self.setStyleSheet('QLabel{border: 1px solid black;}')
		e.accept()
	
	def leaveEvent(self, e):
		self.setStyleSheet('')

class playerlabel(q.QLabel):

	def __init__(self, player, parent=None):
		super(playerlabel,self).__init__(parent)
		self.player = player

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
