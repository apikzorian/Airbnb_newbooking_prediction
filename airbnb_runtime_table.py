from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from ndcg_scoring import make_ndcg_scorer
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from datetime import datetime, date
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedShuffleSplit
from IPython.display import display
import gc


accuracy_ndcg = pd.read_pickle('accuracy1.pickle')
runtime = pd.read_pickle('runtime1.pickle')

model1 = {}
# value = {}
# kag = {'dt': 0.75291, 'logr': 0.84852, 'rf': 0.85352, 'rf_gd': 0.86449, 'xgb': 1.0, 'xgb_gd': 1.0}
# desc = {'dt': 'Decision Tree', 'logr': 'Logistic Regression',
#         'rf': 'Random Forest', 'rf_gd': 'Random Forest - Best Estimator',
#         'xgb': 'XGBoost', 'xgb_gd': 'XGBoost - Best Estimator'}
# for j in accuracy_ndcg.keys():
#     if desc[j[0]] not in model1.keys():
#         value = {}
#         value['Runtime(s)'] = runtime[j[0]][0]
#         if j[0] in kag.keys():
#             value['kaggle_nDCG'] = kag[j[0]]
#     value[j[1]] = accuracy_ndcg[j]
#     model1[desc[j[0]]] = value
#     print(pd.DataFrame(model1).T)

final_dict = {}

desc = {'dt': 'Decision Tree', 'logr': 'Logistic Regression',
        'rf': 'Random Forest', 'rf_gd': 'Random Forest - Best Estimator',
        'xgb': 'XGBoost', 'xgb_gd': 'XGBoost - Best Estimator'}
kag = {'dt': 0.75291, 'logr': 0.84852, 'rf': 0.85352, 'rf_gd': 0.86449, 'xgb': 1.0, 'xgb_gd': 1.0}
processed = []
for d, k in accuracy_ndcg.items():
    clf_name = d[0]
    if clf_name in processed:
        continue
    value = {}
    print(d)
    if d[1] == 'nDCG':
        score = 'Accuracy'
    else:
        score = 'nDCG'
    clf_name = d[0]
    d1 = accuracy_ndcg[(clf_name, d[1])]
    d2 = accuracy_ndcg[(clf_name, score)]
    k_val = kag[clf_name]
    print(d2)
    print(k)
    value[d[1]] = d1
    value[score] = d2
    value['kaggle_nDCG'] = kag[clf_name]
    value['Runtime(s)'] = runtime[clf_name][0]
    final_dict[desc[clf_name]] = value
    processed.append(clf_name)
    print(pd.DataFrame(final_dict).T)

print("esh")