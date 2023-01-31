from enum import Enum

from seleniumwire import webdriver
from selenium.webdriver.firefox.options import Options

class BrowserType(Enum):
    FIREFOX = 0x00
    CHROME = 0x01

class Browser:
    def __init__(self, config):
        self.browser_type = config.browser_type
        self.profile_dir = config.browser_profile_dir
        self.log_level = config.selenium_log_level
        self.driver = self.new_wd()

    def new_wd(self):
        match self.browser_type:
            case BrowserType.FIREFOX:
                return self.to_firefox_wd()
            case BrowserType.CHROME:
                return self.to_chrome_wd()

    def to_firefox_wd(self):
        profile = None
        if self.profile_dir:
            profile = webdriver.FirefoxProfile(self.profile_dir)

        options = Options()
        options.add_argument(f"--log-level={self.log_level}")

        return webdriver.Firefox(firefox_profile=profile, options=options)

    def to_chrome_wd(self):
        # TODO
        pass
