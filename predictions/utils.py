'''
General utility functions
'''

__author__ = "Celso M. de Melo"
__email__ = "celsodemelo@eleveninc.com"

import operator

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression
from predictions.feature_sets import clean_df

def sort_coef(features, coefs):
    pairs = dict()
    for idx, val in enumerate(features):
        pairs[val] = coefs[idx]

    return sorted(pairs.items(), key=operator.itemgetter(1), reverse=True)


def get_ordered_best_features(features, df_train, label='both_three_points_made'):
    ordered_bfs = []

    df_train_clean = clean_df(df_train, features + [label])

    for k in range(1, len(features) + 1):
        selector = SelectKBest(f_regression, k=k)
        selector.fit(df_train_clean[features], df_train_clean[label])
        idxs_selected = selector.get_support(indices=True)
        idxs_selected = [i for i in idxs_selected if i < len(features)] # Prevent bug: Index out of bounds
        df_train_selected = df_train_clean.iloc[:, idxs_selected]
        selected_features = list(df_train_selected.columns)
        for f in selected_features:
            if f not in ordered_bfs:
                ordered_bfs.append(f)
                break

    return ordered_bfs
