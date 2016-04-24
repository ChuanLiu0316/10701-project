#Distance Based Algorithm run on one passage
from Passage import * 
class DistanceBased:
    # the algorithm doesn't return one answer but scores for 4 answers, easy to optimize later
    @classmethod
    def run(self, passage):
        def score(SQ, SA):
            Qindexes = [i for i,x in enumerate(passage.passage) if x in SQ]
            Aindexes = [i for i,x in enumerate(passage.passage) if x in SA]
            sum = 0.0 
            for Qindex in Qindexes:
                min = len(passage.passage)
                for Aindex in Aindexes:
                    if abs(Qindex - Aindex) < min:
                        min = abs(Qindex - Aindex)

                sum += min
            avg = sum/len(Qindexes)            
            return float(avg)/len(passage.passage)            
        
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