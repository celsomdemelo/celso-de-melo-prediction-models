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

if not os.path.isfile('../data/games_with_labels.csv'):
    df = pd.read_csv('../data/games.csv')

    predictions.labels.add_numerical_label(df)
    df = df[df.total_three_points != -1]  # Assuming that if 3-pts is missing, the others are too (and vice-versa)
    predictions.labels.add_classification_labels(df)

    df.to_csv('../data/games_with_labels.csv', index=False)
else:
    df = pd.read_csv('../data/games_with_labels.csv')

if not os.path.isfile('../data/train_eval.csv'):
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
    df_train_eval.to_csv('../data/train_eval.csv', index=False)
    df_train.to_csv('../data/train.csv', index=False)
    df_eval.to_csv('../data/eval.csv', index=False)
    df_test.to_csv('../data/test.csv', index=False)
else:
    print('Reading CSV files...')
    df_train_eval = pd.read_csv('../data/train_eval.csv')
    df_train = pd.read_csv('../data/train.csv')
    df_eval = pd.read_csv('../data/eval.csv')
    df_test = pd.read_csv('../data/test.csv')
print('Done.')

labels = ['total_three_points', 'h_three_points_made', 'a_three_points_made',
          'total_three_points_att', 'h_three_points_att', 'a_three_points_att',
          'h_three_points_pct', 'a_three_points_pct',
          'total_free_throws', 'h_free_throws_made', 'a_free_throws_made',
          'h_free_throws_pct', 'a_free_throws_pct',
          'total_rebounds', 'h_rebounds', 'a_rebounds',
          'total_offensive_rebounds', 'h_offensive_rebounds', 'a_offensive_rebounds',
          'total_assists', 'h_assists', 'a_assists',
          'total_field_goals_att', 'h_field_goals_att', 'a_field_goals_att',
          'h_field_goals_pct', 'a_field_goals_pct',
          'total_possessions', 'h_possessions', 'a_possessions']

print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('TRAINING')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
for label in labels:
    print('-----------------------------------')
    print('LABEL: ' + label)
    predictions.models.glm_ols.find_best_model(predictions.feature_sets.features_1, label, df_train, df_eval)

print('\n\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('SCORE ON TEST SET')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
for label in labels:
    print('-----------------------------------')
    print('LABEL: ' + label)
    predictions.models.glm_ols.score_on_test_set(predictions.feature_sets.features_1, label, df_train_eval,
                                             df_test, path='models/' + label + '.pkl')