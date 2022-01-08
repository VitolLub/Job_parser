#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__      = "Lubomir Vitol"
__copyright__   = "Copyright 2022, Planet Earth"

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

url = "https://www.helmholtz.de/en/search/jobs/"

