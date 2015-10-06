
import re
import urllib2
import time

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

imdb_id = 'tt0407362'
final_season = 4
file_name = 'scraped-episodes.txt'
blacklist = ['Pilot','Shotgun']

def series_title(html):
    return re.findall('<title>(.*?) \(TV Series ', html)[0]
        
def episode_titles(html):
    return re.findall('<a href="\/title\/tt\d\d\d\d\d\d\d\/\?ref_=ttep_ep\d+\"\stitle=\"(.*?)\" itemprop=\"url\"> <div data-const=\"tt', html)

def imdb_ids(html):
    return re.findall('<strong><a href="\/title\/tt(.*?)\/\?ref_=ttep_ep', html)

def season_number(html):
    return re.findall('\">\s<div>S(.*?), Ep', html)

def episode_numbers(html):
    return re.findall(', Ep(.*?)<\/div>\s<\/div>\s<\/a>  <\/div>\s  <div class=\"info\" itemprop=\"episodes\" itemscope itemtype=', html)


if __name__ == '__main__':
    html = '' # define string because it needs to be defined in +=
    for season_count in range(1,final_season + 1): # I dont't know why needs to be +1		
        url = 'http://www.imdb.com/title/' + imdb_id + '/episodes?season=' + str(season_count)
        print('Scraping season ' + str(season_count))
        html += urllib2.urlopen(url).read()
        
        print(color.GREEN + ' DONE' + color.END)
        matching = [m for m in blacklist if m in episode_titles(html)]
        
        time.sleep(0.5) 

print('Writing file: ' + file_name)
open(file_name, 'w').close() # clear file contents
f=open(file_name, 'a+')        
for t,i,s,e in zip(episode_titles(html),imdb_ids(html),season_number(html),episode_numbers(html)):
    data = "{{{{-start-}}}}\n'''{}'''\n{{{{Movie\n|Has IMDb ID=tt{}\n|Is part of series={}\n|Is episode of season number={}\n|Is episode number={}\n}}}}\n{{{{-stop-}}}}\n".format(t,i,series_title(html),s,e)
    f.write(data)
f.close()
print(color.GREEN + ' DONE' + color.END)

print('\n' + color.CYAN + 'To bulk create MyMDb pages for all those episodes, use:\n' + color.END + color.BOLD + ' python pwb.py pagefromfile.py -file:' + file_name + ' -notitle' + color.END)

if matching:
    print '\n' + color.RED + 'Warning: The following blacklisted titles were found:\n '+ color.END + color.BOLD + '\n '.join(matching), color.END
    print color.CYAN + '  You should manually edit file ' + file_name + '\n  and disambiguate them before submitting' + color.END
