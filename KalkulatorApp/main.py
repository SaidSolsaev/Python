import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from matplotlib.dviread import Box

class MainApp(App):
    def build(self):
        self.operasjoner = ["/", "*", "-", "+", ]
        self.siste_brukte_operasjon = None
        self.siste_knapp = None

        main_layout = BoxLayout(orientation = "vertical")
        self.solution = TextInput(background_color = "black", foreground_color = "white", readonly = True, multiline=False, halign="right", font_size=55)
        main_layout.add_widget(self.solution)
        
        buttons = [
            ["7","8", "9", "/"],
            ["4","5", "6", "*"],
            ["1","2", "3", "-"],
            [".","0", "C", "+"],
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text = label, 
                font_size = 30, 
                background_color = "grey",
                pos_hint = {"center_x": 0.5, "center_y":0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
        equal_button = Button(text = "=", 
                font_size = 30, 
                background_color = "grey",
                pos_hint = {"center_x": 0.5, "center_y":0.5},
                )
        equal_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equal_button)
        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            self.solution.text = ""
        else:
            if current and (
                self.siste_brukte_operasjon and button_text in self.operasjoner):
                return
            elif current == "" and button_text in self.operasjoner:
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.siste_knapp = button_text
        self.siste_brukte_operasjon = self.siste_knapp in self.operasjoner

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution


if __name__ == "__main__":
    app = MainApp()
    app.run()