# -*- coding:UTF-8 -*-
import MySQLdb


class GenStat():
    def __init__(self):
        self.db = MySQLdb.connect("localhost", "root", "root", "sse", charset='utf8')
        self.cursor = self.db.cursor()
        self.gen_mission(self.get_data())

    def __del__(self):
        self.cursor.close()
        self.db.close()

    def write_mysql(self, dt, page, max_page):
        sql = "REPLACE INTO sse.crawl_stat(dt, page, max_page, stat) " \
              "VALUES('%s','%s','%s','%s')" % (
                  dt, page, max_page, "INIT")
        print sql
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
            print "Mysql Wrong"

    def get_data(self):
        sql = "select distinct dt,max_page from sse.ori_crawl_sse"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def gen_mission(self, table):
        for row in table:
            dt, max_page = row
            for page in range(1, max_page + 1):
                self.write_mysql(dt, page, max_page)


if __name__ == '__main__':
    genStat = GenStat()
