# Sliding Window Algorithm to run on one passage
from Passage import * 
from math import log
class SlidingWindow:
    # the algorithm doesn't return one answer but scores for 4 answers, easy to optimize later
    @classmethod
    def run(self, passage):
        def score(S):
            max = 0
            for j in range(len(passage.passage) - len(S)):
                sum = 0
                for w in range(len(S)):
                    tempWord =passage.passage[j+w]
                    if tempWord in S:
                        sum += passage.InverseWordCount(tempWord)
                if sum > max:
                    max = sum

            return max                  
                                

        answersScores = []
        for i in range(4):
            Q =  passage.questions[i]    
            Qset = Q.questionWords    
            ScoreArray = []
            for j in range(4):
                Sset = Qset.union(Q.answersWords[j])
                ScoreArray.append(score(Sset))

            answersScores.append(ScoreArray)

        return answersScores  

    @classmethod
    def runSentence(self, passage):
        def score(S):
            max = 0.0
            for i in range(len(passage.sentences)):
                sum = 0.0
                currentSence = passage.sentences[i]
                for j in range(len(currentSence)):
                    tempWord = currentSence[j]
                    if tempWord in S:
                        sum += passage.InverseWordCount(tempWord)   
                tempScore = (sum)/log(1 + len(currentSence))
                if tempScore > max:
                    max = tempScore       
            return max  

        answersScores = []
        for i in range(4):
            Q =  passage.questions[i]    
            Qset = Q.questionWords    
            ScoreArray = []
            for j in range(4):
                Sset = Qset.union(Q.answersWords[j])
                ScoreArray.append(score(Sset))

            answersScores.append(ScoreArray)

        return answersScores 
