'''

'''

__author__ = "Celso M. de Melo"
__email__ = "celsodemelo@eleveninc.com"

import os.path

import pandas as pd
import numpy as np

import predictions.labels
import predictions.models.glm_ols
import predictions.feature_sets

print('Reading CSV files...')
# df_train_eval = pd.read_csv('../../data/train_eval.csv')
df_train = pd.read_csv('../../data/train.csv')
df_eval = pd.read_csv('../../data/eval.csv')
# df_test = pd.read_csv('../../data/test.csv')
print('Done.')

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression
from sklearn.feature_selection import mutual_info_regression
from predictions.feature_sets import clean_df
from predictions.utils import sort_coef, get_ordered_best_features

print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('BEST K FEATURES')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
ordered_bfs = get_ordered_best_features(predictions.feature_sets.features_5, df_train)
for of in ordered_bfs:
    print(of)

print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('TRAINING')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
funcs = [f_regression,
         # mutual_info_regression
         ]
func_labels = ['f_regression',
               # 'mutual_info_regression'
               ]
for label in predictions.labels.labels_for_feature_selection:
    print('-----------------------------------')
    print('LABEL: ' + label)

    features = predictions.feature_sets.features_5

    df_train_clean = clean_df(df_train, features + [label])
    df_eval_clean = clean_df(df_eval, features + [label])

    results = []
    for idx, func_label in enumerate(func_labels):
        print('----------------')
        print('func_label: ' + func_label)
        for k in range(1, len(features) + 1):
            print('----------------')
            print('k: ' + str(k))
            selector = SelectKBest(funcs[idx], k=k)
            selector.fit(df_train_clean[features], df_train_clean[label])
            idxs_selected = selector.get_support(indices=True)
            idxs_selected = [i for i in idxs_selected if i < len(features)] # Prevent bug: Index out of bounds
            df_train_selected = df_train_clean.iloc[:, idxs_selected]
            print(df_train_selected.columns)

            selected_features = list(df_train_selected.columns)
            result = predictions.models.glm_ols.find_best_model(selected_features, label, df_train, df_eval,
                                                                verbose=True, scale=False)
            results.append(
                'features_5 (' + func_label + ', best ' + str(k) + ')\t' + str(result[1]) + '\t' + str(
                    result[2]))
            # sorted_coefs = sort_coef(features, result[0].coef_)
            # for k in sorted_coefs:
            #     print(k[0] + '\t' + str(k[1]))
    for r in results:
        print(r)

# for label in predictions.labels.labels_to_predict_2nd_half:
#     print('-----------------------------------')
#     print('LABEL: ' + label + ' (2nd-half)')
#     predictions.models.glm_ols.find_best_model(predictions.feature_sets.features_ht_1, label, df_train, df_eval)
