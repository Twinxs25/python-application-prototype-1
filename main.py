from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix import textfield
from kivymd.uix import label
from kivymd.uix.behaviors import elevation
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.selectioncontrol import MDSwitch
from kivymd.uix.toolbar import MDBottomAppBar

class WebEx(MDApp):

    def time(self):
        print("time...")

    def callback(self, button):
        self.menu.caller = button
        self.menu.open()

    def menu_callback(self, text_item):
        self.menu.dismiss()
        Snackbar(text=text_item).open()


    def build(self):
        
        screen = MDScreen()

        self.theme_cls.primary_palette = 'Cyan'

        #Toolbar with burger and timer functions
        self.toolbar = MDToolbar(title="THE ANTI-SOCIAL APP",
        elevation = 8)
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.left_action_items = [
        ["menu", lambda x: self.callback(x)]]
        self.toolbar.right_action_items = [["timer", lambda x: self.time()]]        
        screen.add_widget(self.toolbar)

        #FACEBOOK SWITCH
        self.switch = MDSwitch(
        pos_hint = {"center_x" : 0.87, "center_y" : 0.80 })
        screen.add_widget(self.switch)
        screen.add_widget(Image(source = "R.png",
        pos_hint = {"center_x" : 0.75, "center_y" : 0.80},
        size_hint_x = 0.15, size_hint_y = 0.15))


        #YOUTUBE SWITCH
        self.switch = MDSwitch(
        pos_hint = {"center_x" : 0.87, "center_y" : 0.60 })
        screen.add_widget(Image(source = "Y.png",
        pos_hint = {"center_x" : 0.755, "center_y" : 0.60},
        size_hint_x = 0.3, size_hint_y = 0.3))
        
        screen.add_widget(self.switch)
 

        #The Loop for the list of websites
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

        # The text field that users, use to add 
        # websites to block with URL
        self.input = MDTextField (
            hint_text = "Enter Website URL",
            halign = "center",
            size_hint = (0.8,1),
            pos_hint= {"center_x" : 0.5, "center_y" : 0.30},
            font_size = 22
        )
        screen.add_widget(self.input)
        
        return screen

if __name__ == '__main__':
    WebEx().run()
