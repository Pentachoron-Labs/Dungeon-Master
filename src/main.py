# -*- coding: utf-8 -*-
from lang import lang,qlang
import dgc,so
q = so.q #Better than loading the same library three times... or ten.

class win(object):
	
	def __init__(self):
		app = q.QApplication([])
		so.init()
		self.widget = dgc.widget()
		self.widget.setWindowTitle(qlang('gui.title'))
		self.widget.setWindowIcon(q.QIcon('rsc/icon.png'))
		self.widget.resize(600,400)
		self.widget.show()
		self.btnstart = q.QPushButton(qlang('gui.newgame'),self.widget)
		self.btnstart.show()
		self.btnstart.move(300-(self.btnstart.width()/2),50)
		self.widget.connect(self.btnstart,q.SIGNAL('clicked()'),self.opennewgame)
		self.btnoptions = q.QPushButton(qlang('gui.options'),self.widget)
		self.btnoptions.show()
		self.btnoptions.move(300-(self.btnoptions.width()/2), 100)
		self.widget.connect(self.btnoptions,q.SIGNAL('clicked()'),self.openoptions)
		#Game-screen initialization
		self.scrollpane = dgc.listwidget(self.widget)
		self.scrollpane.hide()
		self.scrollpane.move(400,0)
		self.scrollpane.resize(200,400)
		self.scrollpane.setSelectionMode(1)
		so.selectedobject = 'empty'
		self.widget.connect(self.scrollpane,q.SIGNAL('itemSelectionChanged()'),self.updateselection)
		for i in so.objs:
			x = so.objs[i]
			if x.haswidgetitem:
				x.widgetitem = q.QListWidgetItem(qlang('object.%s'%i),self.scrollpane)
				if x.icon: x.widgetitem.setIcon(x.icon)
				x.widgetitem.obj = i
				if i == 'empty': x.widgetitem.setSelected(True)
		self.populatedungeongui()
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
		for i in self.grid: i.show()
	
	def populatedungeongui(self):
		self.grid = []
		for i in range(400):
			x = dgc.imglabel(self.widget)
			x.setobj('blank')
			x.hide()
			x.move((i%20)*20,(i/20)*20)
			x.setScaledContents(True)
			x.resize(20,20)
			self.grid.append(x)
		self.grid[[189,190,209,210][so.random.randrange(4)]].setobj('goal')
	
	def updateselection(self):
		so.selectedobject = self.scrollpane.selectedItems()[0].obj

window = win()
