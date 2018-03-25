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


def save_train_eval_test_sets(df, train_eval_path, df_train_path, df_eval_path, df_test_path):
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
    df_train_eval.to_csv(train_eval_path, index=False)
    df_train.to_csv(df_train_path, index=False)
    df_eval.to_csv(df_eval_path, index=False)
    df_test.to_csv(df_test_path, index=False)

    return df_train_eval, df_train, df_eval, df_test


df = pd.read_csv('../data/games.csv')

TOURNAMENT_DATA_ONLY = False

train_eval_path = '../data/v2.1/train_eval.csv'
df_train_path = '../data/v2.1/train.csv'
df_eval_path = '../data/v2.1/eval.csv'
df_test_path = '../data/v2.1/test.csv'
# df_test_path = '../data/tournament/test.csv'
full_time_models_path = 'models/full-time/'
second_half_models_path = 'models/2nd-half/'

if TOURNAMENT_DATA_ONLY:
    df = df[df.tournament == 'NCAA']
    train_eval_path = '../data/tournament/train_eval.csv'
    df_train_path = '../data/tournament/train.csv'
    df_eval_path = '../data/tournament/eval.csv'
    df_test_path = '../data/tournament/test.csv'
    full_time_models_path = 'models/tournament/full-time/'
    second_half_models_path = 'models/tournament/2nd-half/'

if not os.path.isfile(train_eval_path):
    df_train_eval, df_train, df_eval, df_test = save_train_eval_test_sets(df, train_eval_path, df_train_path,
                                                                          df_eval_path, df_test_path)
else:
    print('Reading CSV files...')
    df_train_eval = pd.read_csv(train_eval_path)
    df_train = pd.read_csv(df_train_path)
    df_eval = pd.read_csv(df_eval_path)
    df_test = pd.read_csv(df_test_path)
print('Done.')


def print_detailed_scores(scores):
    for s in scores:
        print(s['label'] + '\t' + str(s['r2']) + '\t' +
              str(s['gt_acc']) + '\t' + str(s['gt_err']) + '\t' +
              str(s['rg_acc']) + '\t' + str(s['rg_err']) + '\t' +
              str(s['gt_70_acc']) + '\t' + str(s['gt_70_err']) + '\t' +
              str(s['gt_75_acc']) + '\t' + str(s['gt_75_err']))


print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('TRAINING')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
# for label in predictions.labels.labels_to_predict:
#     print('-----------------------------------')
#     print('LABEL: ' + label)
#     predictions.models.glm_ols.find_best_model(predictions.feature_sets.features_5, label, df_train, df_eval)
# for label in predictions.labels.labels_to_predict_2nd_half:
#     print('-----------------------------------')
#     print('LABEL: ' + label + ' (2nd-half)')
#     predictions.models.glm_ols.find_best_model(predictions.feature_sets.features_ht_5, label, df_train,
#                                                df_eval)

print('\n\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('SCORE ON TEST SET')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
detailed_scores = []
for label in predictions.labels.labels_to_predict:
    print('-----------------------------------')
    print('LABEL: ' + label)
    detailed_scores.append(
        predictions.models.glm_ols.score_on_test_set(predictions.feature_sets.features_6, label, df_train_eval,
                                                     df_test, path=full_time_models_path + label + '.pkl'))
print_detailed_scores(detailed_scores)

detailed_scores = []
for label in predictions.labels.labels_to_predict_2nd_half:
    print('-----------------------------------')
    print('LABEL: ' + label + ' (2nd-half)')
    detailed_scores.append(
        predictions.models.glm_ols.score_on_test_set(predictions.feature_sets.features_ht_6, label,
                                                     df_train_eval,
                                                     df_test, path=second_half_models_path + label + '.pkl'))
print_detailed_scores(detailed_scores)
