
# This module defines the Class Passage, including methods wordCount and InverseWordCount
# constructor takes input as raw data from tsv file from MCTest by microsoft
# parsing also done here 
from math import log

class Question:

    def __init__(self, data):
        self.words = {} #set of words in question 
        self.answersWords = [] #array of length 4, each one is a set of words for answer 1,2,3,4



class Passage:

    passageCount = 0

    def __init__(self, data):
        #record nunber of passages, should have 160 or 500 for MCTest 160 and MCTest 500
        Passage.passageCount += 1

        #just structure, unfinished
        self.passage = []  #should be a string array, in paper notation is 'P'
        self.passageWords = {} #should be a set containing non-duplicate words in passage, appear in paper, but i don't know what it's for 
        self.questions = [] #array of length 4 of object Question 
        self.stopWords = {} # set of stop words, in paper notation is U, can be downloaded, will only be used in distance based Algo
     
    def wordCount(word):
        #return counts of word appears in self.passage

    def InverseWordCount(word):
        # simple, this is final
        return log(1 + (1/ wordCount(word)))
        

