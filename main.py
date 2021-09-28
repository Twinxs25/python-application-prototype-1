from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix import menu, screen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar
from kivy.metrics import dp
from kivy.uix.screenmanager import ScreenManager




class Aegis(MDApp):


    def build(self):

        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("prelogin.kv"))
        screen_manager.add_widget(Builder.load_file("menu.kv"))

        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"Website {i+1}",
                "height": dp(56),
                "on_release": lambda x=f"Webiste {i+1}": self.menu_callback(x),
             } for i in range(5)
        ]
        self.menu = MDDropdownMenu(
            items=menu_items,
            width_mult=3,
        )

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return screen_manager

    def callback(self, button):
        self.menu.caller = button
        self.menu.open()

    def menu_callback(self, text_item):
        self.menu.dismiss()
        Snackbar(text=text_item).open()

    def time(self):
        print("time...")


    def on_start(self):
        Clock.schedule_once(self.login, 5)

    def login(self, *args):
        screen_manager.current = "login"





if __name__ == '__main__':
    Aegis().run()
