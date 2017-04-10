import MySQLdb
import urllib2
import urllib
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')

db = MySQLdb.connect("localhost", "root", "root", "house")
db.set_character_set('utf8')
cursor = db.cursor()

def writeAction(id, title, alf, href, houseInfo, dealDate, totalPrice, unit, positionInfo, \
               source, unitPrice, dealHouseTxt, url):
    sql = "REPLACE into jdata.user_action(user_id, sku_id, time_str, model_id, \
           type, cate, brand) \
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
