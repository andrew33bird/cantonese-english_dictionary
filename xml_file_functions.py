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
    all_labels = []
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
                labels = sort_labels(child.text)
                for j in range(len(labels)):
                    if not labels[j] in all_labels:
                        all_labels.append(labels[j])

        words.append(dict_entry(chinese, jyutping, english, part_speech, labels))
    
    return {'words': words, 'labels': all_labels}
    
def sort_labels(label_string):
    if label_string == None:
        return []
    labels = []
    temp_label = ''
    for i in range(len(label_string)):
        if label_string[i] == ',':
            if temp_label != '':
                labels.append(temp_label.lstrip())
                temp_label = ''
        else:
            temp_label += label_string[i]
    
    if temp_label != '':
        labels.append(temp_label.lstrip())
    
    return labels