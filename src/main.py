# -*- coding: utf-8 -*-
import PyQt4.Qt as q

class win(object):

	def __init__(self):
		app = q.QApplication([])
		self.widget = q.QWidget()
		self.widget.setWindowTitle('Dungeon Master')
		self.widget.setWindowIcon(q.QIcon('rsc/icon.png'))
		self.widget.resize(600,400)
		self.widget.show()
		self.btnstart = q.QPushButton('New Game',self.widget)
		self.btnstart.move(300,100)
		self.widget.connect(self.btnstart,q.SIGNAL('clicked()'),self.startgame)
		self.btnstart.show()
		app.exec_()

	def startgame(self):
		'''Do stuff.'''
		print 'Starting game'

window = win()
