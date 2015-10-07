# MyMDb-tools
**MyMDb tools** is a small collection of scripts for use with the [MyMDb](http://prot.gr/mymdb) wiki ontology by Ioannis Protonotarios.

## MyMDb-series-scraper
MyMDb episode scraper from IMDb series pages

This is a python script that paired with [pywikibot](https://www.mediawiki.org/wiki/Manual:Pywikibot) allows the bulk creation of all episode pages of a series.

### Usage
Enter the IMDb ID of a series and the number of the last season you want to get episodes up to (usually the final season).

The script will produce a text file named: `scraped-episodes.txt`

Then, use this text file as input to the pywikibot script and let it auto-create all pages:

`python pwb.py pagefromfile.py -file:scraped-episodes.txt -notitle`

## IMDb-to-MyMDb-bookmarklet

This is a javascript bookmarklet that allows the quick adding of a movie while browsing it on IMDb.
