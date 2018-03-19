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
    decimal_places = 2
    return (predictions_1.round(decimal_places) + predictions_2.round(decimal_places)) / 2.0


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


class NCAAStringConstants:
    FGM = 0
    FGA = 1
    P3M = 2
    P3A = 3
    FTM = 4
    FTA = 5
    OREB = 6
    REB = 7
    AST = 8
    ST = 9
    BLK = 10
    TO = 11
    PF = 12
    PTS = 13


def get_numbers_from_ncaa_string(ncaa_string):
    ncaa_string = ncaa_string[7:]
    ns = re.findall(r"[\w']+", ncaa_string)
    return list(map(int, ns))


def half_time_stats_from_ncaa_string(ncaa_string, prefix):
    ns = get_numbers_from_ncaa_string(ncaa_string)

    return {prefix + '_h1_points': ns[NCAAStringConstants.PTS],
            prefix + '_h1_three': ns[NCAAStringConstants.P3M],
            prefix + '_h1_three_att': ns[NCAAStringConstants.P3A],
            prefix + '_h1_two': ns[NCAAStringConstants.PTS] - ns[NCAAStringConstants.P3M],
            prefix + '_h1_two_att': ns[NCAAStringConstants.FGA] - ns[NCAAStringConstants.P3A],
            prefix + '_h1_free': ns[NCAAStringConstants.FTM],
            prefix + '_h1_free_att': ns[NCAAStringConstants.FTA],
            prefix + '_h1_off_rebounds': ns[NCAAStringConstants.OREB],
            prefix + '_h1_rebounds': ns[NCAAStringConstants.REB],
            prefix + '_h1_assists': ns[NCAAStringConstants.AST],
            prefix + '_h1_blocks': ns[NCAAStringConstants.BLK],
            prefix + '_h1_turnovers': ns[NCAAStringConstants.TO],
            prefix + '_h1_fouls': ns[NCAAStringConstants.PF], }


