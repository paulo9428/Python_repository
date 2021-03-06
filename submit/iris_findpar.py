from sklearn import svm, metrics
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV

csv = pd.read_csv('./data/iris.csv')
cdata = csv[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
cret = csv['Name']

trainData, testData, trainLabel, testLabel = train_test_split(cdata, cret)

# grid-search params
params = [
    {"C": [1, 10, 100, 1000], "kernel": ['linear']},
    {"C": [1, 10, 100, 1000], "kernel": ['rbf'], "gamma": [0.001, 0.0001]},
]
clf = GridSearchCV(svm.SVC(), params, n_jobs = -1, cv = 3, iid=True)

clf.fit(trainLabel, testLabel)

print("machine=", clf.best_estimator_)
 

 # 검증(test)
pred = clf.predict(testData)   
score = metrics.accuracy_score(testLabel, pred)
print("score=", score)



