from selenium.webdriver.common.by import By
from utils import get_driver

def task1():
    driver = get_driver()
    driver.get("https://durhamcountylibrary.org/robots.txt")
    print(driver.page_source)
    driver.quit()