from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


DELAY_SECONDS = 15


def get_driver():
    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    # WebDriver location hardcoded. Matches location set in Dockerfile.
    return webdriver.Chrome("./chromedriver", options=opts)


def element_by_id(driver, id):
    return WebDriverWait(driver, DELAY_SECONDS).until(
        EC.presence_of_element_located((By.ID, id))
    )


def element_by_css(driver, selector, multiple=False):
    # Wait until one occurence is found.
    found = WebDriverWait(driver, DELAY_SECONDS).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, selector))
    )

    # If we want multiple, re-scan the document now it has loaded.
    return driver.find_elements_by_css_selector(selector) if multiple else found
