from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file("calc.kv")  # Load the UI

class MyLayout(BoxLayout):
    def clear(self):
        self.ids.result.text = ""

    def button_press(self, button):
        self.ids.result.text += str(button)

    def calculate(self):
        try:
            self.ids.result.text = str(eval(self.ids.result.text))
        except:
            self.ids.result.text = "Error"

    def plus_minus(self):
        try:
            value = str(eval(self.ids.result.text))
            if value.startswith("-"):
                self.ids.result.text = value[1:]
            else:
                self.ids.result.text = "-" + value
        except:
            self.ids.result.text = "Error"

class CalculatorApp(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    CalculatorApp().run()
