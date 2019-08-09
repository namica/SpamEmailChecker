# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 17:37:20 2019

@author: Naseem
"""

from NaiveBayes import Pool
import os
import json


def get_json(data):
    response = []
    for value in data:
        response.append({str(value[0]): value[1]})
    return json.dumps({"res": response})


DClasses = ["business", "entertainment", "politics", "sport", "tech", "spam"]
TClasses = ["spam"]

base = "learn/"
p = Pool()
for i in DClasses:
    p.learn(base + i, i)

base = "test/"
for i in TClasses:
    directory = os.listdir(base + i)
    for file in directory:
        res = p.Probability(base + i + "/" + file)
        print(i + ": " + file + ": " + str(get_json(res)))
