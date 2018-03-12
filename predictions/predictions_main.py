__author__ = "Celso M. de Melo"
__email__ = "celsodemelo@eleveninc.com"

from sklearn.externals import joblib
import pandas as pd
import numpy as np
import pickle

import predictions.labels
import predictions.feature_sets
import predictions.models.glm_ols

pickle_in = open("../data/season_stats_2017.pkl", "rb")
season_stats = pickle.load(pickle_in)


def make_prediction_old(home_name, away_name, path, season_stats_names, extra_features={}):
    home_stats = season_stats[home_name]
    away_stats = season_stats[away_name]

    args = []
    for f in season_stats_names:
        stat = f[5:]  # Get rid of 'both_'
        args.append((home_stats[stat] + away_stats[stat]) / 2.0)

    regr = joblib.load(path)
    features = np.array(args + list(extra_features.values()))
    return regr.predict(features.reshape(1, -1))

def make_prediction(home_name, away_name, path, features, extra_features={}):
    home_stats = season_stats[home_name]
    away_stats = season_stats[away_name]

    args = []
    for f in features:
        if '_h1_' in f:
            continue

        stat = f[2:]  # Get rid of 'h_' or '_a'
        if f[:2] == 'h_':
            args.append(home_stats[stat])
        elif f[:2] == 'a_':
            args.append(away_stats[stat])

    regr = joblib.load(path)
    features = np.array(args + list(extra_features.values()))
    return regr.predict(features.reshape(1, -1))

def make_prediction_neutral_ground(home_name, away_name, path, features, extra_features={}):
    predictions_1 = make_prediction(home_name, away_name, path, features, extra_features)
    predictions_2 = make_prediction(away_name, home_name, path, features, extra_features)
    return (predictions_1 + predictions_2) / 2.0

def calculate_percentiles(df, labels):
    ranks = dict()
    percentile_25th = dict()
    percentile_75th = dict()
    for label in labels:
        ranks[label] = df[label].rank(pct=True)

    for index, row in df.iterrows():
        for label in labels:
            if ranks[label][index] <= 0.25:
                if label in percentile_25th:
                    percentile_25th[label] = max(row[label], percentile_25th[label])
                else:
                    percentile_25th[label] = row[label]
            elif ranks[label][index] >= 0.75:
                if label in percentile_75th:
                    percentile_75th[label] = min(row[label], percentile_75th[label])
                else:
                    percentile_75th[label] = row[label]

    return percentile_25th, percentile_75th


games = [
    {'away': 'LIU Brooklyn', 'home': 'Radford',
         'half_time_stats': {'a_h1_points':28,
                             'a_h1_three':2,'a_h1_three_att':10,
                             'a_h1_two':9,'a_h1_two_att':21,
                             'a_h1_free':4,'a_h1_free_att':4,
                             'a_h1_off_rebounds':5,'a_h1_rebounds':14,
                             'a_h1_assists':3,'a_h1_blocks':3,'a_h1_turnovers':4,'a_h1_fouls':8,
                             'h_h1_points':35,
                             'h_h1_three':7,'h_h1_three_att':11,
                             'h_h1_two':4,'h_h1_two_att':17,
                             'h_h1_free':6,'h_h1_free_att':8,
                             'h_h1_off_rebounds':5,'h_h1_rebounds':20,
                             'h_h1_assists':6,'h_h1_blocks':1,'h_h1_turnovers':5,'h_h1_fouls':10,
                            # 'both_h1_points':63,
                            # 'both_h1_three':9,'both_h1_three_att':21,
                            # 'both_h1_two':13,'both_h1_two_att':38,
                            # 'both_h1_free':10,'both_h1_free_att':12,
                            # 'both_h1_off_rebounds':10,'both_h1_rebounds':34,
                            # 'both_h1_assists':9,
                            # 'both_h1_blocks':4,
                            # 'both_h1_turnovers':9,
                            # 'both_h1_fouls':18,
                             }},
    {'away': 'St. Bonaventure', 'home': 'UCLA',
         'half_time_stats': {'a_h1_points':28,
                             'a_h1_three':2,'a_h1_three_att':10,
                             'a_h1_two':9,'a_h1_two_att':21,
                             'a_h1_free':4,'a_h1_free_att':4,
                             'a_h1_off_rebounds':5,'a_h1_rebounds':14,
                             'a_h1_assists':3,'a_h1_blocks':3,'a_h1_turnovers':4,'a_h1_fouls':8,
                             'h_h1_points':35,
                             'h_h1_three':7,'h_h1_three_att':11,
                             'h_h1_two':4,'h_h1_two_att':17,
                             'h_h1_free':6,'h_h1_free_att':8,
                             'h_h1_off_rebounds':5,'h_h1_rebounds':20,
                             'h_h1_assists':6,'h_h1_blocks':1,'h_h1_turnovers':5,'h_h1_fouls':10,
                            # 'both_h1_points':63,
                            # 'both_h1_three':9,'both_h1_three_att':21,
                            # 'both_h1_two':13,'both_h1_two_att':38,
                            # 'both_h1_free':10,'both_h1_free_att':12,
                            # 'both_h1_off_rebounds':10,'both_h1_rebounds':34,
                            # 'both_h1_assists':9,
                            # 'both_h1_blocks':4,
                            # 'both_h1_turnovers':9,
                            # 'both_h1_fouls':18,
                             }},
    {'away': 'North Carolina Central', 'home': 'Texas Southern',
         'half_time_stats': {'a_h1_points':28,
                             'a_h1_three':2,'a_h1_three_att':10,
                             'a_h1_two':9,'a_h1_two_att':21,
                             'a_h1_free':4,'a_h1_free_att':4,
                             'a_h1_off_rebounds':5,'a_h1_rebounds':14,
                             'a_h1_assists':3,'a_h1_blocks':3,'a_h1_turnovers':4,'a_h1_fouls':8,
                             'h_h1_points':35,
                             'h_h1_three':7,'h_h1_three_att':11,
                             'h_h1_two':4,'h_h1_two_att':17,
                             'h_h1_free':6,'h_h1_free_att':8,
                             'h_h1_off_rebounds':5,'h_h1_rebounds':20,
                             'h_h1_assists':6,'h_h1_blocks':1,'h_h1_turnovers':5,'h_h1_fouls':10,
                            # 'both_h1_points':63,
                            # 'both_h1_three':9,'both_h1_three_att':21,
                            # 'both_h1_two':13,'both_h1_two_att':38,
                            # 'both_h1_free':10,'both_h1_free_att':12,
                            # 'both_h1_off_rebounds':10,'both_h1_rebounds':34,
                            # 'both_h1_assists':9,
                            # 'both_h1_blocks':4,
                            # 'both_h1_turnovers':9,
                            # 'both_h1_fouls':18,
                             }},
    {'away': 'Arizona State', 'home': 'Syracuse',
         'half_time_stats': {'a_h1_points':28,
                             'a_h1_three':2,'a_h1_three_att':10,
                             'a_h1_two':9,'a_h1_two_att':21,
                             'a_h1_free':4,'a_h1_free_att':4,
                             'a_h1_off_rebounds':5,'a_h1_rebounds':14,
                             'a_h1_assists':3,'a_h1_blocks':3,'a_h1_turnovers':4,'a_h1_fouls':8,
                             'h_h1_points':35,
                             'h_h1_three':7,'h_h1_three_att':11,
                             'h_h1_two':4,'h_h1_two_att':17,
                             'h_h1_free':6,'h_h1_free_att':8,
                             'h_h1_off_rebounds':5,'h_h1_rebounds':20,
                             'h_h1_assists':6,'h_h1_blocks':1,'h_h1_turnovers':5,'h_h1_fouls':10,
                            # 'both_h1_points':63,
                            # 'both_h1_three':9,'both_h1_three_att':21,
                            # 'both_h1_two':13,'both_h1_two_att':38,
                            # 'both_h1_free':10,'both_h1_free_att':12,
                            # 'both_h1_off_rebounds':10,'both_h1_rebounds':34,
                            # 'both_h1_assists':9,
                            # 'both_h1_blocks':4,
                            # 'both_h1_turnovers':9,
                            # 'both_h1_fouls':18,
                             }},
]

