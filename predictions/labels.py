'''
Numerical and classification labels
'''

__author__ = "Celso M. de Melo"
__email__ = "celsodemelo@eleveninc.com"

labels_for_feature_selection = ['both_three_points_made', 'h_three_points_made', 'a_three_points_made']

labels_to_predict = ['both_three_points_made', 'h_three_points_made', 'a_three_points_made',
                     'both_three_points_att', 'h_three_points_att', 'a_three_points_att',
                     'both_two_points_made', 'h_two_points_made', 'a_two_points_made',
                     'both_two_points_att', 'h_two_points_att', 'a_two_points_att',
                     'h_three_points_pct', 'a_three_points_pct',
                     'both_free_throws_made', 'h_free_throws_made', 'a_free_throws_made',
                     'h_free_throws_pct', 'a_free_throws_pct',
                     'both_rebounds', 'h_rebounds', 'a_rebounds',
                     'both_offensive_rebounds', 'h_offensive_rebounds', 'a_offensive_rebounds',
                     'both_assists', 'h_assists', 'a_assists',
                     'both_field_goals_att', 'h_field_goals_att', 'a_field_goals_att',
                     'h_field_goals_pct', 'a_field_goals_pct',
                     'both_possessions', 'h_possessions', 'a_possessions']

labels_to_predict_2nd_half = ['both_h2_three', 'h_h2_three', 'a_h2_three',
                              'both_h2_three_att', 'h_h2_three_att', 'a_h2_three_att',
                              'both_h2_two', 'h_h2_two', 'a_h2_two',
                              'both_h2_two_att', 'h_h2_two_att', 'a_h2_two_att',
                              'h_h2_three_points_pct', 'a_h2_three_points_pct',
                              'both_h2_free', 'h_h2_free', 'a_h2_free',
                              'h_h2_free_throws_pct', 'a_h2_free_throws_pct',
                              'both_h2_rebounds', 'h_h2_rebounds', 'a_h2_rebounds',
                              'both_h2_off_rebounds', 'h_h2_off_rebounds', 'a_h2_off_rebounds',
                              'both_h2_assists', 'h_h2_assists', 'a_h2_assists',
                              'both_h2_field_goals_att', 'h_h2_field_goals_att', 'a_h2_field_goals_att',
                              'h_h2_field_goals_pct', 'a_h2_field_goals_pct',
                              'both_h2_possessions', 'h_h2_possessions', 'a_h2_possessions'
                              ]


