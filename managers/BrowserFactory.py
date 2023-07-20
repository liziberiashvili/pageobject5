from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class BrowserFactory:
    @staticmethod
    def get_browser(browser="chrome"):
        if browser.lower() == "chrome":
            return webdriver.Chrome(ChromeDriverManager().install())
        elif browser == "Safari":
            return webdriver.Safari()
