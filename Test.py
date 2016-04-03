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
        
        SWcorrect = 0
        SWerror = 0
        SWDcorrect = 0
        SWDerror = 0
        for i in range(len(Answers)):
            for j in range(4):
                if SWanswers[i][j] == Answers[i][j]:
                    SWcorrect += 1
                else:
                    SWerror += 1

                if SWDanswers[i][j] == Answers[i][j]:
                    SWDcorrect += 1
                else:
                    SWDerror += 1

        return (Answers, SWanswers, SWcorrect, SWerror, SWDanswers, SWDcorrect, SWDerror)                       
