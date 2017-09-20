# -*- coding:UTF-8 -*-
import MySQLdb


class CleanDataDate():
    def __init__(self, dt):
        self.db = MySQLdb.connect("localhost", "root", "root", "sse", charset='utf8')
        self.cursor = self.db.cursor()
        self.clean_data(self.get_data(dt))

    def __del__(self):
        self.cursor.close()
        self.db.close()

    def write_mysql(self, dt, id, name, cnt, money, avg_money, page, max_page, last_page):
        sql = "REPLACE INTO sse.crawl_result(dt, id, name, cnt, money, avg_money, page, max_page, last_page) " \
              "VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                  dt, id, name, cnt, money, avg_money, page, max_page, last_page)
        print sql
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
            print "Mysql Wrong"

    def get_data(self, date='2017-09-01'):
        sql = "select * from sse.ori_crawl_sse where dt >= '%s'" % (date)
        print sql
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def clean_data(self, table):
        for row in table:
            dt, page, max_page, last_page, src = row
            try:
                for double_data in src.split("<tr class=tr_odd data>")[1:]:
                    arr = double_data.split("<tr class=tr_even data>")[0].split("valign=>")
                    id = arr[1].split("</td><td class=")[0]
                    name = arr[2].split("</td>")[0]
                    cnt = (arr[3]).split("</td>")[0]
                    money = (arr[4]).split("</td>")[0]
                    avg_money = (arr[5]).split("</td>")[0]
                    self.write_mysql(dt, id, name, cnt, money, avg_money, page, max_page, last_page)
                    if len(double_data.split("<tr class=tr_even data>")) > 1:
                        arr = double_data.split("<tr class=tr_even data>")[1].split("valign=>")
                        id = arr[1].split("</td><td class=")[0]
                        name = arr[2].split("</td>")[0]
                        cnt = (arr[3]).split("</td>")[0]
                        money = (arr[4]).split("</td>")[0]
                        avg_money = (arr[5]).split("</td>")[0]
                        self.write_mysql(dt, id, name, cnt, money, avg_money, page, max_page, last_page)
            except:
                print "error"
                print src


if __name__ == '__main__':
    date = '2017-09-01'
    cleanDataDate = CleanDataDate(date)
    cleanDataDate.get_data()
