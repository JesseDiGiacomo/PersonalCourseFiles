#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

#########################################################


def classify(features_train, labels_train):
    
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier

    import numpy as np
    from sklearn import svm   
    from sklearn.metrics import accuracy_score

    C=10000
    
    clf = svm.SVC(kernel = "rbf", C=C)

    #features_train = features_train[:len(features_train)/100] 
    #labels_train = labels_train[:len(labels_train)/100]

    t0 = time()
    clf.fit(features_train, labels_train)
    print "training time:", round(time()-t0, 3), "s"

 

    print "Resposta para 50: ", clf.predict(features_test[50])
    
    pred = clf.predict(features_test)
    t0 = time()
    print "predict time:", round(time()-t0, 3), "s"
    
    print "Accuracy: ", clf.score(features_test, labels_test)
    
    print "Support Vectors: ", clf.support_vectors_

    print "Support Vectors for each class: ", clf.n_support_

    print "e-mails da Sara: ",len(pred[pred == 0])

    print "e-mails da Chris: ",len(pred[pred == 1])

    return clf
    

    
classify(features_train, labels_train)
