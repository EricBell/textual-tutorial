from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Button
from textual.containers import Center


class HelloApp(App):
    """A small Textual app with a centered button and body text."""

    CSS = """
    #body {
        padding: 1 2;
    }
    Button {
        margin: 1 0;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        # Center the body text and the button so the label appears inside the button
        yield Center(Static("Press the button", id="body"), Button("Click me", id="btn"))
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle the button press and update the body text.

        The handler must be a method on the App (or a Widget) so Textual wires it up.
        """
        body = self.query_one("#body", Static)
        body.update("Hello — you pressed the button!")


if __name__ == "__main__":
    HelloApp().run()