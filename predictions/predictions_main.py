__author__ = "Celso M. de Melo"
__email__ = "celsodemelo@eleveninc.com"

from sklearn.externals import joblib
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

def make_prediction(home_name, away_name, path, season_stats_names, extra_features={}):
    home_stats = season_stats[home_name]
    away_stats = season_stats[away_name]

    args = []
    for f in season_stats_names:
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


games = [
    # {'away': 'Wake Forest', 'home': 'Syracuse',
    #  'half_time_stats': {'a_h1_points':24,
    #                      'a_h1_three':1,'a_h1_three_att':13,
    #                      'a_h1_two':10,'a_h1_two_att':18,
    #                      'a_h1_free':1,'a_h1_free_att':1,
    #                      'a_h1_off_rebounds':5,'a_h1_rebounds':16,
    #                      'a_h1_assists':7,'a_h1_blocks':2,'a_h1_turnovers':8,'a_h1_fouls':6,
    #                      'h_h1_points':30,
    #                      'h_h1_three':2,'h_h1_three_att':11,
    #                      'h_h1_two':9,'h_h1_two_att':13,
    #                      'h_h1_free':6,'h_h1_free_att':8,
    #                      'h_h1_off_rebounds':3,'h_h1_rebounds':16,
    #                      'h_h1_assists':3,'h_h1_blocks':2,'h_h1_turnovers':9,'h_h1_fouls':7,
    #                     'both_h1_points':54,
    #                     'both_h1_three':3,'both_h1_three_att':24,
    #                     'both_h1_two':19,'both_h1_two_att':31,
    #                     'both_h1_free':7,'both_h1_free_att':9,
    #                     'both_h1_off_rebounds':8,
    #                     'both_h1_rebounds':32,
    #                     'both_h1_assists':10,
    #                     'both_h1_blocks':4,
    #                     'both_h1_turnovers':17,
    #                     'both_h1_fouls':13,
    #                      }},
    # {'away': 'BYU', 'home': 'Gonzaga',
    #  'half_time_stats': {'a_h1_points':24,
    #                      'a_h1_three':1,'a_h1_three_att':13,
    #                      'a_h1_two':10,'a_h1_two_att':18,
    #                      'a_h1_free':1,'a_h1_free_att':1,
    #                      'a_h1_off_rebounds':5,'a_h1_rebounds':16,
    #                      'a_h1_assists':7,'a_h1_blocks':2,'a_h1_turnovers':8,'a_h1_fouls':6,
    #                      'h_h1_points':30,
    #                      'h_h1_three':2,'h_h1_three_att':11,
    #                      'h_h1_two_att':9,'h_h1_two':13,
    #                      'h_h1_free':6,'h_h1_free_att':8,
    #                      'h_h1_off_rebounds':3,'h_h1_rebounds':16,
    #                      'h_h1_assists':3,'h_h1_blocks':2,'h_h1_turnovers':9,'h_h1_fouls':7,
    #                     'both_h1_points':0,
    #                     'both_h1_three_att':0,
    #                     'both_h1_three':0,
    #                     'both_h1_two_att':0,
    #                     'both_h1_two':0,
    #                     'both_h1_free_att':0,
    #                     'both_h1_free':0,
    #                     'both_h1_off_rebounds':0,
    #                     'both_h1_rebounds':0,
    #                     'both_h1_assists':0,
    #                     'both_h1_blocks':0,
    #                     'both_h1_turnovers':0,
    #                     'both_h1_fouls':0,
    #                      }},
    {'away': 'Texas', 'home': 'Texas Tech',
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
                            'both_h1_points':63,
                            'both_h1_three':9,'both_h1_three_att':21,
                            'both_h1_two':13,'both_h1_two_att':38,
                            'both_h1_free':10,'both_h1_free_att':12,
                            'both_h1_off_rebounds':10,'both_h1_rebounds':34,
                            'both_h1_assists':9,
                            'both_h1_blocks':4,
                            'both_h1_turnovers':9,
                            'both_h1_fouls':18,
                             }},
]

print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('PREDICTIONS')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
for label in predictions.labels.labels_to_predict:
    print('-----------------------------------')
    print('LABEL: ' + label)
    for idx, game in enumerate(games):
        print('\t' + game['away'] + ' x ' + game['home'] + ': ' +
              str(make_prediction(away_name=game['away'], home_name=game['home'],
                                  path='models/full-time/' + label + '.pkl',
                                  season_stats_names=predictions.feature_sets.features_1_h_and_a)))

for label in predictions.labels.labels_to_predict_2nd_half:
    print('-----------------------------------')
    print('LABEL: ' + label + ' (2nd-half)')
    for idx, game in enumerate(games):
        print('\t' + game['away'] + ' x ' + game['home'] + ': ' +
              str(make_prediction(away_name=game['away'], home_name=game['home'],
                                  path='models/2nd-half/' + label + '.pkl',
                                  season_stats_names=predictions.feature_sets.features_ht_1_h_and_a_and_both,
                                  extra_features=game['half_time_stats'])))

print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('PREDICTIONS (SPREADSHEET-FRIENDLY FORMAT')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('FULL-TIME')
for idx, game in enumerate(games):
    print('\t' + game['away'] + ' x ' + game['home'])
    for label in predictions.labels.labels_to_predict:
        print(str(make_prediction(away_name=game['away'], home_name=game['home'],
                                  path='models/full-time/' + label + '.pkl',
                                  season_stats_names=predictions.feature_sets.features_1_h_and_a)[0]))
print('2nd-HALF')
for idx, game in enumerate(games):
    print('\t' + game['away'] + ' x ' + game['home'])
    for label in predictions.labels.labels_to_predict_2nd_half:
        print(str(make_prediction(away_name=game['away'], home_name=game['home'],
                                  path='models/2nd-half/' + label + '.pkl',
                                  season_stats_names=predictions.feature_sets.features_ht_1_h_and_a_and_both,
                                  extra_features=game['half_time_stats'])[0]))
