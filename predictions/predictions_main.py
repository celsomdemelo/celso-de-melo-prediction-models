__author__ = "Celso M. de Melo"
__email__ = "celsodemelo@eleveninc.com"

from sklearn.externals import joblib
import pandas as pd
import numpy as np
import pickle
import re

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


def calculate_first_half_stats(per_team_stats):
    per_team_stats['both_h1_points'] = per_team_stats['h_h1_points'] + per_team_stats['a_h1_points']
    per_team_stats['both_h1_three'] = per_team_stats['h_h1_three'] + per_team_stats['a_h1_three']
    per_team_stats['both_h1_three_att'] = per_team_stats['h_h1_three_att'] + per_team_stats['a_h1_three_att']
    per_team_stats['both_h1_two'] = per_team_stats['h_h1_two'] + per_team_stats['a_h1_two']
    per_team_stats['both_h1_two_att'] = per_team_stats['h_h1_two_att'] + per_team_stats['a_h1_two_att']
    per_team_stats['both_h1_free'] = per_team_stats['h_h1_free'] + per_team_stats['a_h1_free']
    per_team_stats['both_h1_free_att'] = per_team_stats['h_h1_free_att'] + per_team_stats['a_h1_free_att']
    per_team_stats['both_h1_off_rebounds'] = per_team_stats['h_h1_off_rebounds'] + per_team_stats['a_h1_off_rebounds']
    per_team_stats['both_h1_rebounds'] = per_team_stats['h_h1_rebounds'] + per_team_stats['a_h1_rebounds']
    per_team_stats['both_h1_assists'] = per_team_stats['h_h1_assists'] + per_team_stats['a_h1_assists']
    per_team_stats['both_h1_blocks'] = per_team_stats['h_h1_blocks'] + per_team_stats['a_h1_blocks']
    per_team_stats['both_h1_turnovers'] = per_team_stats['h_h1_turnovers'] + per_team_stats['a_h1_turnovers']
    per_team_stats['both_h1_fouls'] = per_team_stats['h_h1_fouls'] + per_team_stats['a_h1_fouls']

    return per_team_stats


def half_time_stats_from_ncaa_string(ncaa_string, prefix):
    ncaa_string = ncaa_string[7:]
    ns = re.findall(r"[\w']+", ncaa_string)
    ns = list(map(int, ns))

    return {prefix + '_h1_points': ns[13],
            prefix + '_h1_three': ns[2],
            prefix + '_h1_three_att': ns[3],
            prefix + '_h1_two': ns[0] - ns[2],
            prefix + '_h1_two_att': ns[1] - ns[3],
            prefix + '_h1_free': ns[4],
            prefix + '_h1_free_att': ns[5],
            prefix + '_h1_off_rebounds': ns[6],
            prefix + '_h1_rebounds': ns[7],
            prefix + '_h1_assists': ns[8],
            prefix + '_h1_blocks': ns[10],
            prefix + '_h1_turnovers': ns[11],
            prefix + '_h1_fouls': ns[12], }


games = [
    {'away': 'LIU Brooklyn', 'home': 'Radford',
     'away_ht_ncaa_string': 'TOTAL		25-58	7-18	12-15	10	27	9	6	4	7	18	69',
     'home_ht_ncaa_string': 'TOTAL		26-55	9-16	12-18	11	35	13	5	3	9	19	73',
     },
    {'away': 'St. Bonaventure', 'home': 'UCLA',
     'away_ht_ncaa_string': 'TOTAL		25-58	7-18	12-15	10	27	9	6	4	7	18	69',
     'home_ht_ncaa_string': 'TOTAL		26-55	9-16	12-18	11	35	13	5	3	9	19	73',
     },
    {'away': 'North Carolina Central', 'home': 'Texas Southern',
     'away_ht_ncaa_string': 'TOTAL		25-58	7-18	12-15	10	27	9	6	4	7	18	69',
     'home_ht_ncaa_string': 'TOTAL		26-55	9-16	12-18	11	35	13	5	3	9	19	73',
     },
    {'away': 'Arizona State', 'home': 'Syracuse',
     'away_ht_ncaa_string': 'TOTAL		25-58	7-18	12-15	10	27	9	6	4	7	18	69',
     'home_ht_ncaa_string': 'TOTAL		26-55	9-16	12-18	11	35	13	5	3	9	19	73',
     },
    # {'away': 'Template 1', 'home': 'Template 2',
    #  'half_time_stats': {'a_h1_points': 28,
    #                      'a_h1_three': 2, 'a_h1_three_att': 10,
    #                      'a_h1_two': 9, 'a_h1_two_att': 21,
    #                      'a_h1_free': 4, 'a_h1_free_att': 4,
    #                      'a_h1_off_rebounds': 5, 'a_h1_rebounds': 14,
    #                      'a_h1_assists': 3, 'a_h1_blocks': 3, 'a_h1_turnovers': 4, 'a_h1_fouls': 8,
    #                      'h_h1_points': 35,
    #                      'h_h1_three': 7, 'h_h1_three_att': 11,
    #                      'h_h1_two': 4, 'h_h1_two_att': 17,
    #                      'h_h1_free': 6, 'h_h1_free_att': 8,
    #                      'h_h1_off_rebounds': 5, 'h_h1_rebounds': 20,
    #                      'h_h1_assists': 6, 'h_h1_blocks': 1, 'h_h1_turnovers': 5, 'h_h1_fouls': 10, },
    #  'away_ht_ncaa_string': 'TOTAL		25-58	7-18	12-15	10	27	9	6	4	7	18	69',
    #  'home_ht_ncaa_string': 'TOTAL		26-55	9-16	12-18	11	35	13	5	3	9	19	73',
    #  },
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

print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('PREDICTIONS (SPREADSHEET-FRIENDLY FORMAT')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('**************************************************************************')
print('FULL-TIME')
for idx, game in enumerate(games):
    print('\t' + game['away'] + ' x ' + game['home'])
    for label in predictions.labels.labels_to_predict:
        print(str(make_prediction_neutral_ground(away_name=game['away'], home_name=game['home'],
                                                 path='models/full-time/' + label + '.pkl',
                                                 features=predictions.feature_sets.features_6)[0]))
print('**************************************************************************')
print('2nd-HALF')
for idx, game in enumerate(games):
    print('\t' + game['away'] + ' x ' + game['home'])
    for label in predictions.labels.labels_to_predict_2nd_half:
        print(str(make_prediction_neutral_ground(away_name=game['away'], home_name=game['home'],
                                                 path='models/2nd-half/' + label + '.pkl',
                                                 features=predictions.feature_sets.features_ht_6,
                                                 extra_features=calculate_first_half_stats(
                                                     # game['half_time_stats']
                                                     {**half_time_stats_from_ncaa_string(game['away_ht_ncaa_string'],
                                                                                         'a'),
                                                      **half_time_stats_from_ncaa_string(game['home_ht_ncaa_string'],
                                                                                         'h')}
                                                 ))[0]))
