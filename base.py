import kivy
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager    
from kivy.lang import Builder

class MainScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('my.kv')

class MyMainApp(App):
    def build(self):
        return kv
        

if __name__ == '__main__':
    MyMainApp().run()