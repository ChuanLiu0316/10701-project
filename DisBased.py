#Distance Based Algorithm run on one passage
from Passage import * 
class DistanceBased:
    # the algorithm doesn't return one answer but scores for 4 answers, easy to optimize later
    @classmethod
    def run(self, passage):
        def score(SQ, SA):
            Qindexes = [i for i,x in enumerate(passage.passage) if x in SQ]
            Aindexes = [i for i,x in enumerate(passage.passage) if x in SA]
            min = len(passage.passage)
            for Aindex in Aindexes:
                for Qindex in Qindexes:
                    if abs(Qindex - Aindex) < min:
                        min = abs(Qindex - Aindex)
            return float(min)/len(passage.passage)            
        
        answersScores = []
        for i in range(4):
            Q =  passage.questions[i]    
            Qset = Q.questionWords  
            
            SQ = Qset.intersection(passage.passageWords).difference(passage.stopWords)
            ScoreArray = []
            for j in range(4):
                SAI = ((Q.answersWords[j].intersection(passage.passageWords)).difference(Qset)).difference(passage.stopWords)
                if len(SQ) == 0 or len(SAI) == 0:
                    ScoreArray.append(1.0)
                else:
                    ScoreArray.append(score(SQ, SAI))

            answersScores.append(ScoreArray)

        return answersScores  