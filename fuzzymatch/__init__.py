# 
# command line utility for merging two tables
#

import sys

def prompt(question, options, default=None):
	print '\n'+question
	for i in range(len(options)):
		print '   [%s]: %s' % (str(i), options[i])
	print
	if default is not None:
		sys.stdout.write("? default: [%s] " % str(default))
	else:
		sys.stdout.write("? ")
	sys.stdout.flush()
	line = sys.stdin.readline().lower().strip()
	if len(line) == 0:
		if default is not None and default in options:
			return options[default]
		else:
			return prompt(question, options, default)
	try:
		return options[int(line)]
	except:
		print "Invalid input!"
		return prompt(question, options, default)


class Result():
	"""Result of a text matching query"""
	
	def __init__(self, id, label, score):
		self.id = id
		self.label = label
		self.score = score

	def __repr__(self):
		return "%s (score: %.3f)" % (self.label, self.score)


