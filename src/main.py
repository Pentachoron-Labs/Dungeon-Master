# -*- coding: utf-8 -*-
import PyQt4.Qt as q
from lang import lang
import dgc

class win(object):
	
	def __init__(self):
		app = q.QApplication([])
		self.widget = dgc.widget()
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
		#Game-screen initialization
		self.scrollpane = dgc.listwidget(self.widget)
		self.scrollpane.hide()
		self.scrollpane.move(400,0)
		self.scrollpane.resize(200,400)
		self.populatescrollpane()
		self.populatedungeon()
		app.exec_()
	
	def opennewgame(self):
		'''Open new game menu.'''
		self.hideall()
		#TODO: probably add an intermediary screen
		self.startnewgame()

	def openoptions(self):
		'''Open options menu.'''
		self.hideall()

	def hideall(self):
		self.btnstart.hide()
		self.btnoptions.hide()
	
	#### Game screen shtuff ####
	def startnewgame(self):
		self.hideall()
		self.scrollpane.show()
		self.testlabel.show()
		self.testlabel2.show()
	
	def populatescrollpane(self):
		self.testimg = q.QListWidgetItem('Example',self.scrollpane)
		self.testimg.setIcon(q.QIcon('rsc/img/example.gif'))
	
	def populatedungeon(self):
		self.testlabel = dgc.imglabel(self.widget)
		self.testlabel.setPixmap(q.QPixmap('rsc/img/blank.gif'))
		self.testlabel.hide()
		self.testlabel.move(100,100)
		self.testlabel2 = dgc.imglabel(self.widget)
		self.testlabel2.setPixmap(q.QPixmap('rsc/img/blank.gif'))
		self.testlabel2.hide()
		self.testlabel2.move(200,100)
		
window = win()
