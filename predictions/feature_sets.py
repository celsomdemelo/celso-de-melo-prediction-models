__author__ = "Celso M. de Melo"
__email__ = "celsodemelo@eleveninc.com"

features_1 = [
    'both_avg_points_game',
    'both_avg_field_goals_made',
    'both_avg_field_goals_att',
    'both_avg_field_goals_pct',
    'both_avg_three_points_made',
    'both_avg_three_points_att',
    'both_avg_three_points_pct',
    'both_avg_two_points_made',
    'both_avg_two_points_att',
    'both_avg_two_points_pct',
    'both_avg_blocked_att',
    'both_avg_free_throws_made',
    'both_avg_free_throws_att',
    'both_avg_free_throws_pct',
    'both_avg_offensive_rebounds',
    'both_avg_defensive_rebounds',
    'both_avg_rebounds',
    'both_avg_assists',
    'both_avg_turnovers',
    'both_avg_blocks',
    'both_avg_personal_fouls',
    'both_avg_score_margin',
    'both_avg_opp_points',
    'both_avg_opp_off_rebounds',
    'both_avg_opp_def_rebounds',
    'both_avg_opp_blocks',
    'both_avg_possessions'
]

features_ht_1 = features_1[:] + [
    'both_h1_points',
    'both_h1_three_att',
    'both_h1_three',
    'both_h1_two_att',
    'both_h1_two',
    'both_h1_free_att',
    'both_h1_free',
    'both_h1_off_rebounds',
    'both_h1_rebounds',
    'both_h1_assists',
    'both_h1_blocks',
    'both_h1_turnovers',
    'both_h1_fouls'
]


def clean_df(df, vars):
    df = df[vars]
    df = df.dropna(axis=0, how='any')

    return df
