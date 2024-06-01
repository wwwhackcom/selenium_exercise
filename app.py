import sys
from selenium import webdriver

def main(url):
    driver = webdriver.Chrome()
    driver.get(url) 
    input("Press ENTER to close the browser")
    driver.quit()

if __name__ == "__main__":
    URL = sys.argv[1]
    main(URL)