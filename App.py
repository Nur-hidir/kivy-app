from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Line, Ellipse,Color 
from kivy.animation import Animation
from kivy.uix.label import Label
from kivy.config import Config
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.graphics import Color, Rectangle
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.graphics import Color, Line
from kivy.properties import StringProperty
from kivy.uix.checkbox import CheckBox


 



Window.size=(400,600)
Window.clearcolor=(100/255, 133/255, 152/255)

class MainScreen(Screen):
   pass

            

class DersScreen(Screen):
   pass
class SporScreen(Screen):
   pass
class GunlukScreen(Screen):
   pass

class TaskScreen(Screen):
    def add_task(self, task_text):
        if task_text.strip() == "":
            return
        new_label = Label(text=task_text, size_hint_y=None, height=30)
        self.ids.task_list.add_widget(new_label)

     

 

 

class catlak(Widget):
   pass





class tascatlak(App):
   def build(self):
      Builder.load_file('mainscreen.kv')
      Builder.load_file('spor.kv')
      Builder.load_file('ders.kv')
      Builder.load_file('gunluk.kv')
      Builder.load_file('yapilacak.kv')
      sm=ScreenManager()
      sm.add_widget(MainScreen(name='main_screen'))
       
      sm.add_widget(TaskScreen(name='task_screen'))
       
      sm.add_widget(DersScreen(name='ders_screen'))
      sm.add_widget(SporScreen(name='spor_screen'))
      sm.add_widget(GunlukScreen(name='gunluk_screen'))
      return sm


   def save_journal(self, journal_text):
        # Girilen metni bir dosyaya kaydedebiliriz
      with open("gunluk.txt", "a") as file:
         file.write(journal_text + "\n\n") 

    
 





tascatlak().run()