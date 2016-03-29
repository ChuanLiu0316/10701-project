from Passage import *

class Passages:
    
    self.passages = []

    def __init__(self, file):
        with open(file) as tsv:
            for line in csv.reader(tsv, delimiter='\t'):
                newPassage =  Passage(line)
                self.passages.append(newPassage)
