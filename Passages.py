from Passage import *

class Passages:
    ASDASD = 0
    def __init__(self, file):
        self.passages = []
        with open(file) as tsv:
            for line in csv.reader(tsv, delimiter='\t'):
                newPassage =  Passage(line)
                self.passages.append(newPassage)
