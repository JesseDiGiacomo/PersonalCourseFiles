#!/usr/local/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data) #sort_keys = "../tools/python2_lesson14_keys.pkl")



### your code goes here
"""Begining of spliting data"""

from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)

"""End of spliting data"""


print ("number of POIs on test set: ", len(features_list[0]))
print ("number persons on test set: ", len(features_test))

"""Begining of Decison tree"""

from sklearn import tree

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)
pred = clf.predict(features_test, labels_test)
print ("Decision Tree Accuracy: ", clf.score(features_test, labels_test))

"""End of Decision tree"""

'''
predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
trueLabels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

features_test = trueLabels
pred = predictions

from sklearn.metrics import confusion_matrix
tn, fp, fn, tp = confusion_matrix(features_test, pred).ravel()
print ("TN:",tn,"FP:", fp,"FN:", fn,"TP:", tp)
'''

import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

print "accuracy_score"

print accuracy_score(features_test, pred)

print "precision_score"

print precision_score(features_test, pred, average='macro')

print precision_score(features_test, pred, average='micro')

print precision_score(features_test, pred, average='weighted')

print precision_score(features_test, pred, average= None)

print "recall_score"

print recall_score(features_test, pred, average='macro')

print recall_score(features_test, pred, average='micro')

print recall_score(features_test, pred, average='weighted')

print recall_score(features_test, pred, average=None)
