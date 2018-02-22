'''

'''

__author__ = "Celso M. de Melo"
__email__ = "celsodemelo@eleveninc.com"

import os.path

import pandas as pd
import numpy as np

import predictions.labels

if not os.path.isfile('games_3_points.csv'):
    df = pd.read_csv('../../data/games.csv')

    predictions.labels.add_numerical_label(df)
    df = df[df.total_three_points != -1]
    predictions.labels.add_classification_labels(df)

    df.to_csv('games_3_points.csv', index=False)
else:
    df = pd.read_csv('games_3_points.csv')

if not os.path.isfile('train_eval.csv'):
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
    print('Done.')