# print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
# print('PERCENTILES')
# print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
# df = pd.read_csv('../data/games.csv')
# df = df[df.season == 2017]
# print('FULL-TIME')
# percentile_25th, percentile_75th = calculate_percentiles(df, predictions.labels.labels_to_predict)
# for l in predictions.labels.labels_to_predict:
#     print(l + '\t' + str(percentile_25th[l]) + '\t' + str(percentile_75th[l]))
#
# print('2nd-HALF')
# percentile_25th, percentile_75th = calculate_percentiles(df, predictions.labels.labels_to_predict_2nd_half)
# for l in predictions.labels.labels_to_predict_2nd_half:
#     print(l + '\t' + str(percentile_25th[l]) + '\t' + str(percentile_75th[l]))

# print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
# print('PREDICTIONS')
# print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
# for label in predictions.labels.labels_to_predict:
#     print('-----------------------------------')
#     print('LABEL: ' + label)
#     for idx, game in enumerate(games):
#         print('\t' + game['away'] + ' x ' + game['home'] + ': ' +
#               str(make_prediction(away_name=game['away'], home_name=game['home'],
#                                   path='models/full-time/' + label + '.pkl',
#                                   features=predictions.feature_sets.features_6)))
#
# for label in predictions.labels.labels_to_predict_2nd_half:
#     print('-----------------------------------')
#     print('LABEL: ' + label + ' (2nd-half)')
#     for idx, game in enumerate(games):
#         print('\t' + game['away'] + ' x ' + game['home'] + ': ' +
#               str(make_prediction(away_name=game['away'], home_name=game['home'],
#                                   path='models/2nd-half/' + label + '.pkl',
#                                   features=predictions.feature_sets.features_ht_6,
#                                   extra_features=game['half_time_stats'])))

print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('PREDICTIONS (SPREADSHEET-FRIENDLY FORMAT')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('FULL-TIME')
for idx, game in enumerate(games):
    print('\t' + game['away'] + ' x ' + game['home'])
    for label in predictions.labels.labels_to_predict:
        print(str(make_prediction_neutral_ground(away_name=game['away'], home_name=game['home'],
                                  path='models/full-time/' + label + '.pkl',
                                  features=predictions.feature_sets.features_6)[0]))
# print('2nd-HALF')
# for idx, game in enumerate(games):
#     print('\t' + game['away'] + ' x ' + game['home'])
#     for label in predictions.labels.labels_to_predict_2nd_half:
#         print(str(make_prediction(away_name=game['away'], home_name=game['home'],
#                                   path='models/2nd-half/' + label + '.pkl',
#                                   features=predictions.feature_sets.features_ht_6,
#                                   extra_features=game['half_time_stats'])[0]))
