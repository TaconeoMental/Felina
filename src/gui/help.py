from pathlib import Path

from rich.markdown import Markdown
from textual.screen import Screen
from textual.widgets import Static, Footer
from textual.binding import Binding

class HelpScreen(Screen):
    BINDINGS = [
        Binding("escape,q,question_mark", "app.pop_screen", "Salir de la ayuda")
    ]

    def compose(self):
        help_path = Path(__file__).parent / "felina_help.md"
        help_text = help_path.read_text(encoding="utf-8")
        rendered_help = Markdown(help_text)
        yield Static(rendered_help)
        yield Footer()
