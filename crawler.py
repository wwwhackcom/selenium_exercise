from selenium import webdriver

def crawl(driver: webdriver.Chrome, parent_selectors, child_link_selector, child_selectors):
    parent_data = [element.text for selector in parent_selectors for element in driver.find_elements_by_css_selector(selector)]

    child_page_link = driver.find_element_by_css_selector(child_link_selector).get_attribute('href')
    driver.get(child_page_link)

    child_data = [element.text for selector in child_selectors for element in driver.find_elements_by_css_selector(selector)]

    return parent_data, child_data