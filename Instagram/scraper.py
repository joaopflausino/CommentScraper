import time
import re
from selenium.webdriver.common.by import By

def get_post_id(url):
    pattern = r"\/p\/([A-Za-z0-9_-]+)\/"
    match = re.search(pattern, url)
    return match.group(1) if match else None

def load_comments(driver, url):
    driver.get(url)
    time.sleep(5)
    while True:
        try:
            load_more_button = driver.find_element(By.CSS_SELECTOR, "button._abl-")
            load_more_button.click()
            time.sleep(2)
        except:
            break

    comment_spans = driver.find_elements(By.XPATH, "//span[contains(@style, '--base-line-clamp-line-height: 18px')]")
    return [span.text for span in comment_spans]

def scrape_comments(driver, url):
    post_id = get_post_id(url)
    comments = load_comments(driver, url)
    return comments, post_id