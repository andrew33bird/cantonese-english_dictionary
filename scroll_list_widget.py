from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

from kivy.lang.builder import Builder
Builder.load_file('scroll_list_widget.kv')

class Scroll_List(ScrollView):
    
    def __init__(self, word_list, english_lead=True, **kwargs):
        super().__init__(**kwargs)
        self.english_lead = english_lead
        self.word_list = word_list
        
        self.ids.layout.bind(minimum_height=self.ids.layout.setter('height'))
        
        for i in range(len(word_list)):
            self.ids.layout.add_widget(Row_Button(word_list[i], english_lead))
            
class Row_Button(BoxLayout):
    from display_settings import (widget_height)
    
    def __init__(self, word, english_lead, **kwargs):
        super().__init__(**kwargs)
        self.word = word
        self.english_lead = english_lead
        
        if english_lead:
            self.ids.left_col.text = self.word.english
            self.ids.right_col.text = self.word.jyutping
        else:
            self.ids.left_col.text = self.word.jyutping
            self.ids.right_col.text = self.word.english