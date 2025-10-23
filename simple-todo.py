from textual.app import App
from textual.widgets import Header, Footer, Input, Button, Static
from textual.containers import Vertical, Horizontal

class SimpleTodo(App):
    """A simple todo list application."""
    
    CSS = """
    Horizontal {
        height: 5;
        margin: 1 1 2 1;
        align: center middle;
    }
    
    Input {
        width: 80%;
        margin: 1 2;
        height: 3;
        border: tall $primary;
    }
    
    Button {
        margin: 1 2;
    }
    
    #tasks {
        margin: 1 2;
        height: auto;
        padding: 1;
    }
    
    .task-line {
        padding: 0 1;
        color: $text;
    }
    """

    def compose(self):
        yield Header()
        with Vertical():
            with Horizontal():
                yield Input(placeholder="New task", id="input")
                yield Button("Add", id="add")
            yield Static("", id="tasks", classes="task-list")
        yield Footer()


    def add_task(self) -> None:
        """Add the current input value as a new task."""
        from rich.text import Text
        
        inp = self.query_one("#input", Input)
        text = inp.value.strip()
        if text:
            tasks = self.query_one("#tasks", Static)
            current = tasks.render() if tasks.render() is not None else ""
            
            # Create styled task using Rich's Text class
            task_line = Text()
            task_line.append("• ", style="bold green")  # Bullet in green
            task_line.append(text, style="white")  # Task text in white
            
            # Combine with existing tasks
            if current:
                tasks.update(str(current) + "\n" + str(task_line))
            else:
                tasks.update(str(task_line))
                
            inp.value = ""  # Clear input

    def on_button_pressed(self, event) -> None:
        """Handle the Add button press."""
        if event.button.id == "add":
            self.add_task()

    def on_input_submitted(self, event) -> None:
        """Handle when the user presses Enter in the input."""
        self.add_task()

if __name__ == "__main__":
    SimpleTodo().run()