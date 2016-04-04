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
        SWSenresult = []
        SWDresult = []
        SWDSenresult = []
        passageIndex = 0
        for passage in TestPassages.passages:

            SWresult.append(SlidingWindow.run(passage))
            SWSenresult.append(SlidingWindow.runSentence(passage))
            SWDresult.append(SWDalgo.run(passage))
            SWDSenresult.append(SWDalgo.runSentence(passage))

            passageIndex += 1


        SWanswers = []
        SWSenanswers = []
        SWDanswers = []
        SWDSenanswers = []

        for i in range(len(SWresult)):
            tempSW = []
            tempSWSen = []
            tempSWD = []
            tempSWDSen = []
            for j in range(4):
                tempSW.append(maxScoreIndex(SWresult[i][j]))
                tempSWSen.append(maxScoreIndex(SWSenresult[i][j]))
                tempSWD.append(maxScoreIndex(SWDresult[i][j]))
                tempSWDSen.append(maxScoreIndex(SWDSenresult[i][j]))



            SWanswers.append(tempSW)  
            SWSenanswers.append(tempSWSen)  
            SWDanswers.append(tempSWD)
            SWDSenanswers.append(tempSWDSen)
        
        SWcorrectOne = 0
        SWcorrectMultiple = 0
        SWerrorOne = 0
        SWerrorMultiple = 0

        SWSencorrectOne = 0
        SWSencorrectMultiple = 0
        SWSenerrorOne = 0
        SWSenerrorMultiple = 0

        SWDcorrectOne = 0
        SWDcorrectMultiple = 0
        SWDerrorOne = 0
        SWDerrorMultiple = 0

        SWDSencorrectOne = 0
        SWDSencorrectMultiple = 0
        SWDSenerrorOne = 0
        SWDSenerrorMultiple = 0

        for i in range(len(Answers)):
            for j in range(4):
                if TestPassages.passages[i].questions[j].isOne:
                    if SWanswers[i][j] == Answers[i][j]:
                        SWcorrectOne += 1
                    else:
                        SWerrorOne += 1

                    if SWSenanswers[i][j] == Answers[i][j]:
                        SWSencorrectOne += 1
                    else:
                        SWSenerrorOne += 1

                    if SWDanswers[i][j] == Answers[i][j]:
                        SWDcorrectOne += 1
                    else:
                        SWDerrorOne += 1

                    if SWDSenanswers[i][j] == Answers[i][j]:
                        SWDSencorrectOne += 1
                    else:
                        SWDSenerrorOne += 1    
                else:
                    if SWanswers[i][j] == Answers[i][j]:
                        SWcorrectMultiple += 1
                    else:
                        SWerrorMultiple += 1

                    if SWSenanswers[i][j] == Answers[i][j]:
                        SWSencorrectMultiple += 1
                    else:
                        SWSenerrorMultiple += 1

                    if SWDanswers[i][j] == Answers[i][j]:
                        SWDcorrectMultiple += 1
                    else:
                        SWDerrorMultiple += 1 

                    if SWDSenanswers[i][j] == Answers[i][j]:
                        SWDSencorrectMultiple += 1
                    else:
                        SWDSenerrorMultiple += 1     

        return [Answers, 
               [SWanswers, SWcorrectOne, SWerrorOne, SWcorrectMultiple, SWerrorMultiple],
               [SWSenanswers, SWSencorrectOne, SWSenerrorOne, SWSencorrectMultiple, SWSenerrorMultiple],
               [SWDanswers, SWDcorrectOne, SWDerrorOne, SWDcorrectMultiple, SWDerrorMultiple],
               [SWDSenanswers, SWDSencorrectOne, SWDSenerrorOne, SWDSencorrectMultiple, SWDSenerrorMultiple]]                     
