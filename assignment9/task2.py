from selenium.webdriver.common.by import By
from utils import get_driver

def task2():
    driver = get_driver()
    driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")

    book_items = driver.find_elements(By.CSS_SELECTOR, "li.row.cp-search-result-item")
    # By.CSS_SELECTOR, "ul.results > li.row.cp-search-result-item"

    for item in book_items:
        try:
            # print(item.get_attribute("innerHTML"))
            title = item.find_element(By.CLASS_NAME, "title-content").text
            authors = item.find_elements(By.CLASS_NAME, "author-link")
            author_names = [a.text for a in authors]
            format_info = item.find_element(By.CLASS_NAME, "display-info-primary").text

            print(f"Title: {title}")
            print(f"Author(s): {', '.join(author_names)}")
            print(f"Format and Year: {format_info}")
            print("-" * 40)
            print(title)
        except:
            continue