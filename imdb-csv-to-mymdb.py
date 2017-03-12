#!/usr/bin/env python
# encoding: utf-8 

import csv
import sys
import datetime

source_file = 'The best alternative and weird movies.csv'

rows = []
movie_type = ''
movie_subtype = ''

now = datetime.datetime.now()
today = str(now.year) + '-' + str(now.month) + '-' + str(now.day)

#f = open(sys.argv[1], 'rt') ## Command line argument
f = open(source_file, 'rt')
try:
	reader = csv.reader(f)
	for row in reader:
		if row[6] == 'Feature Film':
			movie_type = 'movie'
		else:
			movie_type = row[6]
		if movie_type != row[6]:
			movie_subtype = row[6]
		rows.append([row[1],row[5],movie_type,row[7],row[9],row[10],row[11],row[12].title(),row[13],row[14],movie_subtype])
finally:
	f.close()

with open('movies2mymdb.txt', 'w') as text_file:
	iterrows = iter(rows)
	next(iterrows) # skip 1st row
	for row in iterrows:
		text_file.write("{{{{-start-}}}}\n'''{1}'''\n{{{{Movie\n|Has IMDb ID={0}\n|Is of movie type={2}\n|Is of movie subtype={10}\n|Has year of release={6}\n|Has date of release={9}\n|Is directed by={3}\n|Is of genre={7}\n|Has runtime={5} min\n|Has IMDb archived rating={4}\n|Has IMDb archived rating date={11}\n|Has IMDb archived votes={8}\n|Is watchlisted=Ναι\n}}}}\n{{{{-stop-}}}}\n\n".format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],today))
