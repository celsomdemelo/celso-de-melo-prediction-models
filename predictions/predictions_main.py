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
    {'away': 'Gonzaga', 'home': 'BYU',
     'half_time_stats': {'both_h1_points': 0, 'both_h1_three_att': 0, 'both_h1_three': 0, 'both_h1_two_att': 0,
                         'both_h1_two': 0, 'both_h1_free_att': 0, 'both_h1_free': 0, 'both_h1_off_rebounds': 0}},
    {'away': 'Auburn', 'home': 'Florida',
     'half_time_stats': {'both_h1_points': 0, 'both_h1_three_att': 0, 'both_h1_three': 0, 'both_h1_two_att': 0,
                         'both_h1_two': 0, 'both_h1_free_att': 0, 'both_h1_free': 0, 'both_h1_off_rebounds': 0}},
    {'away': 'Arizona', 'home': 'Oregon',
     'half_time_stats': {'both_h1_points': 0, 'both_h1_three_att': 0, 'both_h1_three': 0, 'both_h1_two_att': 0,
                         'both_h1_two': 0, 'both_h1_free_att': 0, 'both_h1_free': 0, 'both_h1_off_rebounds': 0}},
    {'away': 'Villanova', 'home': 'Creighton',
     'half_time_stats': {'both_h1_points': 0, 'both_h1_three_att': 0, 'both_h1_three': 0, 'both_h1_two_att': 0,
                         'both_h1_two': 0, 'both_h1_free_att': 0, 'both_h1_free': 0, 'both_h1_off_rebounds': 0}},
    {'away': 'Kansas', 'home': 'Texas Tech',
     'half_time_stats': {'both_h1_points': 0, 'both_h1_three_att': 0, 'both_h1_three': 0, 'both_h1_two_att': 0,
                         'both_h1_two': 0, 'both_h1_free_att': 0, 'both_h1_free': 0, 'both_h1_off_rebounds': 0}},
]

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
print('PREDICTIONS')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
for label in labels:
    print('-----------------------------------')
    print('LABEL: ' + label)
    for idx, game in enumerate(games):
        print('\t' + game['away'] + ' x ' + game['home'] + ': ' +
              str(make_prediction(away_name=game['away'], home_name=game['home'],
                                  path='models/' + label + '.pkl',
                                  season_stats_names=predictions.feature_sets.features_1)))

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
for idx, game in enumerate(games):
    print('\t' + game['away'] + ' x ' + game['home'])
    for label in labels:
        print(str(make_prediction(away_name=game['away'], home_name=game['home'],
                                                       path='models/' + label + '.pkl',
                                                       season_stats_names=predictions.feature_sets.features_1)[0]))
