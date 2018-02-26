import urllib.request, urllib.parse, urllib.error
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup
from urllib.parse import urlparse as up
import pdfkit


def getSoupFromURL(url):
    req=Request(url,headers={'User-Agent': 'Mozilla/5.0'})
    page=urlopen(req).read()
    return BeautifulSoup(page,"html.parser")

url='https://www.programcreek.com/2012/11/top-10-algorithms-for-coding-interview/'
rootHostname=up(url).hostname

thresholdOfUrlLength=50
pathPrefix='questions\\'
i=0


soup =getSoupFromURL(url)
allLinks=soup.findAll('a')

error=open('errors.txt','w')
file=open('links.txt','w')

for link in allLinks:
    tmpUrl=link['href']
    if(len(tmpUrl)>thresholdOfUrlLength):
        hostname=up(tmpUrl).hostname
        if hostname == rootHostname:
            file.write(tmpUrl+'\n')
            try:
                pdfkit.from_url(tmpUrl, pathPrefix+link.text+'.pdf')
                i+=1
            except Exception as e:
                error.write(tmpUrl+'\n')

file.close()
error.close();