def ground_truth(away_ncaa_string, home_ncaa_string):
    away_ns = get_numbers_from_ncaa_string(away_ncaa_string)
    home_ns = get_numbers_from_ncaa_string(home_ncaa_string)

    h_possessions = 0.5 * (home_ns[NCAAStringConstants.FGA] + 0.475 * home_ns[NCAAStringConstants.FTA] -
                           home_ns[NCAAStringConstants.OREB] + home_ns[NCAAStringConstants.TO]) + 0.5 * (
        away_ns[NCAAStringConstants.FGA] + 0.475 * away_ns[NCAAStringConstants.FTA] -
        away_ns[NCAAStringConstants.OREB] + away_ns[NCAAStringConstants.TO])
    a_possessions = 0.5 * (away_ns[NCAAStringConstants.FGA] + 0.475 * away_ns[NCAAStringConstants.FTA] -
                           away_ns[NCAAStringConstants.OREB] + away_ns[NCAAStringConstants.TO]) + 0.5 * (
        home_ns[NCAAStringConstants.FGA] + 0.475 * home_ns[NCAAStringConstants.FTA] -
        home_ns[NCAAStringConstants.OREB] + home_ns[NCAAStringConstants.TO])

    h_free_throws_pct = 0
    if home_ns[NCAAStringConstants.FTA] != 0:
        h_free_throws_pct = 100.0 * float(home_ns[NCAAStringConstants.FTM]) / home_ns[NCAAStringConstants.FTA]
    a_free_throws_pct = 0
    if away_ns[NCAAStringConstants.FTA] != 0:
        a_free_throws_pct = 100.0 * float(away_ns[NCAAStringConstants.FTM]) / away_ns[NCAAStringConstants.FTA]

    return [
        away_ns[NCAAStringConstants.P3M] + home_ns[NCAAStringConstants.P3M],  # both_three_points_made
        home_ns[NCAAStringConstants.P3M],  # h_three_points_made
        away_ns[NCAAStringConstants.P3M],  # a_three_points_made
        away_ns[NCAAStringConstants.P3A] + home_ns[NCAAStringConstants.P3A],  # both_three_points_att
        home_ns[NCAAStringConstants.P3A],  # h_three_points_att
        away_ns[NCAAStringConstants.P3A],  # a_three_points_att
        away_ns[NCAAStringConstants.FGM] - away_ns[NCAAStringConstants.P3M] + home_ns[NCAAStringConstants.FGM] -
        home_ns[NCAAStringConstants.P3M],  # both_two_points_made
        home_ns[NCAAStringConstants.FGM] - home_ns[NCAAStringConstants.P3M],  # h_two_points_made
        away_ns[NCAAStringConstants.FGM] - away_ns[NCAAStringConstants.P3M],  # a_two_points_made
        away_ns[NCAAStringConstants.FGA] - away_ns[NCAAStringConstants.P3A] + home_ns[NCAAStringConstants.FGA] -
        home_ns[NCAAStringConstants.P3A],  # both_two_points_att
        home_ns[NCAAStringConstants.FGA] - home_ns[NCAAStringConstants.P3A],  # h_two_points_att
        away_ns[NCAAStringConstants.FGA] - away_ns[NCAAStringConstants.P3A],  # a_two_points_att
        100.0 * float(home_ns[NCAAStringConstants.P3M]) / home_ns[NCAAStringConstants.P3A],  # h_three_points_pct
        100.0 * float(away_ns[NCAAStringConstants.P3M]) / away_ns[NCAAStringConstants.P3A],  # a_three_points_pct

        away_ns[NCAAStringConstants.FTM] + home_ns[NCAAStringConstants.FTM],  # both_free_throws_made
        home_ns[NCAAStringConstants.FTM],  # h_free_throws_made
        away_ns[NCAAStringConstants.FTM],  # a_free_throws_made

        h_free_throws_pct,
        a_free_throws_pct,

        away_ns[NCAAStringConstants.REB] + home_ns[NCAAStringConstants.REB],  # both_rebounds
        home_ns[NCAAStringConstants.REB],  # h_rebounds
        away_ns[NCAAStringConstants.REB],  # a_rebounds
        away_ns[NCAAStringConstants.OREB] + home_ns[NCAAStringConstants.OREB],  # both_offensive_rebounds
        home_ns[NCAAStringConstants.OREB],  # h_offensive_rebounds
        away_ns[NCAAStringConstants.OREB],  # a_offensive_rebounds

        away_ns[NCAAStringConstants.AST] + home_ns[NCAAStringConstants.AST],  # both_assists
        home_ns[NCAAStringConstants.AST],  # h_assists
        away_ns[NCAAStringConstants.AST],  # a_assists

        away_ns[NCAAStringConstants.FGA] + home_ns[NCAAStringConstants.FGA],  # both_field_goals_att
        home_ns[NCAAStringConstants.FGA],  # h_field_goals_att
        away_ns[NCAAStringConstants.FGA],  # a_field_goals_att
        100.0 * float(home_ns[NCAAStringConstants.FGM]) / home_ns[NCAAStringConstants.FGA],  # h_field_goals_pct
        100.0 * float(away_ns[NCAAStringConstants.FGM]) / away_ns[NCAAStringConstants.FGA],  # a_field_goals_pct

        a_possessions + h_possessions,  # both_possessions
        h_possessions,  # h_possessions
        a_possessions,  # a_possessions
    ]


def ground_truth_2nd_half(away_ncaa_string, home_ncaa_string, away_ht_ncaa_string, home_ht_ncaa_string):
    ft = ground_truth(away_ncaa_string, home_ncaa_string)
    ht = ground_truth(away_ht_ncaa_string, home_ht_ncaa_string)
    return np.array(ft) - np.array(ht)


def print_ground_truth(away_ncaa_string, home_ncaa_string):
    gt = ground_truth(away_ncaa_string, home_ncaa_string)
    for n in gt:
        print(str(n))


