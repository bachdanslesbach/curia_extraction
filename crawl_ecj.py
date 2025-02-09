from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import csv
import time
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://curia.europa.eu/juris/liste.jsf"
CSV_FILE = "links.csv"
DELAY = 0.5
PAGES_TO_SCRAPE = 5041  # Test with 5 pages first

def scrape_links(driver):
    links = []
    spans = driver.find_elements(By.CSS_SELECTOR, 'span.decision_links a[href]')  # Corrected selector
    for span in spans:
        links.append(span.get_attribute('href'))
    return links

def main():
    options = webdriver.ChromeOptions()
    # Remove "--headless" temporarily to debug and see the browser
    # options.add_argument("--headless")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(BASE_URL)

    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Decision Link"])

        for _ in range(PAGES_TO_SCRAPE):
            # Wait for links to load (add explicit wait)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'span.decision_links a[href]'))
            )
            links = scrape_links(driver)
            for link in links:
                writer.writerow([link])
            print(f"Scraped {len(links)} links from page.")

            try:
                next_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "mainForm:j_id458"))
                )
                next_button.click()
                time.sleep(DELAY)
            except (NoSuchElementException, TimeoutException) as e:
                print("Next page button not found. Exiting.")
                break

    driver.quit()

if __name__ == "__main__":
    main()