from textual.screen import Screen
from textual.widgets import Header, Footer

class MainScreen(Screen):
    def compose(self):
        yield Header()
        yield Footer()
