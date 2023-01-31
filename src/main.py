from src.browser import Browser

def process_browser_log_entry(entry):
    response = json.loads(entry['message'])['message']
    return response

class Felina:
    def __init__(self, config):
        self.config = config
        self.browser = Browser(config)

    def run(self):
        self.browser.driver.get("https://stderr.cl")
        for request in self.browser.driver.requests:
            if request.response:
                print(
                    request.url,
                    request.response.status_code,
                    request.response.headers['Content-Type']
                )