def print_ground_truth_2nd_half(away_ncaa_string, home_ncaa_string, away_ht_ncaa_string, home_ht_ncaa_string):
    gt = ground_truth_2nd_half(away_ncaa_string, home_ncaa_string, away_ht_ncaa_string, home_ht_ncaa_string)
    for n in gt:
        print(str(n))

# TOURNAMENT_DATA_ONLY = False

full_time_models_path = 'models/full-time/'
second_half_models_path = 'models/2nd-half/'

# if TOURNAMENT_DATA_ONLY:
#     full_time_models_path = 'models/tournament/full-time/'
#     second_half_models_path = 'models/tournament/2nd-half/'


# print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
# print('GROUND TRUTH')
# print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
# print('**************************************************************************')
# print('FULL-TIME')
# print_ground_truth('TOTAL		21-69	0-14	4-6	17	39	10	5	2	15	18	46',
#                    'TOTAL		21-57	6-24	16-19	11	38	9	7	8	14	12	64')
# print('**************************************************************************')
# print('2nd-HALF')
# print_ground_truth_2nd_half(
#     'TOTAL		21-69	0-14	4-6	17	39	10	5	2	15	18	46',
#     'TOTAL		21-57	6-24	16-19	11	38	9	7	8	14	12	64',
#     'TOTAL		13-35	0-6	0-0	7	14	6	2	2	7	10	26',
#     'TOTAL		11-23	3-8	11-12	3	14	4	3	6	8	4	36')

