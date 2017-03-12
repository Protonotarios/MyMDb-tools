# MyMDb-tools
**MyMDb tools** is a small collection of scripts for use with the [MyMDb](http://prot.gr/mymdb) wiki ontology by Ioannis Protonotarios.

## MyMDb-series-scraper.py
MyMDb episode scraper from IMDb series pages

This is a python 2.7 script that paired with [pywikibot](https://www.mediawiki.org/wiki/Manual:Pywikibot) allows the bulk creation of all episode pages of a series.

### Usage
Enter the IMDb ID of a series and the number of the last season you want to get episodes up to (usually the final season).

The script will produce a text file named: `scraped-episodes.txt`

Then, use this text file as input to the pywikibot script and let it auto-create all pages:

`python pwb.py pagefromfile.py -file:scraped-episodes.txt -notitle`

## imdb-csv-to-mymdb.py
For bulk uploading an IMDb list of movies to MyMDb

Converts an IMDb movie list export `csv` to a pywikibot input file.

## IMDb-to-MyMDb-bookmarklet

This is a javascript bookmarklet that allows the quick adding of a movie while browsing it on IMDb. When pressed on an IMDb page, it redirects to a MyMDb new page form with name same as the movie. User may enter more details and save the page.

See [meta](http://meta.protonotarios.eu/wiki/index.php?title=Meta:Bookmarklet_for_IMDb_pages_to_quickly_add_movies_to_MyMDb).

## IMDb-to-MyMDb-API-bookmarklet

Same idea as above, only this time page is saved at once (no form) via API.
