# -*- coding: utf-8 -*-
from lang import lang,qlang
import lang as lang_
import dgc,so,player
q = so.q #Better than loading the same library three times... or ten.

class win(object):
	
	def __init__(self):
		self.app = q.QApplication([])
		so.init()
		self.widget = dgc.widget('gui.title')
		self.widget.setWindowIcon(q.QIcon('rsc/icon.png'))
		self.widget.resize(600,400)
		self.widget.show()
		self.btnstart = dgc.button('gui.newgame',self.widget)
		self.btnstart.show()
		self.btnstart.move(300-(self.btnstart.width()/2),50)
		self.widget.connect(self.btnstart,q.SIGNAL('clicked()'),self.opennewgame)
		self.btnoptions = dgc.button('gui.options',self.widget)
		self.btnoptions.show()
		self.btnoptions.move(300-(self.btnoptions.width()/2), 100)
		self.widget.connect(self.btnoptions,q.SIGNAL('clicked()'),self.openoptions)
		#Game-screen initialization
		self.scrollpane = dgc.listwidget(self.widget)
		self.scrollpane.hide()
		self.scrollpane.move(400,0)
		self.scrollpane.resize(200,200)
		self.scrollpane.setSelectionMode(1)
		so.selectedobject = 'empty'
		self.widget.connect(self.scrollpane,q.SIGNAL('itemSelectionChanged()'),self.updateselection)
		for i in so.objs:
			x = so.objs[i]
			if x.haswidgetitem:
				x.widgetitem = dgc.lwitem('object.%s'%i,i,self.scrollpane)
				if x.icon: x.widgetitem.setIcon(x.icon)
				if i == 'empty': x.widgetitem.setSelected(True)
		self.populatedungeongui()
		#Game-screen shtuffs
		self.gamebox = dgc.groupbox('gui.groupbox',self.widget)
		self.gamebox.hide()
		self.gamebox.move(400,200)
		self.gamebox.resize(200,200)
		self.btngo = dgc.button('gui.gobutton',self.gamebox)
		self.btngo.hide()
		self.btnexit = dgc.button('gui.exitbutton',self.gamebox)
		self.btnexit.hide()
		self.widget.connect(self.btngo,q.SIGNAL('clicked()'),self.startround)
		self.widget.connect(self.btnexit,q.SIGNAL('clicked()'),self.exitgame)
		self.gblayout = q.QVBoxLayout(self.widget)
		self.gblayout.addWidget(self.btngo)
		self.gblayout.addWidget(self.btnexit)
		self.gamebox.setLayout(self.gblayout)
		self.langbox = q.QComboBox(self.widget)
		self.langbox.hide()
		self.langbox.addItems(lang_.supported.keys())
		self.langbox.move(300-(self.langbox.width()/2),50)
		self.widget.connect(self.langbox,q.SIGNAL('activated(QString)'),self.changelang)
		self.btnback = dgc.button('gui.exitbutton',self.widget)
		self.btnback.hide()
		self.btnback.move(300-(self.btnexit.width()/2),350)
		self.widget.connect(self.btnback,q.SIGNAL('clicked()'),self.exitgame)
		self.app.exec_()
	
	def opennewgame(self):
		'''Open new game menu.'''
		self.hideall()
		#TODO: probably add an intermediary screen
		self.startnewgame()

	def openoptions(self):
		'''Open options menu.'''
		self.hideall()
		self.langbox.show()
		self.btnback.show()

	def hideall(self):
		self.btnstart.hide()
		self.btnoptions.hide()
		self.scrollpane.hide()
		self.gamebox.hide()
		self.btngo.hide()
		self.btnexit.hide()
		for i in self.grid: i.hide()
		self.langbox.hide()
		self.btnexit.hide()
		self.btnback.hide()
	
	#### Game screen shtuff ####
	def startnewgame(self):
		self.hideall()
		self.scrollpane.show()
		self.gamebox.show()
		self.btngo.show()
		self.btnexit.show()
		for i in self.grid: i.show()
		
	def populatedungeongui(self):
		self.grid = []
		so.imggrid = self.grid
		for i in range(400):
			x = dgc.imglabel(i%20,i/20,self.widget)
			x.hide()
			x.move((i%20)*20,(i/20)*20)
			x.setScaledContents(True)
			x.resize(20,20)
			self.grid.append(x)
			so.setobj(i%20,i/20,'blank')
		so.setobj(9+(so.random.random()>.5),9+(so.random.random()>.5),'goal')
	
	def updateselection(self):
		so.selectedobject = so.objs[self.scrollpane.selectedItems()[0].obj](-1,-1)

	def startround(self):
		path,options,marked = so.getpath(so.grid) #although I don't think I'll need any of them… yet.
		if not path:
			q.QMessageBox.about(self.widget,qlang('nopath.title'),qlang('nopath.text'))
			return
		ec = so.entrancecoords
		party = player.party(ec[0],ec[1])
		playerpixmap = q.QPixmap('rsc/img/player.gif')
		party.label = dgc.playerlabel(party,self.widget)
		party.label.move(ec[0]*20,ec[1]*20)
		party.label.setScaledContents(True)
		party.label.resize(20,20)
		party.label.setPixmap(playerpixmap)
		party.label.show()
		while party.active:
			party.act()
			self.app.processEvents()

	def exitgame(self):
		self.hideall()
		self.openmain()

	def openmain(self):
		self.btnstart.show()
		self.btnoptions.show()

	def changelang(self):
		lang_.curr = unicode(self.langbox.currentText())
		for i in dgc.textobjs: i.updatetext()

window = win()
