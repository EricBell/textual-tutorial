from textual.app import App
from textual.widgets import Header, Footer, Input, Button, Static
from textual.containers import Vertical, Horizontal

class SimpleTodo(App):
    def compose(self):
        yield Header()
        with Vertical():
            with Horizontal():
                yield Input(placeholder="New task", id="input")
                yield Button("Add", id="add")
            yield Static("", id="tasks")  # we'll append tasks here
        yield Footer()


    def add_task(self) -> None:
        """Add the current input value as a new task."""
        inp = self.query_one("#input", Input)
        text = inp.value.strip()
        if text:
            tasks = self.query_one("#tasks", Static)
            # Get current content or empty string if None
            current = tasks.render() if tasks.render() is not None else ""
            # naive append; for nicer layout, use a ListView or DataTable
            tasks.update(current + f"\n• {text}" if current else f"• {text}")
            inp.value = ""

    def on_button_pressed(self, event) -> None:
        """Handle the Add button press."""
        if event.button.id == "add":
            self.add_task()

    def on_input_submitted(self, event) -> None:
        """Handle when the user presses Enter in the input."""
        self.add_task()

if __name__ == "__main__":
    SimpleTodo().run()