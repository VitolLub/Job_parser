#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Lubomir Vitol"
__copyright__ = "Copyright 2022, Planet Earth"

import time

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

URL = "https://www.helmholtz.de/en/search/jobs/"
PAGE = 42

title_arr = []
position_arr = []
company_name = []
location_arr = []
link_arr = []

def run_browser():
    options = Options()
    #options.add_argument("--headless")
    #options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome('chromedriver.exe',options=options)
    driver.get(URL)
    return driver


def accept_cookies(driver):
    driver.find_element(By.XPATH,"//button[@class='btn btn--primary cookiebanner__close']").click()
    return driver

def goto(driver, page):
    driver.get(URL+"/?search[page]="+str(page))
    time.sleep(2)
    # parse data from currect page
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    div = soup.find('div', {'class': 'list'})
    try:
        li = div.find_all('li')
        # get all titles
        for every in li:
            for index in range(1,6):
                # get all job titles
                class_type = 'class'
                tag_name = 'span'
                data_type = index
                class_name = 'list__label'
                parser(every,class_type, tag_name, class_name, data_type)
    except Exception as e:
        print(e)

def parser(div,class_type, tag_name, class_name, data_type):
    if data_type == 1:
        try:
            position = div.find_all('span', {'class': 'list__label'})
            for pos in position:
                position_arr.append(pos.text)
        except Exception as e:
            position_arr.append("")
    if data_type == 2:
        try:
            title = div.find_all('a')
            for t in title:
                title_arr.append(t.text)
        except:
            title_arr.append("")
    if data_type == 4:

            location = div.find_all('p')
            for index,l in enumerate(location):
                print(index)
                print(l.text)
                try:
                    if index==1:
                        company_name.append(l.text)
                    if index==2:
                        location_arr.append(l.text)
                except:
                    company_name.append("")
                    location_arr.append("")
    if data_type == 5:
        try:
            link = div.find_all('a', {'class': 'btn btn--flat btn--icon-right'})
            for l in link:
                link_arr.append(l['href'])
        except:
            link_arr.append("")
    return div

if __name__ == '__main__':
    driver = run_browser()
    driver = accept_cookies(driver)
    time.sleep(3)
    for i in range(1,PAGE):
        try:
            goto(driver,i)
        except Exception as e:
            print(e)

    print(position_arr)
    print(len(position_arr))
    print(title_arr)
    print(len(title_arr))
    print(link_arr)
    print(len(link_arr))
    print(company_name)
    print(len(company_name))
    print(location_arr)
    print(len(location_arr))