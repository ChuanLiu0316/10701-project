# Train using Linear SVC by scikit-learn
from sklearn import svm
#Farray is a features array, each element is feature vector of single data 
def LinearSVCTrain(Farray, Y):
    LSVC = svm.LinearSVC()
    LSVC.fit(Farray, Y)

    return (LSVC.intercept_, LSVC.coef_)
    
