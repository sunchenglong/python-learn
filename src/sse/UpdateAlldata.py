import datetime
from SseCraw import SseCraw
from RandomCrawl import RandomCrawl
import MySQLdb
from CleanDataDate import CleanDataDate

class UpdateAlldata:
    def __init__(self):
        self.db = MySQLdb.connect("localhost", "root", "root", "sse", charset='utf8')
        self.cursor = self.db.cursor()
        self.craw_new_part(self.get_maxdate())

    def __del__(self):
        self.cursor.close()
        self.db.close()

    def update_stat(self, dt, page, max_page):
        sql = "REPLACE INTO sse.crawl_stat(dt, page, max_page, stat) " \
              "VALUES('%s','%s','%s','%s')" % (
                  dt, page, max_page, "INIT")
        print sql
        try:
            self.cursor.execute(sql)
            self.db.commit()
            pass
        except:
            self.db.rollback()
            print "Mysql Wrong"

    def get_data(self, begin):
        sql = "select distinct dt,max_page from sse.ori_crawl_sse where dt >= '%s'" % (begin)
        print sql
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def gen_mission(self, table):
        for row in table:
            dt, max_page = row
            for page in range(1, max_page + 1):
                self.update_stat(dt, page, max_page)

    def get_maxdate(self):
        sql = "select max(dt) from sse.crawl_result"
        print sql
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def craw_new_part(self, date):
        print date
        begin = datetime.datetime.strptime(date[0], "%Y-%m-%d")
        end = datetime.datetime.now()
        sse = SseCraw()
        for i in range((end - begin).days):
            day = begin + datetime.timedelta(days=i)
            sse.craw_all_page(day.strftime("%Y-%m-%d"))
            print "====>" + str(day) + " have run done"
        print "====> test"
        print begin.strftime("%Y-%m-%d")
        self.gen_mission(self.get_data(begin.strftime("%Y-%m-%d")))
        RandomCrawl(1000)
        CleanDataDate(begin.strftime("%Y-%m-%d"))


if __name__ == '__main__':
    updateAlldata = UpdateAlldata()
    updateAlldataAgain = UpdateAlldata()