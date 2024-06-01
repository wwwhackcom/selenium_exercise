import sys
from selenium import webdriver
import crawler
import transformer

def main(url):
    driver = webdriver.Chrome()
    driver.get(url)
    transformer.transToFile("output.txt", crawler.crawl(driver))
    input("Press ENTER to close the browser")
    driver.quit()

if __name__ == "__main__":
    URL = sys.argv[1]
    main(URL)