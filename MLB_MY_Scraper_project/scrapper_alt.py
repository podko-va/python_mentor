from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Настройки браузера
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("user-agent=Mozilla/5.0")

# Запуск драйвера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 10)

# Данные для сохранения
college_links = []
results = []

try:
    # Шаг 1: Получение списка колледжей
    base_url = "https://www.baseball-almanac.com/college/colleges_sort_quantity.shtml"
    driver.get(base_url)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "table")))

    rows = driver.find_elements(By.TAG_NAME, "tr")[1:]  # Пропускаем заголовок

    for row in rows:
        try:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) >= 2:
                link_el = cells[0].find_element(By.TAG_NAME, "a")
                college_link = link_el.get_attribute("href")
                title = cells[0].text.strip()
                college_name = title.split("|")[0].strip()
                college_qty = cells[1].text.strip()
                college_links.append((college_name, college_qty, college_link))
        except Exception as e:
            print(f"⚠️ Skipping college row due to error: {e}")

    # Ограничение на количество колледжей для теста (снимай ограничение при финальном запуске)
    college_links = college_links[:30]

    # Шаг 2: Парсинг игроков с каждой страницы колледжа
    for college_name, college_qty, college_url in college_links:
        try:
            print(f"🔍 Scraping: {college_name} ({college_qty} players)")
            driver.get(college_url)
            time.sleep(2)  # Пауза для полной загрузки и избежания блокировки

            table = wait.until(EC.presence_of_element_located((By.TAG_NAME, "table")))
            player_rows = table.find_elements(By.TAG_NAME, "tr")[1:]  # Пропускаем заголовок

            for row in player_rows:
                try:
                    cells = row.find_elements(By.TAG_NAME, "td")
                    if len(cells) >= 3:
                        player_name = cells[1].text.strip()
                        if not player_name:
                            continue
                        years_raw = cells[2].text.strip()
                        if "-" in years_raw:
                            end_year = years_raw.split("-")[-1].strip()
                        else:
                            end_year = years_raw[-4:]  # Если формат другой, берём последние 4 символа
                        results.append([college_name, college_qty, player_name, end_year])
                except Exception as e:
                    print(f"⚠️ Skipping player row: {e}")
        except Exception as e:
            print(f"❌ Could not scrape {college_name}: {e}")

finally:
    driver.quit()

# Шаг 3: Сохранение в CSV
try:
    df = pd.DataFrame(results, columns=["College", "Players Qty", "Player", "End Year"])
    df.to_csv("my_mlb_data.csv", index=False, encoding="utf-8")
    print("✅ Data saved to my_mlb_data.csv")
except Exception as e:
    print(f"❌ Error saving file: {e}")
