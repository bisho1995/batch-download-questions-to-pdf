import time
import urllib.request, urllib.parse, urllib.error
from urllib.request import Request,urlopen
try:
    from bs4 import BeautifulSoup
except:
    print('beautiful soup doesnot exist please install beautiful soup')
from urllib.parse import urlparse as up
import os
try:
    import pdfkit
except:
    print('pdfkit doesnot exist please install pdfkit')



def getSoupFromURL(url):
    req=Request(url,headers={'User-Agent': 'Mozilla/5.0'})
    page=urlopen(req).read()
    return BeautifulSoup(page,"html.parser")

def getPath(folder,filename):
    try:
        return os.path.join(folder,filename)
    except:
        raise Exception('There was a problem getting path.')

def doesFolderExists(name):
    return (os.path.isdir(name) and os.path.exists(name))

def createDirectory(name):
    os.makedirs(name)

def getHostname(url):
    return up(url).hostname

url='https://www.programcreek.com/2012/11/top-10-algorithms-for-coding-interview/'
rootHostname= getHostname(url)

thresholdOfUrlLength = 50
saveFolder = rootHostname
errorFile = rootHostname + '_error_'+str(time.time())+'.txt'
linksFile = rootHostname + '_links_'+str(time.time())+'.txt'
i=0


soup =getSoupFromURL(url)
allLinks=soup.findAll('a')


if doesFolderExists(saveFolder) == False:
    createDirectory(saveFolder)



error=open(errorFile, 'w')
file=open(linksFile, 'w')

for link in allLinks:
    tmpUrl=link['href']
    if(len(tmpUrl)>thresholdOfUrlLength):
        hostname= getHostname(tmpUrl)
        if hostname == rootHostname:
            file.write(tmpUrl+'\n')
            try:
                filename=link.text+'.pdf'
                fullpath=getPath(saveFolder,filename)
                print('Working om file: ', tmpUrl)
                pdfkit.from_url(tmpUrl, fullpath)
                i+=1
            except Exception as e:
                print(e)
                error.write(tmpUrl+'\n')

file.close()
error.close();

