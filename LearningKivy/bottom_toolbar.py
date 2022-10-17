from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (300, 500)

screen_helper = """
Screen:
    name:'About us'
    BoxLayout:
        orientation:'vertical'
        MDTopAppBar:
            title:'Demo'
            left_action_items:[['menu',lambda x: app.navigation_draw()]]
            right_action_items:[['logout',lambda x: app.navigation_draw()]]
            elevation:25
            md_bg_color: 0,0,100/255,1
              
        MDLabel:
            text:"hi"
            halign:'center'
        MDBottomAppBar:
            title:'Bottom'
            left_action_items:[['menu',lambda x: app.navigation_draw()]]
            elevation:10
            md_bg_color: 0,0,100/255,1
"""


class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Red"
        screen = Builder.load_string(screen_helper)

        return screen

    def navigation_draw(self):
        print("Navigation")


DemoApp().run()
