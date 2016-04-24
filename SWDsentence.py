#Distance Based Algorithm run on one passage
from Passage import * 
from math import log
class SWDalgo:
    # the algorithm doesn't return one answer but scores for 4 answers, easy to optimize later
    @classmethod
    def runSentence(self, passage):

        def scoreDis(SQ, SA, sentence):
            Qindexes = [i for i,x in enumerate(sentence) if x in SQ]
            Aindexes = [i for i,x in enumerate(sentence) if x in SA]
            
            sum = 0.0
            abosulteMin = len(sentence)
            for Qindex in Qindexes:
                min = len(sentence)
                for Aindex in Aindexes:
                    if abs(Qindex - Aindex) < min:
                        min = abs(Qindex - Aindex)
                    if abs(Qindex - Aindex) < abosulteMin: 
                        abosulteMin = abs(Qindex - Aindex)
                sum += min       
      
            avg = sum/len(sentence)
            return avg/len(sentence)      

        def score(Q, A):
            max = -100000
            S = Q.union(A)
            for i in range(len(passage.sentences)):
                sum = 0
                currentSence = passage.sentences[i]
                SentenceSet = set(currentSence)
                QS = Q.intersection(SentenceSet).difference(passage.stopWords)
                AS = ((A.intersection(SentenceSet)).difference(Q)).difference(passage.stopWords)

                for j in range(len(currentSence)):
                    tempWord = currentSence[j]
                    if tempWord in S:
                        sum += passage.InverseWordCount(tempWord)   
                tempScore = (sum)/log(1 + len(currentSence))

                DisScore = 1.0
                if len(QS) != 0 and len(AS) != 0:
                    DisScore = scoreDis(QS, AS, currentSence)

                if DisScore >1:
                    print "impossible!!"    

                tempScore = tempScore - DisScore

                if tempScore > max:
                    max = tempScore       
            return max  


        answersScores = []
        for i in range(4):
            Q =  passage.questions[i] 
  
            ScoreArray = []
            for j in range(4):
                ASet = Q.answersWords[j]
                QSet = Q.questionWords
                ScoreArray.append(score(QSet, ASet))

            answersScores.append(ScoreArray)

        return answersScores 


