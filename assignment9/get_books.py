from selenium.webdriver.common.by import By
from utils import get_driver
import pandas as pd
import json
import time
import os

def task2():
    driver = get_driver()
    driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")

    book_items = driver.find_elements(By.CSS_SELECTOR, "li.row.cp-search-result-item")
    # By.CSS_SELECTOR, "ul.results > li.row.cp-search-result-item"
    print(f"Found {len(book_items)} book entries.")
    results = []

    for item in book_items:
        try:
            # print(item.get_attribute("innerHTML"))
            title = item.find_element(By.CLASS_NAME, "title-content").text
            authors = item.find_elements(By.CLASS_NAME, "author-link")
            author_names = "; ".join([a.text for a in authors])
            format_info = item.find_element(By.CLASS_NAME, "cp-screen-reader-message").text  #display-info-primary

            book_dict = {
                "Title": title,
                "Author": author_names,
                "Format-Year": format_info
            }

            results.append(book_dict)

        except Exception as e:
            print(f"Skipping entry due to error: {e}")

    df = pd.DataFrame(results)

    print(df)

    with open('books.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    driver.quit()

    # Task 4: Write out the Data
    csv_path = os.path.join(".", "get_books.csv")
    df.to_csv(csv_path, index=False)
    print(f"CSV written to: {csv_path}")

    json_path = os.path.join(".", "get_books.json")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"JSON written to: {json_path}")

if __name__ == "__main__":
    task2()