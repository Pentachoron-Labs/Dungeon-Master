# -*- coding: utf-8 -*-
import PyQt4.Qt as q
from lang import lang

class win(object):
	
	def __init__(self):
		app = q.QApplication([])
		self.widget = q.QWidget()
		self.widget.setWindowTitle(lang('gui.title'))
		self.widget.setWindowIcon(q.QIcon('rsc/icon.png'))
		self.widget.resize(600,400)
		self.widget.show()
		self.btnstart = q.QPushButton(lang('gui.newgame'),self.widget)
		self.btnstart.show()
		self.btnstart.move(300-(self.btnstart.width()/2),50)
		self.widget.connect(self.btnstart,q.SIGNAL('clicked()'),self.opennewgame)
		self.btnoptions = q.QPushButton(lang('gui.options'),self.widget)
		self.btnoptions.show()
		self.btnoptions.move(300-(self.btnoptions.width()/2), 100)
		self.widget.connect(self.btnoptions,q.SIGNAL('clicked()'),self.openoptions)
		app.exec_()
	
	def opennewgame(self):
		'''Open new game menu.'''
		self.btnstart.hide()
		self.btnoptions.hide()

	def openoptions(self):
		'''Open options menu.'''
		self.btnstart.hide()
		self.btnoptions.hide()
		
window = win()
