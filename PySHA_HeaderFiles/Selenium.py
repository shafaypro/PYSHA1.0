import selenium
from selenium import webdriver

if __name__ == '__main__':
    browser  = webdriver.Chrome(executable_path="C:\Chrome\\")
    browser.get('https://www.hotmail.com')
    browser.wait(30)
    browser.quit()