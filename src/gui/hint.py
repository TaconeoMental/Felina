from textual.containers import Container
from textual.widgets import Static

class Hint(Static):
    def __init__(
        self,
        title,
        description="",
        name=None,
        id=None,
        classes=None
    ):
        super().__init__(name=name, id=id, classes=classes)
        self.title = title
        self.description = description

    def compose(self):
        yield Static(self.title, id="hint-title")
        yield Static(self.description)

class HintList(Static):
    def compose(self):
        yield Container(id="hint-list-container")

    def add_hint(self):
        new_hint = Hint("Default Title")
        self.query_one("#hint-list-container", Container).mount(new_hint)
        new_hint.scroll_visible()
