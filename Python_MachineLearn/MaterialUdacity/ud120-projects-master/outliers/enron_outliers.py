#!/usr/local/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from operator import itemgetter


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop("TOTAL",0) #remove outlier "TOTAL" da tabela pois era um erro da planilha.
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

### your code below

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


#Exibe o nome da pessoa com maior salario e seu respectivo valor
maxSalary = None
personName = None
for keys,values in data_dict.items():
    if values["salary"]!="NaN" :
        insideList = (keys, values["salary"])
        if maxSalary < values["salary"]:
            maxSalary = values["salary"]
            personName = keys
print "Nome da pessoa com salario mais alto: ",personName
print "Valor do salario: ",maxSalary

#Exibe lista das pessoas com bonus superior a 5 bilhoes e seu respectivo bonus
maxBonus = None
personName = None
print "lista das pessoas com bonus superior a 5 bilhoes: "
for keys,values in data_dict.items():
    if values["bonus"]!="NaN" and values["bonus"] >= 5000000 :
        bonusList = (keys, values["bonus"])
        print bonusList


#print "Nome da pessoa com bonus mais alto: ",personName
#print "Valor do salario: ",maxBonus
