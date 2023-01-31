#!/usr/bin/env python3

import argparse
import sys

from src.config import FelinaConfig
from src.browser import BrowserType
from src.main import Felina

def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-u", "--user-data-dir", default=None)
    argparser.add_argument("-c", "--chrome", action="store_true")
    parsed_args = argparser.parse_args()

    felina_config = FelinaConfig()
    felina_config.browser_profile_dir = parsed_args.user_data_dir

    if parsed_args.chrome:
        felina_config.browser_type = BrowserType.CHROME
    else:
        felina_config.browser_type = BrowserType.FIREFOX

    felina_app = Felina(felina_config)
    felina_app.run()


if __name__ == '__main__':
    main()
