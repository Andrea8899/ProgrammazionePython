from kivy.app import App
from kivy.uix.label import Label 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class Main(BoxLayout):
    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)

        layout = BoxLayout()
        layout2 = BoxLayout()
        nome = Button(text="ciao")
        nome2 = Button(text="come stai")
        layout.add_widget(nome)
        layout.add_widget(nome2)
        self.add_widget(layout2)
        self.add_widget(layout)

class MainApp(App):
    def build(self):
        return Main()

if __name__ == "__main__":
    MainApp().run()