def add_numerical_label(df):
    df['both_three_points_made'] = 0
    df['both_three_points_att'] = 0

    df['both_two_points_made'] = 0
    df['both_two_points_att'] = 0

    df['both_free_throws_made'] = 0
    df['avg_free_throws_pct'] = 0.0

    df['both_rebounds'] = 0
    df['both_offensive_rebounds'] = 0

    df['both_assists'] = 0

    df['both_field_goals_att'] = 0
    df['avg_field_goals_pct'] = 0.0

    df['both_possessions'] = 0

    df['h_h2_three_points_pct'] = 0.0
    df['a_h2_three_points_pct'] = 0.0
    df['h_h2_free_throws_pct'] = 0.0
    df['a_h2_free_throws_pct'] = 0.0
    df['h_h2_field_goals_att'] = 0
    df['a_h2_field_goals_att'] = 0
    df['h_h2_field_goals_pct'] = 0.0
    df['a_h2_field_goals_pct'] = 0.0
    df['h_h2_possessions'] = 0
    df['a_h2_possessions'] = 0
    
    stats_2nd_half = dict()

    decimal_places = 5

    for index, row in df.iterrows():
        if row['h_h2_three'] == -1 or row['h_h2_three_att'] == -1 or row['h_h2_three_att'] == 0:
            stats_2nd_half['h_h2_three_points_pct']= -1
        else:
            stats_2nd_half['h_h2_three_points_pct']= (round(100.0*float(row['h_h2_three']) / float(row['h_h2_three_att']), decimal_places))
        df.set_value(index, 'h_h2_three_points_pct',stats_2nd_half['h_h2_three_points_pct'])
        if row['a_h2_three'] == -1 or row['a_h2_three_att'] == -1 or row['a_h2_three_att'] == 0:
            stats_2nd_half['a_h2_three_points_pct']= -1
        else:
            stats_2nd_half['a_h2_three_points_pct']= (round(100.0*float(row['a_h2_three']) / float(row['a_h2_three_att']), decimal_places))
        df.set_value(index, 'a_h2_three_points_pct',stats_2nd_half['a_h2_three_points_pct'])
        if row['h_h2_free'] == -1 or row['h_h2_free_att'] == -1 or row['h_h2_free_att'] == 0:
            stats_2nd_half['h_h2_free_throws_pct']= -1
        else:
            stats_2nd_half['h_h2_free_throws_pct']= (round(100.0*float(row['h_h2_free']) / float(row['h_h2_free_att']), decimal_places))
        df.set_value(index, 'h_h2_free_throws_pct',stats_2nd_half['h_h2_free_throws_pct'])
        if row['a_h2_free'] == -1 or row['a_h2_free_att'] == -1 or row['a_h2_free_att'] == 0:
            stats_2nd_half['a_h2_free_throws_pct']= -1
        else:
            stats_2nd_half['a_h2_free_throws_pct']= (round(100.0*float(row['a_h2_free']) / float(row['a_h2_free_att']), decimal_places))
        df.set_value(index, 'a_h2_free_throws_pct',stats_2nd_half['a_h2_free_throws_pct'])
        if row['h_h2_three_att'] == -1 or row['h_h2_two_att'] == -1:
            stats_2nd_half['h_h2_field_goals_att']= -1
        else:
            stats_2nd_half['h_h2_field_goals_att']= (row['h_h2_three_att'] + row['h_h2_two_att'])
        df.set_value(index, 'h_h2_field_goals_att',stats_2nd_half['h_h2_field_goals_att'])
        if row['a_h2_three_att'] == -1 or row['a_h2_two_att'] == -1:
            stats_2nd_half['a_h2_field_goals_att']= -1
        else:
            stats_2nd_half['a_h2_field_goals_att']= (row['a_h2_three_att'] + row['a_h2_two_att'])
        df.set_value(index, 'a_h2_field_goals_att',stats_2nd_half['a_h2_field_goals_att'])

        if stats_2nd_half['h_h2_field_goals_att'] == -1 or stats_2nd_half['h_h2_field_goals_att'] == 0:
            stats_2nd_half['h_h2_field_goals_pct'] = -1
        else:
            stats_2nd_half['h_h2_field_goals_pct'] = (round(100.0*float(row['h_h2_three'] + row['h_h2_two']) / float(stats_2nd_half['h_h2_field_goals_att']),decimal_places))
        df.set_value(index, 'h_h2_field_goals_pct',stats_2nd_half['h_h2_field_goals_pct'])
        if stats_2nd_half['a_h2_field_goals_att'] == -1 or stats_2nd_half['a_h2_field_goals_att'] == 0:
            stats_2nd_half['a_h2_field_goals_pct'] = -1
        else:
            stats_2nd_half['a_h2_field_goals_pct']= (round(100.0*float(row['a_h2_three'] + row['a_h2_two']) / float(stats_2nd_half['a_h2_field_goals_att']),decimal_places))

        df.set_value(index, 'a_h2_field_goals_pct',stats_2nd_half['a_h2_field_goals_pct'])
        if stats_2nd_half['a_h2_field_goals_att'] == -1 or stats_2nd_half['h_h2_field_goals_att'] == -1:
            stats_2nd_half['both_h2_field_goals_att'] = -1
        else:
            stats_2nd_half['both_h2_field_goals_att'] = (stats_2nd_half['a_h2_field_goals_att'] + stats_2nd_half['h_h2_field_goals_att'])
        df.set_value(index, 'both_h2_field_goals_att',stats_2nd_half['both_h2_field_goals_att'])
        if row['h_h2_field_goals_att'] == -1 or row['h_h2_turnovers'] == -1 or row['h_h2_free_att'] == -1 or row['h_h2_off_rebounds'] == -1:
            stats_2nd_half['h_h2_possessions'] = -1
        else:
            stats_2nd_half['h_h2_possessions'] = ((
                stats_2nd_half['h_h2_field_goals_att'] + row['h_h2_turnovers'] + 0.475 * row['h_h2_free_att'] -
                row['h_h2_off_rebounds']))
        df.set_value(index, 'h_h2_possessions',stats_2nd_half['h_h2_possessions'])
        if row['a_h2_field_goals_att'] == -1 or row['a_h2_turnovers'] == -1 or row['a_h2_free_att'] == -1 or row['a_h2_off_rebounds'] == -1:
            stats_2nd_half['a_h2_possessions'] = -1
        else:
            stats_2nd_half['a_h2_possessions'] = ((
                stats_2nd_half['a_h2_field_goals_att'] + row['a_h2_turnovers'] + 0.475 * row['a_h2_free_att'] -
                row['a_h2_off_rebounds']))
        df.set_value(index, 'a_h2_possessions',stats_2nd_half['a_h2_possessions'])
        if stats_2nd_half['a_h2_possessions'] == -1 or stats_2nd_half['h_h2_possessions'] == -1:
            stats_2nd_half['both_h2_possessions'] = -1
        else:
            stats_2nd_half['both_h2_possessions'] = (stats_2nd_half['a_h2_possessions'] + stats_2nd_half['h_h2_possessions'])
        df.set_value(index, 'both_h2_possessions',stats_2nd_half['both_h2_possessions'])


        if row['h_h1_three'] == -1 or row['h_h2_three'] == -1 or row['a_h1_three'] == -1 or row['a_h2_three'] == -1:
            df.set_value(index, 'both_three_points_made', -1)
        else:
            df.set_value(index, 'both_three_points_made',
                         row['h_h1_three'] + row['h_h2_three'] + row['a_h1_three'] + row['a_h2_three'])
        if row['h_h1_three_att'] == -1 or row['h_h2_three_att'] == -1 or row['a_h1_three_att'] == -1 or row[
            'a_h2_three_att'] == -1:
            df.set_value(index, 'both_three_points_att', -1)
        else:
            df.set_value(index, 'both_three_points_att',
                         row['h_h1_three_att'] + row['h_h2_three_att'] + row['a_h1_three_att'] + row['a_h2_three_att'])

        if row['h_two_points_made'] == -1 or row['a_two_points_made'] == -1:
            df.set_value(index, 'both_two_points_made', -1)
        else:
            df.set_value(index, 'both_two_points_made',
                         row['h_two_points_made'] + row['a_two_points_made'])
        if row['h_two_points_att'] == -1 or row['a_two_points_att'] == -1:
            df.set_value(index, 'both_two_points_att', -1)
        else:
            df.set_value(index, 'both_two_points_att',
                         row['h_two_points_att'] + row['a_two_points_att'])

        if row['h_h1_free'] == -1 or row['h_h2_free'] == -1 or row['a_h1_free'] == -1 or row['a_h2_free'] == -1:
            df.set_value(index, 'both_free_throws_made', -1)
        else:
            df.set_value(index, 'both_free_throws_made',
                         row['h_h1_free'] + row['h_h2_free'] + row['a_h1_free'] + row['a_h2_free'])
        if row['h_free_throws_pct'] == -1 or row['a_free_throws_pct'] == -1:
            df.set_value(index, 'avg_free_throws_pct', -1)
        else:
            df.set_value(index, 'avg_free_throws_pct',
                         round((row['h_free_throws_pct'] + row['a_free_throws_pct']) / 2.0), decimal_places)

        if row['h_rebounds'] == -1 or row['a_rebounds'] == -1:
            df.set_value(index, 'both_rebounds', -1)
        else:
            df.set_value(index, 'both_rebounds', row['h_rebounds'] + row['a_rebounds'])
        if row['h_offensive_rebounds'] == -1 or row['a_offensive_rebounds'] == -1:
            df.set_value(index, 'both_offensive_rebounds', -1)
        else:
            df.set_value(index, 'both_offensive_rebounds', row['h_offensive_rebounds'] + row['a_offensive_rebounds'])

        if row['h_assists'] == -1 or row['a_assists'] == -1:
            df.set_value(index, 'both_assists', -1)
        else:
            df.set_value(index, 'both_assists', row['h_assists'] + row['a_assists'])

        if row['h_field_goals_att'] == -1 or row['a_field_goals_att'] == -1:
            df.set_value(index, 'both_field_goals_att', -1)
        else:
            df.set_value(index, 'both_field_goals_att', row['h_field_goals_att'] + row['a_field_goals_att'])
        if row['h_field_goals_pct'] == -1 or row['a_field_goals_pct'] == -1:
            df.set_value(index, 'avg_field_goals_pct', -1)
        else:
            df.set_value(index, 'avg_field_goals_pct',
                         round((row['h_field_goals_pct'] + row['a_field_goals_pct']) / 2.0), decimal_places)

        if row['h_possessions'] == -1 or row['a_possessions'] == -1:
            df.set_value(index, 'both_possessions', -1)
        else:
            df.set_value(index, 'both_possessions', row['h_possessions'] + row['a_possessions'])



def add_classification_labels(df):
    ranks = df.both_three_points_made.rank(pct=True)

    percentiles = [15, 20, 25, 30]

    for p in percentiles:
        label = 'total_3pts_' + str(p) + '_80_' + str(p)
        df[label] = '02_Normal'
        label_le = 'total_3pts_le_' + str(p)
        df[label_le] = 'No'
        label_ge = 'total_3pts_ge_' + str(p)
        df[label_ge] = 'No'

        fr = p / 100.0
        for index, row in df.iterrows():
            if ranks[index] <= fr:
                df.set_value(index, label, '01_Low')
                df.set_value(index, label_le, 'Yes')
            elif ranks[index] >= (1.0 - fr):
                df.set_value(index, label, '03_High')
                df.set_value(index, label_ge, 'Yes')
