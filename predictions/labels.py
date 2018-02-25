'''
Adds numerical and classification labels
'''

__author__ = "Celso M. de Melo"
__email__ = "celsodemelo@eleveninc.com"


def add_numerical_label(df):
    df['total_three_points'] = 0
    df['total_three_points_att'] = 0
    df['avg_three_points_pct'] = 0.0

    df['total_free_throws'] = 0
    df['avg_free_throws_pct'] = 0.0

    df['total_rebounds'] = 0
    df['total_offensive_rebounds'] = 0

    df['total_assists'] = 0

    df['total_field_goals_att'] = 0
    df['avg_field_goals_pct'] = 0.0

    df['total_possessions'] = 0

    decimal_places = 5

    for index, row in df.iterrows():
        if row['h_h1_three'] == -1 or row['h_h2_three'] == -1 or row['a_h1_three'] == -1 or row['a_h2_three'] == -1:
            df.set_value(index, 'total_three_points', -1)
        else:
            df.set_value(index, 'total_three_points',
                         row['h_h1_three'] + row['h_h2_three'] + row['a_h1_three'] + row['a_h2_three'])
        if row['h_h1_three_att'] == -1 or row['h_h2_three_att'] == -1 or row['a_h1_three_att'] == -1 or row['a_h2_three_att'] == -1:
            df.set_value(index, 'total_three_points_att', -1)
        else:
            df.set_value(index, 'total_three_points_att',
                         row['h_h1_three_att'] + row['h_h2_three_att'] + row['a_h1_three_att'] + row['a_h2_three_att'])

        if row['h_h1_free'] == -1 or row['h_h2_free'] == -1 or row['a_h1_free'] == -1 or row['a_h2_free'] == -1:
            df.set_value(index, 'total_free_throws', -1)
        else:
            df.set_value(index, 'total_free_throws',
                         row['h_h1_free'] + row['h_h2_free'] + row['a_h1_free'] + row['a_h2_free'])
        if row['h_free_throws_pct'] == -1 or row['a_free_throws_pct'] == -1:
            df.set_value(index, 'avg_free_throws_pct', -1)
        else:
            df.set_value(index, 'avg_free_throws_pct',
                         round((row['h_free_throws_pct'] + row['a_free_throws_pct']) / 2.0), decimal_places)

        if row['h_rebounds'] == -1 or row['a_rebounds'] == -1:
            df.set_value(index, 'total_rebounds', -1)
        else:
            df.set_value(index, 'total_rebounds', row['h_rebounds'] + row['a_rebounds'])
        if row['h_offensive_rebounds'] == -1 or row['a_offensive_rebounds'] == -1:
            df.set_value(index, 'total_offensive_rebounds', -1)
        else:
            df.set_value(index, 'total_offensive_rebounds', row['h_offensive_rebounds'] + row['a_offensive_rebounds'])

        if row['h_assists'] == -1 or row['a_assists'] == -1:
            df.set_value(index, 'total_assists', -1)
        else:
            df.set_value(index, 'total_assists', row['h_assists'] + row['a_assists'])

        if row['h_field_goals_att'] == -1 or row['a_field_goals_att'] == -1:
            df.set_value(index, 'total_field_goals_att', -1)
        else:
            df.set_value(index, 'total_field_goals_att', row['h_field_goals_att'] + row['a_field_goals_att'])
        if row['h_field_goals_pct'] == -1 or row['a_field_goals_pct'] == -1:
            df.set_value(index, 'avg_field_goals_pct', -1)
        else:
            df.set_value(index, 'avg_field_goals_pct',
                         round((row['h_field_goals_pct'] + row['a_field_goals_pct']) / 2.0), decimal_places)

        if row['h_possessions'] == -1 or row['a_possessions'] == -1:
            df.set_value(index, 'total_possessions', -1)
        else:
            df.set_value(index, 'total_possessions', row['h_possessions'] + row['a_possessions'])


def add_classification_labels(df):
    ranks = df.total_three_points.rank(pct=True)

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
