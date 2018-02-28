__author__ = "Celso M. de Melo"
__email__ = "celsodemelo@eleveninc.com"

from sklearn.externals import joblib
import pickle

import predictions.labels
import predictions.feature_sets
import predictions.models.glm_ols

pickle_in = open("../data/season_stats_2017.pkl", "rb")
season_stats = pickle.load(pickle_in)


def make_prediction(home_name, away_name, path, season_stats_names, extra_features={}):
    home_stats = season_stats[home_name]
    away_stats = season_stats[away_name]

    args = []
    for f in season_stats_names:
        stat = f[5:]  # Get rid of 'both_'
        args.append((home_stats[stat] + away_stats[stat]) / 2.0)

    regr = joblib.load(path)
    return regr.predict(args + list(extra_features.values()))


games = [
    {'away': 'Saint Joseph\'s (PA)', 'home': 'Rhode Island',
     'half_time_stats': {'both_h1_points': 51, 'both_h1_three_att': 23, 'both_h1_three': 6, 'both_h1_two_att': 56,
                         'both_h1_two': 20, 'both_h1_free_att': 9, 'both_h1_free': 5, 'both_h1_off_rebounds': 7,
                         'both_h1_rebounds': 29, 'both_h1_assists': 8, 'both_h1_blocks': 1, 'both_h1_turnovers': 11,
                         'both_h1_fouls': 12}},
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
                                  season_stats_names=predictions.feature_sets.features_1)))

for label in predictions.labels.labels_to_predict_2nd_half:
    print('-----------------------------------')
    print('LABEL: ' + label + ' (2nd-half)')
    for idx, game in enumerate(games):
        print('\t' + game['away'] + ' x ' + game['home'] + ': ' +
              str(make_prediction(away_name=game['away'], home_name=game['home'],
                                  path='models/2nd-half/' + label + '.pkl',
                                  season_stats_names=predictions.feature_sets.features_1,
                                  extra_features=game['half_time_stats'])))

# print('BOTH teams: Full-time 3-pointers (WITH half-time measures)')
# for idx, game in enumerate(games):
#     print('\t' + game['away'] + ' x ' + game['home'] + ': ' +
#           str(make_prediction(away_name=game['away'], home_name=game['home'],
#                               path='models/full_time_ht_3_pts_model.pkl',
#                               season_stats_names=predictions.feature_sets.features_1,
#                               extra_features=game['half_time_stats'])))

# print('BOTH teams: 2nd-half 3-pointers')
# for idx, game in enumerate(games):
#     print('\t' + game['away'] + ' x ' + game['home'] + ': ' +
#           str(make_prediction(away_name=game['away'], home_name=game['home'],
#                               path='models/2nd_half_3_pts_model.pkl',
#                               season_stats_names=predictions.feature_sets.features_1,
#                               extra_features=game['half_time_stats'])))

print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('PREDICTIONS (SPREADSHEET-FRIENDLY FORMAT')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('FULL-TIME')
for idx, game in enumerate(games):
    print('\t' + game['away'] + ' x ' + game['home'])
    for label in predictions.labels.labels_to_predict:
        print(str(make_prediction(away_name=game['away'], home_name=game['home'],
                                  path='models/full-time/' + label + '.pkl',
                                  season_stats_names=predictions.feature_sets.features_1)[0]))
print('2nd-HALF')
for idx, game in enumerate(games):
    print('\t' + game['away'] + ' x ' + game['home'])
    for label in predictions.labels.labels_to_predict_2nd_half:
        print(str(make_prediction(away_name=game['away'], home_name=game['home'],
                                  path='models/2nd-half/' + label + '.pkl',
                                  season_stats_names=predictions.feature_sets.features_1,
                                  extra_features=game['half_time_stats'])[0]))
