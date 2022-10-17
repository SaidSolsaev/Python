import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Rectangle
from kivy.graphics import Color
from pyautogui import size


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="Navn: "))
        self.name = TextInput()
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="Etternavn: "))
        self.etternavn = TextInput()
        self.inside.add_widget(self.etternavn)

        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput()
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)

        self.trykk = Button(text="Neste", font_size=40)
        self.trykk.bind(on_press=self.pressed)
        self.add_widget(self.trykk)

        with self.canvas:
            Color(1,0,0,6, mode="rgba")
            self.rect = Rectangle(pos=(0, 0), size=(50, 50))
            Color(1,1,0,5,mode="rgba")
            self.rect = Rectangle(pos=(200, 300), size=(100, 50))

    def on_touch_move(self, touch):
        self.rect.pos = touch.pos

    def pressed(self, instance):
        navn = self.name.text
        etterN = self.etternavn.text
        email = self.email.text
        print("Navn: " + navn, "Etternavn: " + etterN, "Email: " + email)


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
