#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb
import urllib2
import urllib
from bs4 import BeautifulSoup
import sys
from STATUS import INIT,DONE,FAIL
reload(sys)
sys.setdefaultencoding('utf8')

hds=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},\
    {'User-Agent':'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},\
    {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'},\
    {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},\
    {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},\
    {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},\
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'},\
    {'User-Agent':'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'},\
    {'User-Agent':'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'}]

db = MySQLdb.connect("localhost", "root", "root", "house")
db.set_character_set('utf8')
cursor = db.cursor()


def close():
    db.close()

def genPrimaryKey(*strList):
    tmp = ""
    for i in strList:
        tmp = tmp + "###" + i
    return hash(tmp)

def readLink():
    sql = "select link from link_list where status = %d limit 1" % FAIL
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        link = results[0][0]
        print link
        return link
    except:
        print "Error: unable to fecth data"

def updateLink(url, status):
    sql ="update link_list set status = %d where link = \"%s\"" % (status ,url)
    try:
        print sql
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print "ERROR"
    return True

def mysqlWrite(id, title, alf, href, houseInfo, dealDate, totalPrice, unit, positionInfo, \
               source, unitPrice, dealHouseTxt, url):
    sql = "REPLACE into ori_house_da(id, title, alf, href, \
           houseInfo, dealDate, totalPrice, unit, positionInfo, \
           source, unitPrice, dealHouseTxt, url) \
           VALUES (%d, '%s', '%s', '%s', '%s', '%s', '%s', '%s', \
           '%s', '%s', '%s', '%s', '%s')" % \
          (id, title, alf, href, houseInfo, dealDate, totalPrice, unit, positionInfo, \
           source, unitPrice, dealHouseTxt, url)
    print sql
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print "ERROR"
        return False
    return True



def parseUrl(url):
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "html5lib")
    print soup.prettify()
    if soup.find(class_ = "listContent") == None:
        return False
    if soup.find(class_ = "listContent").children == None:
        return False
    for li in soup.find(class_ = "listContent").children:
        alf = ""
        href = ""
        title = ""
        houseInfo = ""
        dealDate = ""
        totalPrice = ""
        unit = ""
        positionInfo = ""
        source = ""
        unitPrice = ""
        dealHouseTxt = ""
        primaryKey = ""
        try:
            alf = li.a.img['alt']
        except:
            alf = ""
        try:
            href = li.a['href']
        except:
            href = ""
        if li.find(class_ = "title") != None:
            for i in li.find(class_ = "title").children:
                title = i.string
        if li.find(class_ = "houseInfo") != None:
            for i in li.find(class_ = "houseInfo").children:
                if i.string != None:
                    houseInfo = i.string
        if li.find(class_ = "dealDate") != None:
            for i in li.find(class_ = "dealDate").children:
                if i.string != None:
                    dealDate = i.string
        if li.find(class_ = "totalPrice") != None:
            for i in li.find(class_ = "totalPrice").children:
                if i.string != None:
                    if i.string.isdigit():
                        totalPrice = i.string
                    else:
                        unit = i.string
        if li.find(class_ = "positionInfo") != None:
            for i in li.find(class_ = "positionInfo").children:
                if i.string != None:
                    positionInfo = i.string
        if li.find(class_="source") != None:
            for i in li.find(class_ = "source").children:
                if i.string != None:
                    source = i.string
        if li.find(class_ = "unitPrice") != None:
            for i in li.find(class_ = "unitPrice").children:
                if i.string != None:
                    unitPrice = i.string
        if li.find(class_ = "dealHouseTxt") != None:
            for i in li.find(class_ = "dealHouseTxt").children:
                if i.string != None:
                    dealHouseTxt = dealHouseTxt + "###" + i.string
        primaryKey = genPrimaryKey(title, dealDate, totalPrice)
        print title
        mysqlWrite(primaryKey, title, alf, href, houseInfo, dealDate, totalPrice, unit, positionInfo,
                   source, unitPrice, dealHouseTxt, url)
    return True

def run():
    while True:
        try:
            link = readLink()
            if(parseUrl(link)):
                updateLink(link,DONE)
            else:
                updateLink(link,FAIL)
        except:
            print "ERROR"
if __name__ == '__main__':
    #url = "http://bj.lianjia.com/chengjiao/"
    #a = parseUrl(url)
    #print a
    #readLink()
    run()
    close()