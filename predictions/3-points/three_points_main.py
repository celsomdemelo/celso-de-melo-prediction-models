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

if not os.path.isfile('games_3_points.csv'):
    df = pd.read_csv('../../data/games.csv')

    predictions.labels.add_numerical_label(df)
    df = df[df.total_three_points != -1]
    predictions.labels.add_classification_labels(df)

    df.to_csv('games_3_points.csv', index=False)
else:
    df = pd.read_csv('games_3_points.csv')

if not os.path.isfile('train_eval.csv'):
    print('Creating CSV files...')
    # Split into train+evaluation and test sets
    df_train_eval, df_test = np.split(df.sample(frac=1), [int(.8 * len(df))])

    # Split into train and evaluation sets
    df_train, df_eval = np.split(df_train_eval.sample(frac=1), [int(.8 * len(df_train_eval))])

    # Shuffle
    df_train_eval = df_train_eval.sample(frac=1)
    df_train = df_train.sample(frac=1)
    df_eval = df_eval.sample(frac=1)
    df_test = df_test.sample(frac=1)

    print('Created sets:')
    print('\tTrain + eval: ' + str(len(df_train_eval)))
    print('\tTrain: ' + str(len(df_train)))
    print('\tEval: ' + str(len(df_eval)))
    print('\tTest: ' + str(len(df_test)))

    # Save CVS files
    print('Saving files...')
    df_train_eval.to_csv('train_eval.csv', index=False)
    df_train.to_csv('train.csv', index=False)
    df_eval.to_csv('eval.csv', index=False)
    df_test.to_csv('test.csv', index=False)
else:
    print('Reading CSV files...')
    df_train_eval = pd.read_csv('train_eval.csv')
    df_train = pd.read_csv('train.csv')
    df_eval = pd.read_csv('eval.csv')
    df_test = pd.read_csv('test.csv')
print('Done.')

print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('TRAINING')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('BOTH teams: Full-time 3-pointers (NO half-time measures)')
predictions.models.glm_ols.find_best_model(predictions.feature_sets.features_1, 'total_three_points', df_train, df_eval)

print('\nBOTH teams: Full-time 3-pointers (WITH half-time measures)')
predictions.models.glm_ols.find_best_model(predictions.feature_sets.features_ht_1, 'total_three_points', df_train, df_eval)

print('\nBOTH teams: 2nd-half 3-pointers')
predictions.models.glm_ols.find_best_model(predictions.feature_sets.features_ht_1, 'total_three_points', df_train, df_eval)

print('\n\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('SCORE ON TEST SET')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('BOTH teams: Full-time 3-pointers (NO half-time measures)')
predictions.models.glm_ols.score_on_test_set(predictions.feature_sets.features_1, 'total_three_points', df_train_eval,
                                             df_test, path='full_time_3_pts_model.pkl')

print(' \nBOTH teams: Full-time 3-pointers (WITH half-time measures)')
predictions.models.glm_ols.score_on_test_set(predictions.feature_sets.features_ht_1, 'total_three_points', df_train_eval,
                                             df_test, path='full_time_ht_3_pts_model.pkl')

print('\nBOTH teams: 2nd-half 3-pointers')
predictions.models.glm_ols.score_on_test_set(predictions.feature_sets.features_ht_1, 'both_h2_three', df_train_eval,
                                             df_test, path='2nd_half_3_pts_model.pkl')