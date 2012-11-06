# -*- coding: utf-8 -*-
import os

langs = {}
curr = 'en_us' #by default. TODO: load from a config. (TODO: write a config, but we can reuse some of this script.)
supported = {'English (American)':'en_us',
	'Latin (Classical)':'la_cl'}

def load(langname):
	'''Loads a lang file.'''
	global langs
	langs[langname] = {}
	print os.listdir('resources')
	x = open('resources/lang/%s.lang' %langname)
	y = 'spam'
	while True:
		y = x.readline()
		if y == '': break
		if y[:3] == '\xef\xbb\xbf': y = y[3:]
		if (y[0] == '#') or (y[0] == '\n'): continue
		if len(y.split('\t')) != 2:
			print 'Error: Corrupted lang file %s. Contact developers!' %langname
			print 'Faulty line:',repr(y)
			break
		if y[-1] == '\n': y = y[:-1]
		if y[-1] == '\r': y = y[:-1]
		key = y.split('\t')[0].replace('\\t','\t').replace('\\n','\n').replace('\\\\','\\')
		text = y.split('\t')[1].replace('\\t','\t').replace('\\n','\n').replace('\\\\','\\')
		langs[langname][key] = text

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
