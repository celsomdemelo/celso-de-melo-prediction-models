__author__ = "Celso M. de Melo"
__email__ = "celsodemelo@eleveninc.com"

from sklearn.externals import joblib
import pickle

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
    {'away': 'Purdue', 'home': 'Illinois',
     'half_time_stats': {'both_h1_points': 81, 'both_h1_three_att': 25, 'both_h1_three': 12, 'both_h1_two_att': 60,
                         'both_h1_two': 32, 'both_h1_free_att': 7, 'both_h1_free': 5, 'both_h1_off_rebounds': 9}},
    {'away': 'Gonzaga', 'home': 'San Diego',
     'half_time_stats': {'both_h1_points': 71, 'both_h1_three_att': 19, 'both_h1_three': 9, 'both_h1_two_att': 40,
                         'both_h1_two': 17, 'both_h1_free_att': 13, 'both_h1_free': 10, 'both_h1_off_rebounds': 14}},
    {'away': 'Connecticut', 'home': 'Cincinnati',
     'half_time_stats': {'both_h1_points': 63, 'both_h1_three_att': 24, 'both_h1_three': 8, 'both_h1_two_att': 35,
                         'both_h1_two': 17, 'both_h1_free_att': 9, 'both_h1_free': 5, 'both_h1_off_rebounds': 12}},
]

print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('PREDICTIONS')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('BOTH teams: Full-time 3-pointers (NO half-time measures)')
for idx, game in enumerate(games):
    print('\t' + game['away'] + ' x ' + game['home'] + ': ' +
          str(make_prediction(away_name=game['away'], home_name=game['home'],
                              path='3-points/full_time_3_pts_model.pkl',
                              season_stats_names=predictions.feature_sets.features_1)))

# print('\nBOTH teams: Full-time 3-pointers (WITH half-time measures)')
# for idx, game in enumerate(games):
#     print('\t' + game['away'] + ' x ' + game['home'] + ': ' +
#           str(make_prediction(away_name=game['away'], home_name=game['home'],
#                               path='3-points/full_time_ht_3_pts_model.pkl',
#                               season_stats_names=predictions.feature_sets.features_1,
#                               extra_features=game['half_time_stats'])))

print('\nBOTH teams: 2nd-half 3-pointers')
for idx, game in enumerate(games):
    print('\t' + game['away'] + ' x ' + game['home'] + ': ' +
          str(make_prediction(away_name=game['away'], home_name=game['home'],
                              path='3-points/2nd_half_3_pts_model.pkl',
                              season_stats_names=predictions.feature_sets.features_1,
                              extra_features=game['half_time_stats'])))
