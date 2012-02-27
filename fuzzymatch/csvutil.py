"""

"""
import ucsv
import csv

def guess_dialect(filename):
	"""tries to guess the dialect of csv files"""
	best = ''
	max_columns = 0
	for dialect in csv.list_dialects():
		file = open(filename, 'r')
		rd = ucsv.reader(file, dialect=dialect)
		header = rd.next()
		if len(header) > max_columns:
			max_columns = len(header)
			best = dialect
		file.close()
	return best

