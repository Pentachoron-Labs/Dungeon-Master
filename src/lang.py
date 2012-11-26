# -*- coding: utf-8 -*-
import os
from PyQt4.Qt import QString #And here I am breaking my own rule, but we only need the one class from such a huge library.

langs = {}
curr = 'en_us' #by default. TODO: load from a config. (TODO: write a config, but we can reuse some of this script.)
supported = {}

def load(langname):
	'''Loads a lang file.'''
	global langs
	langs[langname] = {}
	x = open('rsc/lang/%s.lang' %langname)
	y = 'spam'
	while True:
		y = x.readline()
		if y == '': break
		if y[:3] == '\xef\xbb\xbf': y = y[3:]
		if (y[0] == '#') or (y[0] == '\n'): continue
		if len(y.split('\t')) != 2:
			print 'Error: Corrupted lang file %s. Contact developers!' %langname
			print 'Faulty line:',repr(y)
			return False
		if y[-1] == '\n': y = y[:-1]
		if y[-1] == '\r': y = y[:-1]
		key = unicode(y.split('\t')[0].replace('\\t','\t').replace('\\n','\n').replace('\\\\','\\'),'utf-8')
		text = unicode(y.split('\t')[1].replace('\\t','\t').replace('\\n','\n').replace('\\\\','\\'),'utf-8')
		langs[langname][key] = text
	return True

for i in os.listdir('rsc/lang'):
	if i[-5:] == '.lang':
		if load(i[:-5]):
			supported[i[:-5]] = langs[i[:-5]]['lang.name']
print supported

def lang(key):
	'''Gets the text from the currently loaded language for a certain key.
	[Note from Newt: While I discourage the use of "from blah import blah",
	use it here. We do not actually want a lot of lang.lang(whatever)
	clogging up the code.]
	'''
	try:
		return langs[curr][key]
	except KeyError as e:
		if e.message == curr:
			try:
				load(curr)
				return lang(key)
			except IOError:
				print 'Tried to access key %s for language %s, but language could not be loaded. What gives?' %(key,curr)
				raise
		elif e.message == key: print 'Key %s not defined for language %s. Update the lang file!' %(key,curr)
		else: raise
		return ''

def qlang(key):
	'''Returns QString(lang(key)). Just a shortcut function to save space.'''
	return QString(lang(key))
