from textual.app import App, ComposeResult
from textual.widgets import Header, Footer


class TUI_HamRadioLogApp(App):
    """A Textual app to manage stopwatches."""

    BINDINGS = [("q", "exit", "Wyjście"), ("d", "toggle_dark", "Włącz tryb ciemny")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

    def action_exit(self) -> None:
        self.exit()

    def on_mount(self) -> None:
        self.title = "TUI Ham Radio Log"

if __name__ == "__main__":
    app = TUI_HamRadioLogApp()
    app.run()