import urllib2
import sys
import MySQLdb
from STATUS import INIT
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf8')
db = MySQLdb.connect("localhost", "root", "root", "house")
db.set_character_set('utf8')
cursor = db.cursor()

def writeLink(url):
    sql = "INSERT into link_list(link, status) VALUES ('%s', '%d')" % (url, INIT)
    print sql
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print "ERROR"
    return True


def close():
    db.close()
#max p8
p = ['p1','p2','p3','p4','p5','p6']
#max a8
a = ['a1','a2','a3','a4','a5','a6']
#max l6
l = ['l1','l2','l3','l4','l5','l6']
#max sf5
sf =['sf1','sf2','sf3','sf4','sf5']
#max lc5
lc = ['lc1','lc2','lc3','lc4','lc5','lc6']
#max f5
f = ['f1','f2','f3','f4','f5','f6']
#page pg 1-100

def genUrl():
    for i in range(100):
        if i > 0:
            url  = "http://bj.lianjia.com/chengjiao/pg"+ str(i) +"rs%E8%A5%BF%E5%9F%8E/"
            if containList(url):
                writeLink(url)

def containList(url):
    try:
        response = urllib2.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, "html5lib")
        count = 0
        for i in soup.find(class_="listContent").children:
            if count > 0:
                return True
            count = count + 1
        if count == 0:
            return False
    except:
        return False
if __name__ == '__main__':
    #url = "http://bj.lianjia.com/chengjiao/l6a6p1pg100/"
    #print containList(url)
    #genUrl()
    #genUrlWithParameter(sys.argv[1])
    genUrl()
    close()