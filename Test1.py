from SWDsentence import *
from Passages import *

class Test:

    @classmethod
    def run(self, fileP, fileAnswer):
        def maxScoreIndex(L):
            max = L[0]
            index = 0
            for i in range(1, len(L)):
                if L[i] > max:
                    index = i
                    max = L[i]
            temp = ['A', 'B', 'C', 'D']
            return temp[index]
                    
        Answers = []
        with open(fileAnswer) as tsv:
            for line in csv.reader(tsv, delimiter='\t'):
                Answers.append(line)

        TestPassages = Passages(fileP)
        SWDresult = []
  
        for passage in TestPassages.passages:

            SWDresult.append(SWDalgo.runSentence(passage))


        SWDanswers = []

        for i in range(len(SWDresult)):

            tempSWD = []

            for j in range(4):

                tempSWD.append(maxScoreIndex(SWDresult[i][j]))

            SWDanswers.append(tempSWD)
        
        SWDcorrectOne = 0
        SWDcorrectMultiple = 0
        SWDerrorOne = 0
        SWDerrorMultiple = 0

        for i in range(len(Answers)):
            for j in range(4):
                if TestPassages.passages[i].questions[j].isOne:

                    if SWDanswers[i][j] == Answers[i][j]:
                        SWDcorrectOne += 1
                    else:
                        SWDerrorOne += 1

                else:


                    if SWDanswers[i][j] == Answers[i][j]:
                        SWDcorrectMultiple += 1
                    else:
                        SWDerrorMultiple += 1 

        return [Answers, 
               [SWDanswers, SWDcorrectOne, SWDerrorOne, SWDcorrectMultiple, SWDerrorMultiple],
               ]                     
