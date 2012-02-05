"""

"""
import unicodecsv as ucsv
import csv

def guess_dialect(file):
	"""tries to guess the dialect of csv files"""
	best = ''
	max_columns = 0
	file = open(file,'r')
	for dialect in csv.list_dialects():
		reader = ucsv.reader(file, dialect=dialect)
		header = reader.next()
		if len(header) > max_columns:
			max_columns = len(header)
			best = dialect
	file.close()
	return best

