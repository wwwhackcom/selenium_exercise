from selenium import webdriver

def crawl(driver: webdriver.Chrome):
    data = driver.page_source
    return data