#Distance Based Algorithm run on one passage
from Passage import * 
from DisBased import *
from SWAlgo import *
from math import log
class SWDalgo:
    # the algorithm doesn't return one answer but scores for 4 answers, easy to optimize later
    @classmethod
    def run(self, passage):     
        Dscores = DistanceBased.run(passage)
        SWscores = SlidingWindow.run(passage)
        for i in range(len(SWscores)):
            for j in range(len(SWscores[i])):
                SWscores[i][j] = SWscores[i][j] -  Dscores[i][j]

        return  SWscores

    @classmethod
    def runSentence(self, passage):
        Dscores = DistanceBased.run(passage)
        SWscores = SlidingWindow.runSentence(passage)
        for i in range(len(SWscores)):
            for j in range(len(SWscores[i])):
                SWscores[i][j] = SWscores[i][j] -  1.8*(Dscores[i][j])

        return  SWscores