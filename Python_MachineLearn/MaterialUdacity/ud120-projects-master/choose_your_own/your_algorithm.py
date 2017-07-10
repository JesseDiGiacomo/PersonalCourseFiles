#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

"""Teste do algoritimo de classificacao nearest neighbor centroid [Accuracy:  0.908]"""

def classify(features_train, labels_train):
    
    from sklearn.neighbors.nearest_centroid import NearestCentroid
    import numpy as np
    from sklearn.metrics import accuracy_score
    from time import time

    clf = NearestCentroid()

    t0 = time()
    clf.fit(features_train, labels_train)
    print "training time:", round(time()-t0, 3), "s"

    t0 = time()
    pred = clf.predict(features_test)
    print "predict time:", round(time()-t0, 3), "s"

    print "Accuracy: ", clf.score(features_test, labels_test)

    prettyPicture(clf, features_test, labels_test)
    
    plt.show()
    
    return clf

"""fim do teste do nearest neighbor centroid"""

classify(features_train, labels_train)


"""Teste do algoritimo de classificacao nearest neighbor [Accuracy:  0.944]"""

def classify2(features_train, labels_train):
    
    print(__doc__)

    import numpy as np
    from sklearn import neighbors, datasets
    from sklearn.metrics import accuracy_score
    from time import time

    n_neighbors = 22
    

    clf = neighbors.KNeighborsClassifier(n_neighbors)

    t0 = time()
    clf.fit(features_train, labels_train)
    print "training time:", round(time()-t0, 3), "s"

    t0 = time()
    pred = clf.predict(features_test)
    print "predict time:", round(time()-t0, 3), "s"

    print "Accuracy: ", clf.score(features_test, labels_test)

    prettyPicture(clf, features_test, labels_test)
    
    plt.show()
    
    return clf

"""fim do teste do nearest neighbor"""

classify2(features_train, labels_train)

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
