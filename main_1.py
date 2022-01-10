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
        driver.find(By.XPATH,"//button[@id='button_10_14_0_0']").click()
    except:
        print("No more pages")

    return driver


if __name__ == '__main__':
    driver = start()
    # receive the html of the page
    # receive data
    driver = click_buttom(driver)
    html = driver.page_source
    # html = driver.page_source
    # parse the html
    soup = BeautifulSoup(html, 'html.parser')
    # find the div with the class "content"
    content = soup.find_all(By.XPATH, "//table[@id='stellenangebote']")
    for i in content:
        # find the title
        titles = i.find_all(By.XPATH, "//tr[@class='jobListData']")
        for j in titles:
            print(j.text)

