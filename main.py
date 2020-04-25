from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.tabbedpanel import TabbedPanel

from kivy.lang.builder import Builder
from kivy.core.window import Window

import xml.etree.ElementTree as et

from display_settings import x, y

Builder.load_file('home_page.kv')
Window.size = (x, y)

class dict_entry:
    def __init__(self, chinese, jyutping, english, part_speech, labels):
        self.chinese = chinese
        self.jyutping = jyutping
        self.english = english
        self.part_speech = part_speech
        if labels == []:
            self.labels = None
        else:
            self.labels = labels
        
def import_xml(filename):
    with open(filename, 'rb') as xml_file:
        tree = et.parse(xml_file)
        root = tree.getroot()
    
    words = []
    for i in range(len(root)):
        chinese = ''
        jyutping = ''
        english = ''
        part_speech = ''
        labels = []
        
        for child in root[i]:
            if child.tag == 'Word':
                chinese = child.text
            elif child.tag == 'Jyutping':
                jyutping = child.text
            elif child.tag == 'English':
                english = child.text
            elif child.tag == 'Class':
                part_speech = child.text
            elif child.tag == 'labels':
                labels.append(child.text)
                
        words.append(dict_entry(chinese, jyutping, english, part_speech, labels))
    
    return words
    
class home_page(BoxLayout):
    from display_settings import (widget_height, tab_width)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.words = import_xml('word_bank.xml')
    
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