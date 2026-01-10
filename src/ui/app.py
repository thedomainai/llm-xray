"""
TUI Application definition using Textual.
"""

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, DataTable, Log

class XRayApp(App):
    """The main TUI for LLM X-Ray."""

    CSS = """
    DataTable {
        height: 1fr;
        border: solid green;
    }
    """

    BINDINGS = [
        ("q", "quit", "Quit"),
        ("d", "toggle_dark", "Toggle Dark Mode"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield DataTable()
        yield Log()
        yield Footer()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns("Time", "Method", "Provider", "Model", "Status")
        self.query_one(Log).write_line("LLM X-Ray TUI initialized. Waiting for traffic...")

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark

if __name__ == "__main__":
    app = XRayApp()
    app.run()
