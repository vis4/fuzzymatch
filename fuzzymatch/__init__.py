# 
# command line utility for merging two tables
#

import sys, os.path, json
import csvutil
import unicodecsv as ucsv
import Levenshtein

def usage():
	print "Usage:\n\nfuzzymatch source_table.csv merge_table.csv result.csv\n" 
	exit(-1)


def cli():
	if len(sys.argv) < 4:
		print "wrong argument count"
		usage()
 
	from_file = sys.argv[1]
	to_file = sys.argv[2]
	out_file = sys.argv[3]
	run(from_file, to_file, out_file)
	

def run(f_file, t_file, o_file):
	
	f_dialect = csvutil.guess_dialect(f_file)
	f_reader = ucsv.reader(open(f_file,'r'), dialect=f_dialect)
	f_header = f_reader.next()
	
	t_dialect = csvutil.guess_dialect(t_file)
	t_reader = ucsv.reader(open(t_file,'r'), dialect=t_dialect)
	t_header = t_reader.next()

	print 'Source table: %s' % f_file
	print 'Target table: %s' % t_file
	
	if os.path.exists(o_file):
		results = json.loads(open(o_file,'r').read())	
	else:
		results = { 'model': {}, 'map': {} }
		results['model']['f_id_col'] = prompt_select('Which column of the source table contains the ids?', f_header)
		results['model']['f_text_col'] = prompt_select('Which column of the source table contains the text to be matched?', f_header)
		results['model']['t_id_col'] = prompt_select('Which column of the target table contains the ids?', t_header)
		results['model']['t_text_col'] =prompt_select('Which column of the target table contains the text to be matched?', t_header)
	
	try:
		f_text_col = f_header.index(results['model']['f_text_col'])
		f_id_col = f_header.index(results['model']['f_id_col'])
		t_text_col = t_header.index(results['model']['t_text_col'])
		t_id_col = t_header.index(results['model']['t_id_col'])
	except:
		print "invalid model"
		exit(-1)
		
	accept_score = 1
	ignore_score = 0.5
	
	t_map = {}
	for t_row in t_reader:
		id = t_row[t_id_col]
		txt = t_row[t_text_col]
		if id not in t_map:
			t_map[id] = []
		t_map[id].append(txt.strip())
		
	for f_row in f_reader:
		f_id = f_row[f_id_col]
		f_text = f_row[f_text_col].strip()
		if f_id in results['map']:# and results['map'][f_id] is not None:
			# already matched
			continue
			
		matches = []
		for t_id in t_map:
			for t_text in t_map[t_id]:
				matches.append(Result(t_id, t_text, Levenshtein.ratio(f_text.lower(), t_text.lower())))
		matches = sorted(matches, key=lambda r: r.score*-1)
		
		m = None
		if matches[0].score >= accept_score:
			m = matches[0]
		elif matches[0].score > ignore_score:
			matches = ['--skip--'] + matches[:9] + ['--manual input--']
			m = prompt_select('Confirm possible match for %s (%s)' % (f_text,f_id), matches, 0)
			if m == '--manual input--':
				m = prompt_text('Insert '+results['model']['t_id_col'])
		
		if m is not None:
			if isinstance(m, Result):
				results['map'][f_id] = m.id
			elif m == '--skip--':
				results['map'][f_id] = None
			else:
				results['map'][f_id] = m #manual inserted id
			out = open(o_file, 'w')
			out.write(json.dumps(results))
			out.close()
				

def prompt_text(question):
	print '\n'+question+'\n'
	sys.stdout.write('? ')
	sys.stdout.flush()
	line = sys.stdin.readline().lower().strip()
	if len(line) == 0:
		print 'empty string not allowed'
		return prompt_text(question)
	return line


def prompt_select(question, options, default=None):
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
		if default is not None:
			return options[default]
		else:
			return prompt_select(question, options, default)
	try:
		return options[int(line)]
	except:
		print "Invalid input!"
		return prompt_select(question, options, default)


class Result():
	"""Result of a text matching query"""
	
	def __init__(self, id, label, score):
		self.id = id
		self.label = label
		self.score = score

	def __repr__(self):
		return "%s (id: %s, score: %.3f)" % (self.label, self.id, self.score)


