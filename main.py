import os, sys, datetime
from time import strftime
from urllib2 import urlopen, urlparse
from urllib import urlretrieve
import feedparser
from bs4 import BeautifulSoup

def main():
	picpath = "/home/simong/Pictures/wallpaper/APOD/"
	feedurl = "http://apod.nasa.gov/apod.rss"
	apodroot = "http://antwrp.gsfc.nasa.gov/apod/"
	getapod(feedurl, apodroot, picpath)
	
def getapod(feedurl, apodroot, picpath):
	today = datetime.date.today()
	filedate = today.strftime('%y%m%d')
	apodhtml = "ap"+filedate+".html"
	apodurl = apodroot + apodhtml
	try:
		soup = BeautifulSoup(urlopen(apodurl))
	except: URLError, e
		if hasattr(e, 'reason')
			print "We can't reach the server. Reason: " + e.reason
		elif hasattr(e, 'code'')
			print "There's a problem. Site says " + e.code
	else:		
		apodsrc = soup.img['src']
		apodfile = apodsrc.split("/")[2]
		apodimg = apodroot + apodsrc
		picfile = os.path.join(picpath, apodfile)
		urlretrieve(apodimg, picfile)
		setapod(picfile)
	
def getapodlist(url, picpath):
	feed = feedparser.parse(url)
	for item in feed["items"]:
		pic = item["description"]
		parseurl = urlparse.urlsplit(pic)
		outfile = parseurl.parse.split("/")[3]
		picfile = os.path.join(picpath, outfile)
		if os.path.isfile(picfile):
			pass
		else:
			urlretrieve(pic, picfile)
			
def setapod(picfile):
	os.system("gsettings set org.gnome.desktop.background picture-uri file:///"+picfile)
	

if __name__ == "__main__":
	main()
	
			

		
		
		
	
