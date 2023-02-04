from pathlib import Path

from rich.syntax import Syntax
from textual.binding import Binding
from textual.widgets import Static


class Viewer(Static):
    BINDINGS = [
        Binding("j", "down", "Down", key_display="j"),
        Binding("k", "up", "Up", key_display="k")
    ]

    def __init__(self, name=None, id=None, classes=None):
        super().__init__(name=name, id=id, classes=classes)
        self.show_syntax("console.log('hola')")

    def show_syntax(self, code):
        self.update(
            Syntax(
                code,
                "javascript",
                line_numbers=True,
                indent_guides=True,
            )
        )
