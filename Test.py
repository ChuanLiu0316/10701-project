from SWandDAlgo import *
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
        SWresult = []
        SWDresult = []
        for passage in TestPassages.passages:
            SWresult.append(SlidingWindow.run(passage))
            SWDresult.append(SWDalgo.run(passage))

        SWanswers = []
        SWDanswers = []
        for i in range(len(SWresult)):
            tempSW = []
            tempSWD = []
            for j in range(len(SWresult[i])):
                tempSW.append(maxScoreIndex(SWresult[i][j]))
                tempSWD.append(maxScoreIndex(SWDresult[i][j]))

            SWanswers.append(tempSW)    
            SWDanswers.append(tempSWD)
        
        SWcorrectOne = 0
        SWcorrectMultiple = 0
        SWerrorOne = 0
        SWerrorMultiple = 0
        SWDcorrectOne = 0
        SWDcorrectMultiple = 0
        SWDerrorOne = 0
        SWDerrorMultiple = 0
        for i in range(len(Answers)):
            for j in range(4):
                if TestPassages.passages[i].questions[j].isOne:
                    if SWanswers[i][j] == Answers[i][j]:
                        SWcorrectOne += 1
                    else:
                        SWerrorOne += 1

                    if SWDanswers[i][j] == Answers[i][j]:
                        SWDcorrectOne += 1
                    else:
                        SWDerrorOne += 1
                else:
                    if SWanswers[i][j] == Answers[i][j]:
                        SWcorrectMultiple += 1
                    else:
                        SWerrorMultiple += 1

                    if SWDanswers[i][j] == Answers[i][j]:
                        SWDcorrectMultiple += 1
                    else:
                        SWDerrorMultiple += 1 

        return [Answers, 
               [SWanswers, SWcorrectOne, SWerrorOne, SWcorrectMultiple, SWerrorMultiple],
               [SWDanswers, SWDcorrectOne, SWDerrorOne, SWDcorrectMultiple, SWDerrorMultiple]]                     
