import sys
from selenium import webdriver
from crawler import crawl
from transformer import transToFile

def main(url, parent_selectors, child_link_selector, child_selectors):
    driver = webdriver.Chrome()
    driver.get(url) 

    data = crawl(driver, parent_selectors, child_link_selector, child_selectors)

    transToFile('parent_data.csv', 'child_data.csv', data)

    input("Press ENTER to close the browser")
    driver.quit()

if __name__ == "__main__":
    URL = sys.argv[1]
    parent_selectors = sys.argv[2].split(',')
    child_link_selector = sys.argv[3]
    child_selectors = sys.argv[4].split(',')
    main(URL, parent_selectors, child_link_selector, child_selectors)