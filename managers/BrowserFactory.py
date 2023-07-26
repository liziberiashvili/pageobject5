from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class BrowserFactory:
    @staticmethod
    def get_browser(browser="chrome"):
        if browser.lower() == "chrome":
            return webdriver.Chrome()
        elif browser == "Safari":
            return webdriver.Safari()
