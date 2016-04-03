
# This module defines the Class Passage, including methods wordCount and InverseWordCount
# constructor takes input as raw data from tsv file from MCTest by microsoft
# parsing also done here 
from math import log
import nltk

class Question:

    def __init__(self, data):
        self.words = {} #set of words in question 
        self.answersWords = [] #array of length 4, each one is a set of words for answer 1,2,3,4



class Passage:

    passageCount = 0

    #helper parser
    def replaceNewlineWithSpace(self,str):
        return str.replace("\\newline", " ")

    #finish later, doesn't need in the intial development 
    def paragraphToListOfSentence(self, paragraph): 
        pass

        

    def __init__(self, data):
        #record nunber of passages, should have 160 or 500 for MCTest 160 and MCTest 500
        Passage.passageCount += 1

        # Passage part
        unparsedPagraph = self.replaceNewlineWithSpace(data[2])
    
        self.passage = nltk.word_tokenize( unparsedPagraph.replace('.', "").replace(',', "")) #should be a string array, in paper notation is 'P', with no '.' and ','
        self.passageWords = set(self.passage) #should be a set containing non-duplicate words in passage, appear in paper, but i don't know what it's for 
        self.passageWordsCountDict = {x: self.passage.count(x) for x in self.passageWords}  #efficient in doing sliding window


        # Questions and answers part
        self.questions = [] #array of length 4 of object Question 
        for i in range(4):
            newQuestion = Question(data[i*5+3: (i+1)*5+3])
            self.questions.append(newQuestion)


        self.stopWords = {} # set of stop words, in paper notation is U, can be downloaded, will only be used in distance based Algo
     
    def wordCount(self, word):
        #return counts of word appears in self.passage
        return 1

    def InverseWordCount(self, word):
        # simple, this is final
        return log(1 + (1/ self.wordCount(word)))
        

