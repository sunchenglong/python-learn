# -*- coding:UTF-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import re


class SseCraw():
    def __init__(self):
        self.driver = webdriver.PhantomJS()

    def log_dump(self, *args, **kwargs):
        for k in kwargs.keys():
            print k + " ==> " + str(kwargs[k])

    def write_mysql(self, dt, page, max_page, last_page, src):
        self.log_dump(dt=dt, page=page, max_page=max_page, last_page=last_page, src=src)

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
            if self.trade_day_verify(date, str(trade_info[0])):
                titles = soup.find_all('table', {'class': 'bond_details_table'})
                if len(titles) > 0:
                    return titles[0]
        return "notcraw"

    def craw_all_page(self, date="2017-09-13"):
        driver = self.driver
        driver.get('http://bond.sse.com.cn/data/statistics/survey/single/')
        js_str = "a = document.getElementById('sDate');" \
                 "a.removeAttribute('readonly','');" \
                 "a.value='%s';" \
                 "e = document.getElementsByClassName('search-btn');" \
                 "e[0].click();" % date
        driver.execute_script(js_str)
        driver.implicitly_wait(5)
        while (True):
            try:
                driver.find_element_by_class_name("td_content_right")
            except:
                return False
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            trade_info = soup.find_all('span', {'id': 'staticDate'})
            if len(trade_info) > 0:
                titles = soup.find_all('table', {'class': 'bond_details_table'})
                if len(titles) > 0:
                    page_raw = soup.find_all('span', {'class': 'paging_input'})
                    page_num_on_raw = soup.find_all('span', {'class': 'paging_num_on'})
                    print str(page_raw)
                    if len(page_raw) > 0:
                        max_page = re.compile('(\d+)').findall(str(page_raw[0]))[0]
                        page_num_on = re.compile('(\d+)').findall(str(page_num_on_raw[0]))[0]
                        last_page = 0
                        self.write_mysql(dt=date, page=page_num_on, max_page=max_page,
                                         last_page=last_page, src=str(titles[0]))
                        if max_page == page_num_on:
                            last_page = 1
                            return True
                        if max_page < page_num_on:
                            return False
                        driver.find_element_by_class_name("paging_next").click()
                        continue
                return False
        return False


if __name__ == '__main__':
    SseCraw().craw_all_page()
