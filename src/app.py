from contextlib import contextmanager, redirect_stdout, redirect_stderr
from pathlib import Path
import sys

from textual.app import App

from src.gui import MainScreen, HelpScreen


class Felina(App):
    CSS_PATH = Path(__file__).parent / "gui" / "felina.css"
    SCREENS = {
        "main": MainScreen,
        "help": HelpScreen,
        #"tutorial": TutorialScreen
    }

    BINDINGS = []

    def on_mount(self):
        self.push_screen("main")

    @contextmanager
    def suspend(self):
        driver = self._driver
        if driver is not None:
            driver.stop_application_mode()
            with redirect_stdout(sys.__stdout__), redirect_stderr(sys.__stderr__):
                yield
            driver.start_application_mode()
