from textual.app import App
from textual.reactive import reactive
from textual.widgets import Static, Button, Header, Footer

class CounterApp(App):
    """A simple counter app with standard quit bindings."""

    BINDINGS = [
        ("q", "quit", "Quit"),
        ("ctrl+c", "quit", "Quit"),
    ]

    count = reactive(0)

    def compose(self):
        yield Header()
        yield Static(f"Count: {self.count}", id="label")
        yield Button("Increment", id="inc")
        yield Button("Reset", id="reset")
        yield Footer()

    def on_button_pressed(self, event):
        if event.button.id == "inc":
            self.count += 1
        elif event.button.id == "reset":
            self.count = 0
        self.query_one("#label", Static).update(f"Count: {self.count}")

    def action_quit(self) -> None:
        """Called by the key binding to quit the app."""
        self.exit()

if __name__ == "__main__":
    CounterApp().run()