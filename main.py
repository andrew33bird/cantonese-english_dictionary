from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.lang.builder import Builder

import xml.etree.ElementTree as et

Builder.load_file('home_page.kv')

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
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def load_xml(self, text_box):
        words = import_xml(text_box.text)
        
        disp_text = 'Number of Dictionary Items: ' + str(len(words)) + '\n\n'
        disp_text += words[0].jyutping + '\n'
        disp_text += words[0].english + '\n'
        disp_text += words[0].part_speech + '\n'
        
        self.ids.main_label.text = disp_text
    
class dictionaryApp(App):
    title = 'Andrew\'s Cantonese/English Dictionary App!!!'
    
    def build(self):
        return home_page()
    
if __name__ == '__main__':

    dictionaryApp().run()