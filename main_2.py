# Import any WebDriver class that you would usually import from
# selenium.webdriver from the seleniumrequests module
import time
from selenium import webdriver
from seleniumrequests import Firefox,Chrome
# More complex usage, using a WebDriver from another Selenium-related module:
from seleniumrequests.request import RequestMixin
# Simple usage with built-in WebDrivers:
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://uni-bayreuth.de/en/job-vacancies"

title_arr = []
position_arr = []
application_arr = []
location_arr = []
link_arr = []


def start():
    options = Options()
    # options.add_argument("--headless")
    # options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome('chromedriver.exe', options=options)
    driver.get(URL)
    time.sleep(20)
    return driver


def str_to_soup(response):
    #print(response.page_source)
    soup = BeautifulSoup(response.page_source, 'html.parser')
    return soup


def acept_cokies(driver):
    # click by text "Accept All"
    button = driver.find_element_by_link_text("Accept All")
    button.click()
    return driver
    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//button[@class="sc-gsTEea encHZb"]'))).click()
    # return driver

def grab_title(div_col_12):
    # find all h3
    h3 = div_col_12.find_all('h3')
    #print(len(h3))
    if len(h3) > 0:
        for h in h3:
            title_arr.append(h.text)


def grab_position_arr(col_12):
    positions = col_12.find_all('span',{'class':'jobElementHeadline--F1udsUrIzp'})
    #print(len(positions))
    if len(positions) > 0:
        for position in positions:
            position_arr.append(position.text)


def grab_application_name(col_12):
        application  = col_12.find_all('a', {'class': 'jobElement--wmPg9KmqC9'})
        for app in application:
            try:
                h3 = app.find('p',{'class':'jobElementDate--o8uhBPaHYk'})
                application_arr.append(h3.text)
            except:
                print("error")
                application_arr.append("")


def grab_link_arr(col_12):
    links = col_12.find_all('a', {'class': 'jobElement--wmPg9KmqC9'})
    #print(len(links))
    if len(links) > 0:
        for link in links:
            link_arr.append(link.get('href'))


if __name__ == '__main__':
    driver = start()
    #driver = acept_cokies(driver)

    soup = str_to_soup(driver)

    # fild all elements
    div_col_12 = soup.find_all('div', {'class':'col-12'})
    for col_12 in div_col_12:
        #print(col_12)
        h3 = col_12.find_all('h3')
        #print(len(h3))
        if len(h3) > 0:
            grab_position_arr(col_12)
            grab_application_name(col_12)
            grab_link_arr(col_12)
            grab_title(col_12)
            break

    driver.close()
    # prepear title
    print(title_arr)
    print(len(title_arr))
    print(link_arr)
    print(len(link_arr))
    print(position_arr)
    print(len(position_arr))
    print(application_arr)
    print(len(application_arr))



