from textual.binding import Binding
from textual.containers import Container
from textual.widgets import Static, Widget

"""
Idea para implementar dsps porque es tarde:
1. Que cada elemento del árbol sea un widget en sí.
Además, que tenga una acción para abrir o cerrar el detalle.
"""


class TreeViewItem(Static):

    # Aún no sé qué parámetros recibe esta función porque no sé cómo voy a
    # ordenar los datos. Probablemente sea un json pero queda como TODO
    def __init__(
            self,
            domain,
            files=None,
            name=None,
            id=None,
            classes=None
    ):
        super().__init__(name=name, id=id, classes=classes)
        self.open = False
        self.domain = domain
        if not files:
            files = list()
        self.files = files

    def compose(self):
        pass

    # O tal vez implementar render() para devolver un rich renderable tipo:
    # """
    # [bold]| DOMAIN
    # [bold pink]\ FILE.js
    # [bold pink]\ FILE.js
    # """


class TreeView(Widget, can_focus=True):

    BINDINGS = [
        Binding("j,down", "next_item", "Next", show=False),
        Binding("k,up", "previous_item", "Previous", show=False),
        Binding("l,enter", "toggle_item", "Toggle", show=False)
    ]

    def compose(self):
        yield Container(id="tree-view-container")

    def add_item(self, domain, files=None):
        new_item = TreeViewItem(domain, files)
        self.query_one("#tree-view-container", Container).mount(new_item)
        new_item.scroll_visible()

    def action_next_item(self):
        pass

    def action_previous_item(self):
        pass

    def action_toggle_item(self):
        pass
