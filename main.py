import xml.etree.ElementTree as et

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
    
if __name__ == '__main__':
    
    words = import_xml('cantoneseclass101_mywordbank_2020-04-21.xml')
    
    for i in range(len(words)):
        print('\t' + words[i].jyutping)