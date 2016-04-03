# Sliding Window Algorithm to run on one passage
from Passage import * 
class SlidingWindow:
    # the algorithm doesn't return one answer but scores for 4 answers, easy to optimize later
    def run(self, passage):
        def score(S):
            max = 0
            for j in range(len(passage.passageWords)):
                sum = 0
                for w in range(len(S)):
                    tempWord =p assage.passageWords[j+w]
                    if tempWord in S:
                        sum += passage.InverseWordCount(tempWord)
                if sum > max:
                    max = sum

            return sum                    
                                

        answersScores = []
        for i in range(4):
            Q =  passage.questions[i]    
            Qset = Q.questionsWords    
            ScoreArray = []
            for j in range(4):
                Sset = Qset.union(Q.answersWords[j])
                ScoreArray.append(score(Sset))

            answersScores.append(ScoreArray)
            
        return ScoreArray        