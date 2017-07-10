def classify(features_train, labels_train):
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier


    ### your code goes here!

    import numpy as np
    from sklearn.naive_bayes import GaussianNB

    clf = GaussianNB()
    clf.fit(features_train, labels_train)
    #pred = clf.predict(features_test)
    return clf

    from sklearn.metrics import accuracy_score

    #print clf.score(features_test, labels_test)