games = [
    {'away': 'UMBC', 'home': 'Kansas State',
         'away_ht_ncaa_string': 'TOTAL		12-31	5-11	4-4	5	11	7	1	0	6	7	33',
         'home_ht_ncaa_string': 'TOTAL		18-30	6-12	2-6	5	15	9	1	3	3	8	44',
         },
    {'away': 'Clemson', 'home': 'Auburn',
         'away_ht_ncaa_string': 'TOTAL		12-31	5-11	4-4	5	11	7	1	0	6	7	33',
         'home_ht_ncaa_string': 'TOTAL		18-30	6-12	2-6	5	15	9	1	3	3	8	44',
         },
    # {'away': 'Ohio State', 'home': 'Gonzaga',
    #      'away_ht_ncaa_string': 'TOTAL		12-31	5-11	4-4	5	11	7	1	0	6	7	33',
    #      'home_ht_ncaa_string': 'TOTAL		18-30	6-12	2-6	5	15	9	1	3	3	8	44',
    #      },
    # {'away': 'LIU Brooklyn', 'home': 'Radford',
    #  'away_ht_ncaa_string': 'TOTAL		12-27	3-13	1-3	1	12	9	1	0	8	8	28',
    #  'home_ht_ncaa_string': 'TOTAL		13-25	2-7	2-4	2	14	10	2	1	8	9	30',
    #  'away_ncaa_string': 'TOTAL		19-50	7-26	16-23	4	30	13	3	0	15	19	61',
    #  'home_ncaa_string': 'TOTAL		28-59	6-17	9-13	8	35	17	6	2	13	23	71',
    #  },
    # {'away': 'St. Bonaventure', 'home': 'UCLA',
    #  'away_ht_ncaa_string': 'TOTAL		25-58	7-18	12-15	10	27	9	6	4	7	18	69',
    #  'home_ht_ncaa_string': 'TOTAL		26-55	9-16	12-18	11	35	13	5	3	9	19	73',
    #  },
    # {'away': 'Texas Southern', 'home': 'North Carolina Central',
    #  'away_ht_ncaa_string': 'TOTAL		11-23	3-8	11-12	3	14	4	3	6	8	4	36',
    #  'home_ht_ncaa_string': 'TOTAL		13-35	0-6	0-0	7	14	6	2	2	7	10	26',
    #  'away_ncaa_string': 'TOTAL		21-57	6-24	16-19	11	38	9	7	8	14	12	64',
    #  'home_ncaa_string': 'TOTAL		21-69	0-14	4-6	17	39	10	5	2	15	18	46',
    #  },
    # {'away': 'Kentucky', 'home': 'Davidson',
    #  'away_ht_ncaa_string': 'TOTAL		15-28	0-3	4-6	3	20	6	2	3	6	7	34',
    #  'home_ht_ncaa_string': 'TOTAL		10-33	3-14	1-1	4	13	5	2	0	3	7	24',
    #  },
    # {'away': 'Bucknell', 'home': 'Michigan State',
    #  'away_ht_ncaa_string': 'TOTAL		13-27	5-7	9-14	3	12	9	2	0	2	9	40',
    #  'home_ht_ncaa_string': 'TOTAL		19-31	3-8	3-4	4	17	15	0	3	4	10	44',
    #  'away_ncaa_string': '',
    #  'home_ncaa_string': '',
    #  },
    # {'away': 'UMBC', 'home': 'Virginia',
    #      'away_ht_ncaa_string': 'TOTAL		7-20	5-12	2-4	1	16	5	-1	0	5	3	21',
    #      'home_ht_ncaa_string': 'TOTAL		9-23	1-9	2-5	1	16	0	-1	0	5	3	21',
    #      },
    # {'away': 'Arizona State', 'home': 'Syracuse',
    #  'away_ht_ncaa_string': 'TOTAL		25-58	7-18	12-15	10	27	9	6	4	7	18	69',
    #  'home_ht_ncaa_string': 'TOTAL		26-55	9-16	12-18	11	35	13	5	3	9	19	73',
    #  },
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

for label in predictions.labels.labels_to_predict:
    print(label)
for label in predictions.labels.labels_to_predict_2nd_half:
    print(label)

print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('PREDICTIONS (SPREADSHEET-FRIENDLY FORMAT')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('**************************************************************************')
print('FULL-TIME')
print('**************************************************************************')
for idx, game in enumerate(games):
    print('' + game['away'] + ' x ' + game['home'])

    print('----------------- LABELS -----------------')
    for label in predictions.labels.labels_to_predict:
        if label[:5] == 'both_':
            print('BOTH: ' + label[5:])
        elif label[:2] == 'h_':
            print(game['home'][:4] + ': ' + label[2:])
        elif label[:2] == 'a_':
            print(game['away'][:4] + ': ' + label[2:])
    print(game['away'])
    print(game['home'])

    print('----------------- POINT ESTIMATES -----------------')
    for label in predictions.labels.labels_to_predict:
        print(str(make_prediction_neutral_ground(away_name=game['away'], home_name=game['home'],
                                                 path=full_time_models_path + label + '.pkl',
                                                 features=predictions.feature_sets.features_6)[0]))
print('**************************************************************************')
print('2nd-HALF')
print('**************************************************************************')
for idx, game in enumerate(games):
    print('' + game['away'] + ' x ' + game['home'])

    print('----------------- LABELS -----------------')
    for label in predictions.labels.labels_to_predict_2nd_half:
        if label[:5] == 'both_':
            print('BOTH: ' + label[5:])
        elif label[:2] == 'h_':
            print(game['home'][:4] + ': ' + label[2:])
        elif label[:2] == 'a_':
            print(game['away'][:4] + ': ' + label[2:])
    print(game['away'])
    print(game['home'])

    print('----------------- POINT ESTIMATES -----------------')
    for label in predictions.labels.labels_to_predict_2nd_half:
        print(str(make_prediction_neutral_ground(away_name=game['away'], home_name=game['home'],
                                                 path=second_half_models_path + label + '.pkl',
                                                 features=predictions.feature_sets.features_ht_6,
                                                 extra_features=calculate_first_half_stats(# game['half_time_stats']
                                                  {**half_time_stats_from_ncaa_string(game['away_ht_ncaa_string'],'a'),
                                                   **half_time_stats_from_ncaa_string(game['home_ht_ncaa_string'],'h')}
                                                 ))[0]))
