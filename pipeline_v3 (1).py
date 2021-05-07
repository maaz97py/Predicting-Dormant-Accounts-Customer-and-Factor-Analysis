# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 16:59:18 2021

@author: prahn
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy, dill  
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer,make_column_transformer
from sklearn.preprocessing import StandardScaler,OneHotEncoder,LabelEncoder
from sklearn.ensemble import RandomForestClassifier as RF
from sklearn.model_selection import train_test_split as tts
from sklearn import metrics
import pickle

#dill.load_session('final_pipeline.pkl')
path = ("E://Python/360digitmg/Assignments/DS - Project/Data_TarImp_CleanOutlier.csv")

TarImp = pd.read_csv(path).iloc[:,1:]
#This dataset is cleaned. No dummy variables or standardization done

output = TarImp['Current Status']
TarImp.drop('Current Status', axis = 1, inplace = True)
le = LabelEncoder()
le = le.fit(output)
y1 = le.transform(output)

numeric_features = ['Age', 'Opening balance', 'Current balance',
                    'Dist of residence from the bank', 'Quarterly activity rate',
                    'Months since last transaction']
numeric_transformer = StandardScaler()


categorical_features = ['Gender', 'Education', 'Occupation', 'Account type',
       'Have minimum balance?', 'Have multiple accounts?',
       'Own an active loan?', 'Use internet or mobile banking?',
       'Has an active credit Card?', 'Ever defaulted on a loan?',
       'Satisfied with bank service?', 'Any transaction in the past 24 months']

categorical_transformer1 = OneHotEncoder(handle_unknown='ignore')

processor = ColumnTransformer(
        transformers=[('cat', categorical_transformer1, categorical_features),
            ('num', numeric_transformer, numeric_features)])

model = RF(class_weight= None,criterion ='entropy', max_depth = 6,
           max_features = 0.9,min_samples_split = 20, n_estimators = 200,
           random_state=0)


pipe1 = Pipeline(steps=[('processor', processor),
                        ('classifier', model)])


train_x, test_x, train_y, test_y = tts(TarImp, y1, test_size=0.2,random_state = 41)

pipe1.fit(train_x,train_y)

pred_p = pipe1.predict(train_x)
eval_p = pipe1.predict(test_x)

print(metrics.classification_report(train_y,pred_p))
print(metrics.classification_report(test_y,eval_p))


#Feature Importances
pipe1.named_steps['classifier'].feature_importances_
pipe1.named_steps['classifier'].coef_
feats = {} # a dict to hold feature_name: feature_importance
for feature, importance in zip(train_x.columns, pipe1.named_steps['classifier'].feature_importances_):
    feats[feature] = importance #add the name/value pair 
importances = pd.DataFrame.from_dict(feats, orient='index')
importances = importances.sort_values(0, ascending=False)

dill.dump_session('final_pipeline.pkl')

pickle.dump(pipe1,open('model_rf_final.pkl','wb'))