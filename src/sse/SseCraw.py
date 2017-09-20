# -*- coding:UTF-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import MySQLdb
import re
import sys

reload(sys)
sys.setdefaultencoding('utf8')


def log_dump(**kwargs):
    for k in kwargs.keys():
        print k + " ==> " + str(kwargs[k])


class SseCraw():
    def __init__(self):
        self.driver = webdriver.PhantomJS()
        self.db = MySQLdb.connect("localhost", "root", "root", "sse", charset='utf8')
        self.cursor = self.db.cursor()

    def __del__(self):
        self.cursor.close()
        self.db.close()

    def write_mysql(self, dt, page, max_page, last_page, src):
        log_dump(dt=dt, page=page, max_page=max_page, last_page=last_page, src=src)
        print src
        sql = "REPLACE INTO sse.ori_crawl_sse(dt, page, max_page, last_page, src) VALUES('%s','%s','%s','%s','%s')" % (
            dt, page, max_page, last_page, src.replace('"', ''))
        print sql
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
            print "Mysql Wrong"
            return False
        return True

    def craw_first_page(self, date="2017-09-13"):
        driver = self.driver
        driver.get('http://bond.sse.com.cn/data/statistics/survey/single/')
        js_str = "a = document.getElementById('sDate');" \
                 "a.removeAttribute('readonly','');" \
                 "a.value='%s';" \
                 "e = document.getElementsByClassName('search-btn');" \
                 "e[0].click();" % date

        driver.execute_script(js_str)
        driver.implicitly_wait(5)
        try:
            driver.find_element_by_class_name("td_content_right")
        except:
            return "notcraw"
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        trade_info = soup.find_all('span', {'id': 'staticDate'})
        if len(trade_info) > 0:
            titles = soup.find_all('table', {'class': 'bond_details_table'})
            if len(titles) > 0:
                return titles[0]
        return "notcraw"

    def craw_all_page(self, date="2017-09-04"):
        print "start run===>" + date
        driver = self.driver
        driver.get('http://bond.sse.com.cn/data/statistics/survey/single/')
        js_str = "a = document.getElementById('sDate');" \
                 "a.removeAttribute('readonly','');" \
                 "a.value='%s';" \
                 "e = document.getElementsByClassName('search-btn');" \
                 "e[0].click();" % date
        driver.execute_script(js_str)
        driver.implicitly_wait(10)
        while True:
            driver.implicitly_wait(10)
            try:
                driver.find_element_by_class_name("td_content_right")
            except:
                return False
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            titles = soup.find_all('table', {'class': 'bond_details_table'})
            if len(titles) > 0:
                page_raw = soup.find_all('span', {'class': 'paging_input'})
                page_num_on_raw = soup.find_all('span', {'class': 'paging_num_on'})
                if len(page_raw) > 0:
                    max_page = re.compile('(\d+)').findall(str(page_raw[0]))[0]
                    page_num_on = re.compile('(\d+)').findall(str(page_num_on_raw[0]))[0]
                    last_page = 0
                    if max_page == page_num_on:
                        last_page = 1
                    self.write_mysql(dt=date, page=page_num_on, max_page=max_page,
                                     last_page=last_page, src=str(titles[0]))
                    if max_page == page_num_on:
                        return True
                    if max_page < page_num_on:
                        return False
                    driver.find_element_by_id("dateList_container_next").click()
                    continue
            return False
        return False

    def craw_one_page(self, date="2017-09-04", page=5):
        driver = self.driver
        driver.get('http://bond.sse.com.cn/data/statistics/survey/single/')
        js_str = "a = document.getElementById('sDate');" \
                 "a.removeAttribute('readonly','');" \
                 "a.value='%s';" \
                 "e = document.getElementsByClassName('search-btn');" \
                 "e[0].click();" % date
        driver.execute_script(js_str)
        driver.implicitly_wait(10)
        try:
            driver.find_element_by_class_name("td_content_right")
        except:
            return False
        js_str = "a = document.getElementById('dateList_container_pageid');" \
                 "a.value='%s';" \
                 "e = document.getElementById('dateList_container_togo');" \
                 "e.click();" % page
        driver.execute_script(js_str)
        try:
            driver.find_element_by_class_name("td_content_right")
        except:
            return False
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        titles = soup.find_all('table', {'class': 'bond_details_table'})
        print titles[0]
        if len(titles) > 0:
            page_raw = soup.find_all('span', {'class': 'paging_input'})
            page_num_on_raw = soup.find_all('span', {'class': 'paging_num_on'})
            print str(page_raw)
            if len(page_raw) > 0:
                max_page = re.compile('(\d+)').findall(str(page_raw[0]))[0]
                page_num_on = re.compile('(\d+)').findall(str(page_num_on_raw[0]))[0]
                last_page = 0
                if max_page == page_num_on:
                    last_page = 1
                stat = self.write_mysql(dt=date, page=page_num_on, max_page=max_page,
                                        last_page=last_page, src=str(titles[0]))
                return stat
        return False


if __name__ == '__main__':
    #sse = SseCraw()
    #sse.craw_all_page("2017-09-01")
    print SseCraw().craw_one_page(date="2017-06-18", page=2)
