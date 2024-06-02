from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from fake_useragent import UserAgent

def preCrawl(driver: webdriver.Chrome):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'itemPerPageDropdown')))

def crawl_pagination(driver: webdriver.Chrome):
    all_ids = []
    while True:
        preCrawl(driver)
        ids = crawl_all_ids(driver)
        all_ids.extend(ids)

        navigate_to_next_page(driver)

        if check_if_last_page(driver):
            break

    return all_ids

def crawl_all_ids(driver: webdriver.Chrome):
    ids = []
    grid_items = driver.find_elements(By.CSS_SELECTOR, '.grid-row .grid-item')
    for item in grid_items:
        ids.append(list_all_links(item))
    return ids


def list_all_links(item):
    anchor_elements = item.find_elements(By.TAG_NAME, 'a')
    for anchor in anchor_elements:
        href_link = anchor.get_attribute('href')

        if href_link:
            return href_link.split('=')[-1]

def navigate_to_next_page(driver: webdriver.Chrome):
    wait = WebDriverWait(driver, 3)
    next_page_element = wait.until(EC.element_to_be_clickable((By.ID, 'nextPage')))
    next_page_element.click()

def check_if_last_page(driver: webdriver.Chrome):
    wait = WebDriverWait(driver, 3)
    next_page_element = wait.until(EC.element_to_be_clickable((By.ID, 'nextPage')))
    return not next_page_element.is_enabled()

def debug_clickable(driver, element):
    sub_items = element.find_elements(By.XPATH, './/*')
    print(f'sub_items count = {len(sub_items)}')
    for sub_item in sub_items:
        try:
            name = sub_item.tag_name
            type = sub_item.get_attribute('type')
            wait = WebDriverWait(driver, 1)
            clickable_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.js-adobe-tracking')))
            print(f'The element {name} - {type} is clickable.')
        except TimeoutException:
            print(f'The element {name} - {type} is not clickable.')

def navigate_to_sub_page(driver: webdriver.Chrome, element):
    href_link = element.get_attribute('href')
    print(href_link)

    if href_link:
        driver.get(href_link)
    else:
        print('No href attribute found on the element.')

def crawl_detail(driver: webdriver.Chrome):
    next_element = driver.find_element(By.XPATH, '//a[contains(text(), "networking")]/following::a[1]')
    product_type = next_element.text
    print(product_type)

    product_name_element = driver.find_element(By.XPATH, '//td[text()="Product Name"]/following-sibling::td')
    product_name = product_name_element.text
    print(product_name)

    description_element = driver.find_element(By.XPATH, '//div[@id="collapseZero"]//div[@class="font-14 margin-top-sm"]')
    description = description_element.text
    print(description)

    data_dict = {
        "Product Name": product_name,
        "Product Type": product_type,
        "Description": description
    }

    return data_dict