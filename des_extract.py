from bs4 import BeautifulSoup
import urllib2
import requests

url = raw_input('Enter the youtube link: ')
sc = requests.get(url)

soup = BeautifulSoup(sc.text,'lxml')
#anime = soup.select('li a')
print "======Following is the description====="
ls = soup.find(id="eow-description")
st = list(ls)
#print st[0]=='<br/'
for a in st:
	try:
		if str(a) == '<br/>':
			continue
		else:
			print a
	except:
		print "---UNKNOWN LIST WORD----"
		