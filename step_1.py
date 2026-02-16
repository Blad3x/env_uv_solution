# step_1.py
from textual.app import App
from textual.widgets import Label, Static

class TextApp(App):
	def compose(self):
		self.static = Static("I am a [bold red]Static[/bold red] widget!")
		yield self.static
		self.label = Label("I am a [yellow italic]Label[/] widget!")
		yield self.label
		
	def on_mount(self):
		# Styling the static widget
		self.static.styles.background = "blue"
		self.static.styles.border = ("solid", "white")
		self.static.styles.text_align = "center"
		self.static.styles.padding = 1, 1
		self.static.styles.margin = 4, 4
		
		# Styling the Label widget
		self.label.styles.background = "darkgreen"
		self.label.styles.border = ("double", "red")
		self.label.styles.padding = 2, 1
		self.label.styles.margin = 3, 4
		
	def on_key(self, event):
		match event.key:
			case "q":
				exit()
if __name__ == "__main__":
	app = TextApp()
	app.run()
