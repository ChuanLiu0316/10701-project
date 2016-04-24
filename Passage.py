
# This module defines the Class Passage, including methods wordCount and InverseWordCount
# constructor takes input as raw data from tsv file from MCTest by microsoft
# parsing also done here 
from math import log
import nltk
import re 

def eliminatePeriodAndComma(str):
    return str.replace('.', "").replace(',', "")

def toLowerCase(str):
    return str.lower()    

class Question:

    def __init__(self, data):
        Temp = data[0].split(':')
        self.isOne = Temp[0] =='one'  # bool indicating whether the question can be answered by one sentence 
        self.questionWords = set(nltk.word_tokenize(eliminatePeriodAndComma(toLowerCase(Temp[1].replace('?',""))))) #set of words in question 
        self.answersWords = [] #array of length 4, each one is a set of words for answer 1,2,3,4
       
        for i in range(4):
            self.answersWords.append(set(nltk.word_tokenize(toLowerCase(eliminatePeriodAndComma(data[i+1])))))




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
        unparsedPagraph = self.replaceNewlineWithSpace(data[2]) + " "
        self.unparsedPagraph = unparsedPagraph
    
        self.passage = nltk.word_tokenize( toLowerCase(unparsedPagraph.replace('. ', " ").replace(', ', " ").replace("? ", " ").replace("! ", " ").replace('"', " "))) #should be a string array, in paper notation is 'P', with no '.' and ','
        self.passageWords = set(self.passage) #should be a set containing non-duplicate words in passage, appear in paper, but i don't know what it's for 
        self.passageWordsCountDict = {x: self.passage.count(x) for x in self.passageWords}  #efficient in doing sliding window
        rawSentences = nltk.sent_tokenize(toLowerCase(unparsedPagraph))

        self.sentences =[nltk.word_tokenize(value) for value in rawSentences if len(value) != 0]

        # Questions and answers part
        self.questions = [] #array of length 4 of object Question 
        for i in range(4):
            newQuestion = Question(data[i*5+3: (i+1)*5+3])
            self.questions.append(newQuestion)

        TempStopWords = []
        with open('stopwords.txt') as f:
            for line in f:
                TempStopWords.append(line.replace('\r\n', ""))

        self.stopWords = set(TempStopWords) # set of stop words, in paper notation is U, can be downloaded, will only be used in distance based Algo
     
    def wordCount(self, word):
        #return counts of word appears in self.passage
        if word in self.passageWordsCountDict:
            return self.passageWordsCountDict[word]
        else:
            return 0.001    

    def InverseWordCount(self, word):
        # simple, this is final
        return log(1 + (1.0/ self.wordCount(word)))

