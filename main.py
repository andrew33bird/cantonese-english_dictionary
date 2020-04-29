from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.tabbedpanel import TabbedPanel

from kivy.lang.builder import Builder
from kivy.core.window import Window

from display_settings import x, y

import xml_file_functions as xml_func

Builder.load_file('home_page.kv')
Window.size = (x, y)

class home_page(BoxLayout):
    from display_settings import (widget_height, tab_width)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        temp = xml_func.import_xml('word_bank.xml')
        self.words = temp['words']
        self.labels = temp['labels']
        
        temp_text = ''
        for i in range(len(self.labels)):
            temp_text += self.labels[i] + '\n'
            
        self.ids.browse_tab_label.text = temp_text
    
    def entry_search(self, input):
        search_text = input.text.lower()
        if search_text == '':
            self.ids.search_tab_label.text = 'Enter search'
            return
        
        words_found = []
        for i in range(len(self.words)):
            comparision = self.words[i].english.lower()
            if search_text in comparision:
                words_found.append(self.words[i])
                
        self.ids.search_tab_label.text = str(len(words_found)) + ' words found'
    
class dictionaryApp(App):
    title = 'Andrew\'s Cantonese/English Dictionary App!!!'
    
    def build(self):
        return home_page()
    
if __name__ == '__main__':

    dictionaryApp().run()