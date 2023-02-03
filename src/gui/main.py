from textual.binding import Binding
from textual.containers import Horizontal, Container
from textual.screen import Screen
from textual.widgets import Header, Footer

from .viewer import Viewer

class MainScreen(Screen):
    BINDINGS = [
        Binding("question_mark", "app.push_screen('help')", "Ayuda"),
        Binding("ctrl+x", "quit", "Salir", key_display="ctrl+x")
    ]

    def compose(self):
        yield Header()
        yield Horizontal(
            Container(Viewer(id="viewer"))
        )
        yield Footer()
