from turtle import Screen
from kivymd.app import MDApp
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.font_definitions import theme_font_styles
from kivymd.uix.button import MDFloatingActionButton, MDFlatButton
from kivymd.uix.screen import Screen


class Demo(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.primary_hue = "100"
        self.theme_cls.theme_style = "Dark"

        label = MDLabel(text="Hello World!",
                        halign="left",
                        # theme_text_color="Primary",
                        text_color="red",
                        font_style="Subtitle2"
                        )
        btn = MDFlatButton(text="Trykk", pos_hint={
                           "center_x": 0.5, "center_y": 0.1},
                           font_size=50)
        btn1 = MDFloatingActionButton(icon="horse", text_color="red")

        screen.add_widget(btn)
        screen.add_widget(btn1)
        screen.add_widget(label)

        return screen


Demo().run()
