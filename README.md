# Curia case files links scraper

This Python script uses Selenium to scrape links to case files in the European Court of Justice ("ECJ", or "Curia" - "curia.europa.eu") website and saves them into a CSV file. It automates the process of navigating through multiple pages and extracting the relevant links.

## Features

- Automatically navigates through multiple pages of the Curia website.
- Extracts decision links and saves them into a CSV file.
- Handles pagination and waits for elements to load properly.
- Configurable number of pages to scrape.

## Requirements

- Python 3.x
- Libraries: `selenium`, `webdriver_manager`

You can install the required libraries using pip:

```bash
pip install selenium webdriver_manager
```

Additionally, you need to have Chrome browser installed on your system.

## Usage

1. **Prepare Your Environment**:
   - Ensure you have Chrome browser installed.
   - Install the required Python libraries.

2. **Run the Script**:
   - Execute the script using Python:

     ```bash
     python scrape_curia.py
     ```

3. **Output**:
   - The script will generate a CSV file named `links.csv` in the same directory.
   - The CSV file will contain a list of decision links scraped from the Curia Europa website.

## How It Works

1. **Initialize WebDriver**:
   - The script sets up a Selenium WebDriver using Chrome.
   - It navigates to the base URL of the Curia Europa website.

2. **Scrape Links**:
   - The script waits for the decision links to load on each page.
   - It extracts the links using a CSS selector and saves them into a CSV file.

3. **Handle Pagination**:
   - The script clicks the "Next" button to navigate through pages.
   - It handles exceptions if the "Next" button is not found, indicating the end of pagination.

4. **Configurable Parameters**:
   - You can configure the number of pages to scrape by changing the `PAGES_TO_SCRAPE` variable.
   - Adjust the `DELAY` variable to control the waiting time between page navigations.

## Notes

- The script is set to scrape 5041 pages by default. You can test with a smaller number of pages by modifying the `PAGES_TO_SCRAPE` variable.
- The script uses an explicit wait to ensure that elements are loaded before interacting with them.
- Uncomment the `--headless` option in the `webdriver.ChromeOptions()` to run the browser in headless mode for faster execution without a UI.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

This README provides a clear overview of your script's functionality and how to use it. You can customize it further based on your specific needs or additional features you might add in the future.
