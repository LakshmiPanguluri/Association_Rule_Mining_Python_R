#Apriori

#Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Importing the dataset
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header= None)

transactions = []
for i in range(0,7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0,20)])

#Why this is not responding at all- we are not getting nan in quotes here
'''transactions = []
for i in range(0,7501):
    transactions.append([dataset.values[i,j] for j in range(0,20)])'''

# Apriori

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Data Preprocessing
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
transactions = []
for i in range(0, 7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])

# Training Apriori on the dataset
from apyori import apriori
rules = apriori(transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2)

# Visualising the results
results = list(rules)

myresults= [list(x) for x in results]
myRes = []
for j in range(0, 153):
    myRes.append([list(x) for x in myresults[j][2]])    
                     