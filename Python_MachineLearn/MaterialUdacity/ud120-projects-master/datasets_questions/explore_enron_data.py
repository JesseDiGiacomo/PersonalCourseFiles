#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


list_name = dict.keys(enron_data)

#print "Numero de pessoas inscritas: ", len(list_name)

#print "Nome das pessoas inscritas: ", list_name

x = list_name.index
i = 0

for x in list_name:
    if (enron_data[x]["poi"] == True):
        i = i +1


print "Numero de pessoas com POI positivo: ", i

poi_list = open("../final_project/poi_names.txt").readlines()
#print poi_list

#print "Numero de pessoas na lista de POIs: ", len(poi_list)-2

#print "Total de acoes de James Prentice: ", enron_data["PRENTICE JAMES"]["total_stock_value"]

#print "Total de mensagens de email de Wesley Colwell para POIs: ", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

#print "Valor das opcoes de acoes exercidas por Jeffrey K Skilling: ", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

#print "Total payments Jeffrey Skilling: ", enron_data["SKILLING JEFFREY K"]["total_payments"]

#print "Total payments Kenneth Lay: ", enron_data["LAY KENNETH L"]["total_payments"]

#print "Total payments Andrew Fastow: ", enron_data["FASTOW ANDREW S"]["total_payments"]


j = 0

for x in list_name:
    if (enron_data[x]["salary"] != "NaN"):
        j = j +1


#print "Numero de pessoas com salario: ", j


k = 0

for x in list_name:
    if (enron_data[x]["email_address"] != "NaN"):
        k = k +1


#print "Numero de pessoas com email ", k


l = 0

for x in list_name:
    if (enron_data[x]["total_payments"] == "NaN"):
        l = l +1


#print "Numero de pessoas sem dados de pagamento: ", l

y = poi_list.index
m = 0

for y in list_name:
    if (enron_data[x]["total_payments"] == "NaN"):
        m = m +1


#print "Numero de POIs sem dados de pagamento: ", m
