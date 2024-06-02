import sys
import json
from selenium import webdriver
import crawler
from transformer import transToFile

def main(url):
    driver = webdriver.Chrome()
    driver.get(url)
    ids = crawler.crawl_pagination(driver)
    print(ids)
    with open('ids.json', 'w') as f:
        json.dump(ids, f)
    input("Press ENTER to close the browser")
    driver.quit()

if __name__ == "__main__":
    URL = sys.argv[1]
    main(URL)