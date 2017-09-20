# -*- coding:UTF-8 -*-
from SseCraw import SseCraw
import MySQLdb


class RandomCrawl():
    def __init__(self, times):
        self.db = MySQLdb.connect("localhost", "root", "root", "sse", charset='utf8')
        self.cursor = self.db.cursor()
        self.sseCraw = SseCraw()
        while times > 0:
            self.random_crawl(self.get_data())
            times = times - 1

    def get_data(self, buff_size=10):
        sql = "SELECT * FROM sse.crawl_stat where stat = 'INIT' ORDER BY RAND() LIMIT %d" % buff_size
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def success(self, date, page):
        sql = "UPDATE sse.crawl_stat set stat = 'DONE' where dt = '%s' and page = '%s'" % (date, page)
        print sql
        self.cursor.execute(sql)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
            print "Mysql Wrong"

    def random_crawl(self, table):
        for row in table:
            dt, page, max_page, stat = row
            stat = self.sseCraw.craw_one_page(date=dt, page=page)
            if stat:
                self.success(date=dt, page=page)


if __name__ == '__main__':
    RandomCrawl(1000)
