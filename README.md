# fuzzymatch

Interactive command line utility to merge two tables based on text similarity of two columns.

## How it works

```
$ fuzzymatch kek-presse.tsv ivw-printauflagen.tsv out.json
Source table: kek-presse.tsv
Target table: ivw-printauflagen.tsv

Which column of the source table contains the ids?
   [0]: id
   [1]: name

? 0

Which column of the source table contains the text to be matched?
   [0]: id
   [1]: name

? 1

Which column of the target table contains the ids?
   [0]: IVW_Nummer
   [1]: Titelbezeichnung

? 0

Which column of the target table contains the text to be matched?
   [0]: IVW_Nummer
   [1]: Titelbezeichnung

? 1

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
```

