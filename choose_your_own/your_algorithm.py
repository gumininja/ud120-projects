#!/usr/bin/python

import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from time import time

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
# plt.xlim(0.0, 1.0)
# plt.ylim(0.0, 1.0)
# plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
# plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
# plt.legend()
# plt.xlabel("bumpiness")
# plt.ylabel("grade")
# plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary
from sklearn.ensemble import AdaBoostClassifier
print "AdaBoost classifier"
from sklearn.svm import SVC
clf = AdaBoostClassifier(n_estimators=10,learning_rate=.2,base_estimator=SVC(probability=True,C=10000000,kernel='rbf'))
# from sklearn.ensemble import RandomForestClassifier
# print "RandomForest classifier"
# clf = RandomForestClassifier(n_jobs=4,n_estimators=10000,min_samples_split=2,max_features=None)
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"
t0 = time()
pred = clf.predict(features_test)
from sklearn.metrics import accuracy_score
print "prediction time:", round(time()-t0, 3), "s"
print "accuracy:", accuracy_score(labels_test, pred)








try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
