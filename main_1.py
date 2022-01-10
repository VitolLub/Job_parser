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


URL = "https://www.fernuni-hagen.de/uniintern/arbeitsthemen/karriere/stellen/index.shtml"

title_arr = []
position_arr = []
application_arr = []
link_arr = []

def start():
    options = Options()
    # options.add_argument("--headless")
    # options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome('chromedriver.exe', options=options)
    driver.get(URL)
    time.sleep(5)
    return driver


def click_buttom(driver):
    try:
        driver.find(By.XPATH,"//h3[@class='acc_head']").click()
    except:
        print("No more pages")

    return driver


def grab(driver):
    iframe = driver.find_element(By.XPATH, "//iframe[@src='https://fernuni-hagen.hr4you.org/job_liste_extern.php']")
    # get src of iframe
    driver.switch_to.frame(iframe)
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup)
    # # find the div with the class "content"
    # find all td class "jobListData"
    jobListData = soup.find_all("tr", {'class': "jobListData"})
    for jobs in jobListData:
        tds = jobs.find_all("td")
        for index, td in enumerate(tds):
            try:
                link_arr.append(td.find("a")['href'])
            except:
                print("No href")
            if index == 0:
                # print(td)
                # split the string

                res = td.text.split("\n\n")
                # print(res)
                title_arr.append(res[1].strip())
                position_arr.append(res[2].strip())
            elif index == 1:
                date = td.text
                application_arr.append(date.strip())
    return driver


if __name__ == '__main__':
    driver = start()
    # receive the html of the page
    # receive data
    driver = click_buttom(driver)
    time.sleep(5)
    driver = grab(driver)
    driver.close()

    print(title_arr)
    print(len(title_arr))
    print(link_arr)
    print(len(link_arr))
    print(position_arr)
    print(len(position_arr))
    print(application_arr)
    print(len(application_arr))

