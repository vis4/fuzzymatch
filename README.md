# fuzzymatch

Interactive command line utility to merge two tables based on text similarity of two columns.

## How it works

fuzzymatch uses the [Levenshtein](http://pypi.python.org/pypi/python-Levenshtein/) package to compute similarity between strings taken from two csv files. In ambiguous cases it will ask the user to chose among top-guesses.

The resulting matches will be stored in a separate JSON file. You can cancel the merging process (ctrl-c) and proceed at the point you stopped later. If you run fuzzymatch on two csv files for the first time (which is when the json db doesn't exist) it will ask you which columns it should use for text matching.


	$ fuzzymatch kek-presse.csv ivw-printauflagen.tsv out.json
	Source table: kek-presse.csv
	Target table: ivw-printauflagen.tsv
	
	Confirm possible match for Aachener Nachrichten
	   [0]: --skip--
	   [1]: Aichacher Nachrichten (id: 1026810812, score: 0.878)
	   [2]: Dachauer Nachrichten (id: 1472411012, score: 0.850)
	   [3]: Schongauer Nachrichten (id: 1472411038, score: 0.810)
	   [4]: Cuxhavener Nachrichten (id: 1276232800, score: 0.810)
	   [5]: Schleswiger Nachrichten (id: 1201410400, score: 0.791)
	   [6]: Rieser Nachrichten (id: 1026813000, score: 0.789)
	   [7]: Schorndorfer Nachrichten (id: 1655012412, score: 0.773)
	   [8]: Eckernförder Nachrichten (id: 1371211400, score: 0.773)
	   [9]: Holsteiner Nachrichten (id: 1643212200, score: 0.762)
	
	? default: [0] 


