'''
Numerical and classification labels
'''

__author__ = "Celso M. de Melo"
__email__ = "celsodemelo@eleveninc.com"

labels_for_feature_selection = ['both_three_points_made', 'h_three_points_made', 'a_three_points_made']

labels_to_predict = ['both_three_points_made', 'a_three_points_made', 'h_three_points_made',
                     'both_three_points_att', 'a_three_points_att', 'h_three_points_att',
                     'both_two_points_made', 'a_two_points_made', 'h_two_points_made',
                     'both_two_points_att', 'a_two_points_att', 'h_two_points_att',
                     'a_three_points_pct', 'h_three_points_pct',
                     'both_free_throws_made', 'a_free_throws_made', 'h_free_throws_made',
                     'a_free_throws_pct', 'h_free_throws_pct',
                     'both_rebounds', 'a_rebounds', 'h_rebounds',
                     'both_offensive_rebounds', 'a_offensive_rebounds', 'h_offensive_rebounds',
                     'both_defensive_rebounds', 'a_defensive_rebounds', 'h_defensive_rebounds',
                     'both_assists', 'a_assists', 'h_assists',
                     'both_field_goals_att', 'a_field_goals_att', 'h_field_goals_att',
                     'both_field_goals_made', 'a_field_goals_made', 'h_field_goals_made',
                     'a_field_goals_pct', 'h_field_goals_pct',
                     'both_possessions', 'a_possessions', 'h_possessions']

labels_to_predict_2nd_half = ['both_h2_three', 'a_h2_three', 'h_h2_three',
                              'both_h2_three_att', 'a_h2_three_att', 'h_h2_three_att',
                              'both_h2_two', 'a_h2_two', 'h_h2_two',
                              'both_h2_two_att', 'a_h2_two_att', 'h_h2_two_att',
                              'a_h2_three_points_pct', 'h_h2_three_points_pct',
                              'both_h2_free', 'a_h2_free', 'h_h2_free',
                              'a_h2_free_throws_pct', 'h_h2_free_throws_pct',
                              'both_h2_rebounds', 'a_h2_rebounds', 'h_h2_rebounds',
                              'both_h2_off_rebounds', 'a_h2_off_rebounds', 'h_h2_off_rebounds',
                              'both_h2_def_rebounds', 'a_h2_def_rebounds', 'h_h2_def_rebounds',
                              'both_h2_assists', 'a_h2_assists', 'h_h2_assists',
                              'both_h2_field_goals_att', 'a_h2_field_goals_att', 'h_h2_field_goals_att',
                              'both_h2_field_goals_made', 'a_h2_field_goals_made', 'h_h2_field_goals_made',
                              'a_h2_field_goals_pct', 'h_h2_field_goals_pct',
                              'both_h2_possessions', 'a_h2_possessions', 'h_h2_possessions'
                              ]




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
