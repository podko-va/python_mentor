from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import pandas as pd
import json
import time
import os



options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--window-size=1920x1080")
    
driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )

driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")

look_items = driver.find_elements(By.CSS_SELECTOR, "li.row.cp-search-result-item")
    # By.CSS_SELECTOR, "ul.results > li.row.cp-search-result-item"
for item in look_items:
        try:
            # print(item.get_attribute("innerHTML"))
            title = item.find_element(By.CLASS_NAME, "title-content").text
            authors = item.find_elements(By.CLASS_NAME, "author-link")
            author = [a.text for a in authors]
            # author_names = "; ".join([a.text for a in authors])
            format_info = item.find_element(By.CLASS_NAME, "display-info-primary").text  #display-info-primary

            # book_dict = {
            #     "Title": title,
            #     "Author": author_names,
            #     "Format-Year": format_info
            # }
            print(title)
            print(author)
            print(format_info)
        except Exception as e:
            print(f"Skipping entry due to error: {e}")