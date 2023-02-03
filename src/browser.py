from enum import Enum
from pathlib import Path
from urllib.parse import urlparse

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
        self.driver = self.get_driver()

    def open(self, url=None):
        if not url:
            default_page_path = Path(__file__).parent / "assets" / "default_page.html"
            url = f"file://{default_page_path}"
        self.driver.get(url)

    def get_driver(self):
        match self.browser_type:
            case BrowserType.FIREFOX:
                return self._get_firefox_driver()
            case BrowserType.CHROME:
                return self._get_chrome_driver()

    def _get_firefox_driver(self):
        # TODO: Explicar por qué tengo que hacer el truquito
        profile = None
        if self.profile_dir:
            profile = webdriver.FirefoxProfile(self.profile_dir)

        # Truquito owowowo
        options = Options()
        options.add_argument(f"--log-level={self.log_level}")

        return webdriver.Firefox(firefox_profile=profile, options=options)

    def _get_chrome_driver(self):
        raise NotImplementedError("Chrome browser support not implemented yet")

    def get_network_log(self):
        # Por qué hacerlo ordenado si puedo hacer una list comprehension
        # ordinaria y fea?
        urls = [request.url for request in self.driver.requests if
                request.response and request.response.status_code == 200]
        return urls

    def get_js_files(self):
        # Feo pq si
        js_files = filter(
            lambda u: urlparse(u).path.endswith(".js"),
            self.get_network_log()
        )
        return list(js_files)
