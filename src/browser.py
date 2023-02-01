from enum import Enum
import os.path as path
from urllib.parse import urlparse

from seleniumwire import webdriver
from selenium.webdriver.firefox.options import Options

from src.utils import get_script_path


class BrowserType(Enum):
    FIREFOX = 0x00
    CHROME = 0x01


class Browser:
    def __init__(self, config):
        self.browser_type = config.browser_type
        self.profile_dir = config.browser_profile_dir
        self.log_level = config.selenium_log_level
        self.driver = self.new_wd()

    def open(self, url=None):
        if not url:
            default_page_path = path.join(get_script_path(), "assets", "default_page.html")
            url = f"file://{default_page_path}"
        self.driver.get(url)

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
        raise NotImplementedError("Chrome browser support not implemented yet")

    def get_network_log(self):
        urls = [request.url for request in self.driver.requests if
                request.response and request.response.status_code == 200]
        return urls

    def get_js_files(self):
        js_files = filter(lambda u: urlparse(u).path.endswith(".js"), self.get_network_log())
        return list(js_files)
