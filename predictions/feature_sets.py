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
    'both_avg_blocks',
    'both_avg_free_throws_made',
    'both_avg_free_throws_att',
    'both_avg_free_throws_pct',
    'both_avg_offensive_rebounds',
    'both_avg_defensive_rebounds',
    'both_avg_rebounds',
    'both_avg_assists',
    'both_avg_turnovers',
    'both_avg_personal_fouls',
    'both_avg_score_margin',
    'both_avg_opp_points',
    'both_avg_opp_off_rebounds',
    'both_avg_opp_def_rebounds',
    'both_avg_opp_blocks',
    'both_avg_3pt_shot_selection',
    'both_avg_possessions'
]

features_1_h = [
    'h_avg_points_game',
    'h_avg_field_goals_made',
    'h_avg_field_goals_att',
    'h_avg_field_goals_pct',
    'h_avg_three_points_made',
    'h_avg_three_points_att',
    'h_avg_three_points_pct',
    'h_avg_two_points_made',
    'h_avg_two_points_att',
    'h_avg_two_points_pct',
    'h_avg_blocks',
    'h_avg_free_throws_made',
    'h_avg_free_throws_att',
    'h_avg_free_throws_pct',
    'h_avg_offensive_rebounds',
    'h_avg_defensive_rebounds',
    'h_avg_rebounds',
    'h_avg_assists',
    'h_avg_turnovers',
    'h_avg_personal_fouls',
    'h_avg_score_margin',
    'h_avg_3pt_shot_selection',
    'h_avg_possessions',
    # 'h_avg_opp_points',
    # 'h_avg_opp_off_rebounds',
    # 'h_avg_opp_def_rebounds',
    # 'h_avg_opp_blocks'
]

features_1_a = [
    'a_avg_points_game',
    'a_avg_field_goals_made',
    'a_avg_field_goals_att',
    'a_avg_field_goals_pct',
    'a_avg_three_points_made',
    'a_avg_three_points_att',
    'a_avg_three_points_pct',
    'a_avg_two_points_made',
    'a_avg_two_points_att',
    'a_avg_two_points_pct',
    'a_avg_blocks',
    'a_avg_free_throws_made',
    'a_avg_free_throws_att',
    'a_avg_free_throws_pct',
    'a_avg_offensive_rebounds',
    'a_avg_defensive_rebounds',
    'a_avg_rebounds',
    'a_avg_assists',
    'a_avg_turnovers',
    'a_avg_personal_fouls',
    'a_avg_score_margin',
    'a_avg_3pt_shot_selection',
    'a_avg_possessions',
    # 'a_avg_opp_points',
    # 'a_avg_opp_off_rebounds',
    # 'a_avg_opp_def_rebounds',
    # 'a_avg_opp_blocks'
]

features_1_h_and_a = features_1_h[:] + features_1_a[:]

features_1_both_h_and_a = features_1[:] + features_1_h[:] + features_1_a[:]

features_2 = [
    'h_wins',
    'h_losses',
    'h_streak',
    'a_wins',
    'a_losses',
    'a_streak',
    'both_wins',
    'both_losses'
]

features_3_h = [
    'h_avg_points_game',
    'h_avg_field_goals_made',
    'h_avg_field_goals_att',
    'h_avg_field_goals_pct',
    'h_avg_three_points_made',
    'h_avg_three_points_att',
    'h_avg_three_points_pct',
    'h_avg_two_points_made',
    'h_avg_two_points_att',
    'h_avg_two_points_pct',
    'h_avg_blocks',
    'h_avg_free_throws_made',
    'h_avg_free_throws_att',
    'h_avg_free_throws_pct',
    'h_avg_offensive_rebounds',
    'h_avg_defensive_rebounds',
    'h_avg_rebounds',
    'h_avg_assists',
    'h_avg_turnovers',
    'h_avg_personal_fouls',
    'h_avg_score_margin',
    'h_avg_3pt_shot_selection',
    'h_avg_possessions',
    'h_avg_opp_points_game',
    'h_avg_opp_field_goals_made',
    'h_avg_opp_field_goals_att',
    'h_avg_opp_field_goals_pct',
    'h_avg_opp_three_points_made',
    'h_avg_opp_three_points_att',
    'h_avg_opp_three_points_pct',
    'h_avg_opp_two_points_made',
    'h_avg_opp_two_points_att',
    'h_avg_opp_two_points_pct',
    'h_avg_opp_blocks',
    'h_avg_opp_free_throws_made',
    'h_avg_opp_free_throws_att',
    'h_avg_opp_free_throws_pct',
    'h_avg_opp_offensive_rebounds',
    'h_avg_opp_defensive_rebounds',
    'h_avg_opp_rebounds',
    'h_avg_opp_assists',
    'h_avg_opp_turnovers',
    'h_avg_opp_personal_fouls',
    'h_avg_opp_score_margin',
    'h_avg_opp_3pt_shot_selection',
    'h_avg_opp_possessions',
]

features_3_a = [
    'a_avg_points_game',
    'a_avg_field_goals_made',
    'a_avg_field_goals_att',
    'a_avg_field_goals_pct',
    'a_avg_three_points_made',
    'a_avg_three_points_att',
    'a_avg_three_points_pct',
    'a_avg_two_points_made',
    'a_avg_two_points_att',
    'a_avg_two_points_pct',
    'a_avg_blocks',
    'a_avg_free_throws_made',
    'a_avg_free_throws_att',
    'a_avg_free_throws_pct',
    'a_avg_offensive_rebounds',
    'a_avg_defensive_rebounds',
    'a_avg_rebounds',
    'a_avg_assists',
    'a_avg_turnovers',
    'a_avg_personal_fouls',
    'a_avg_score_margin',
    'a_avg_3pt_shot_selection',
    'a_avg_possessions',
    'a_avg_opp_points_game',
    'a_avg_opp_field_goals_made',
    'a_avg_opp_field_goals_att',
    'a_avg_opp_field_goals_pct',
    'a_avg_opp_three_points_made',
    'a_avg_opp_three_points_att',
    'a_avg_opp_three_points_pct',
    'a_avg_opp_two_points_made',
    'a_avg_opp_two_points_att',
    'a_avg_opp_two_points_pct',
    'a_avg_opp_blocks',
    'a_avg_opp_free_throws_made',
    'a_avg_opp_free_throws_att',
    'a_avg_opp_free_throws_pct',
    'a_avg_opp_offensive_rebounds',
    'a_avg_opp_defensive_rebounds',
    'a_avg_opp_rebounds',
    'a_avg_opp_assists',
    'a_avg_opp_turnovers',
    'a_avg_opp_personal_fouls',
    'a_avg_opp_score_margin',
    'a_avg_opp_3pt_shot_selection',
    'a_avg_opp_possessions',
]

# Best features from features_3_h_and_a
features_4 = [
    'h_avg_three_points_made',
    'a_avg_three_points_made',
    'h_avg_three_points_att',
    'a_avg_three_points_att',
    'h_avg_3pt_shot_selection',
    'a_avg_opp_three_points_att',
    'h_avg_opp_three_points_made',
    'a_avg_opp_three_points_made',
    'h_avg_opp_three_points_att',
    'a_avg_opp_assists',
    'h_avg_opp_field_goals_made',
    'h_avg_opp_assists',
    'h_avg_opp_3pt_shot_selection',
    'a_avg_opp_field_goals_made',
    'h_avg_assists',
    'a_avg_3pt_shot_selection',
    'h_avg_points_game',
    'h_avg_opp_points_game',
    'a_avg_opp_points_game',
    'a_avg_opp_defensive_rebounds',
    'h_avg_field_goals_made',
    'h_avg_opp_field_goals_att',
    'a_avg_opp_field_goals_att',
    'a_avg_assists',
    'h_avg_opp_defensive_rebounds',
    'h_avg_three_points_pct',
    'a_avg_blocks',
    'a_avg_opp_rebounds',
    'h_avg_field_goals_att',
    'a_avg_points_game',
    'a_avg_three_points_pct',
    'h_avg_opp_possessions',
    'h_avg_possessions',
    'h_avg_offensive_rebounds',
    'a_avg_field_goals_att',
    'a_avg_field_goals_made',
    'a_avg_offensive_rebounds',
    'h_avg_opp_two_points_made',
    'a_avg_possessions',
    'a_avg_opp_possessions',
    'a_avg_two_points_att',
    'h_avg_blocks',
    'h_avg_opp_rebounds',
    'a_avg_opp_two_points_made',
    'h_avg_two_points_att',
    'h_avg_opp_two_points_pct',
    'a_avg_free_throws_att',
    'a_avg_opp_two_points_pct',
    'h_avg_defensive_rebounds',
    'h_avg_two_points_pct',
    'a_avg_defensive_rebounds',
    'h_avg_free_throws_pct',
    'h_avg_free_throws_att',
    'h_avg_opp_three_points_pct',
    'h_avg_opp_field_goals_pct',
    'h_avg_opp_free_throws_att',
    'a_avg_two_points_made',
    'a_avg_opp_field_goals_pct',
    'a_avg_free_throws_pct',
    'a_avg_opp_three_points_pct',
    'h_avg_opp_free_throws_made',
    'h_avg_field_goals_pct',
]

features_5 = features_4[:] + [
    # 'h_avg_possessions',
    'h_avg_defensive_rating',
    'h_avg_offensive_rating',
    'h_avg_effective_field_goal_percentage',
    'h_avg_net_rating',
    'h_avg_turnover_percentage',
    'h_avg_true_shooting_percentage',
    # 'a_avg_possessions',
    'a_avg_defensive_rating',
    'a_avg_offensive_rating',
    'a_avg_effective_field_goal_percentage',
    'a_avg_net_rating',
    'a_avg_turnover_percentage',
    'a_avg_true_shooting_percentage',

    'h_avg_offensive_rebounding_percentage',
    'h_avg_defensive_rebounding_percentage',
    'h_avg_turnover_percentage',
    'h_avg_free_throw_rate',
    'h_avg_assist_rate',
    'h_avg_block_rate',
    'a_avg_offensive_rebounding_percentage',
    'a_avg_defensive_rebounding_percentage',
    'a_avg_turnover_percentage',
    'a_avg_free_throw_rate',
    'a_avg_assist_rate',
    'a_avg_block_rate',

    # 'h_avg_opp_possessions',
    'h_avg_opp_defensive_rating',
    'h_avg_opp_offensive_rating',
    'h_avg_opp_effective_field_goal_percentage',
    'h_avg_opp_net_rating',
    'h_avg_opp_turnover_percentage',
    'h_avg_opp_true_shooting_percentage',
    # 'a_avg_opp_possessions',
    'a_avg_opp_defensive_rating',
    'a_avg_opp_offensive_rating',
    'a_avg_opp_effective_field_goal_percentage',
    'a_avg_opp_net_rating',
    'a_avg_opp_turnover_percentage',
    'a_avg_opp_true_shooting_percentage',

    'h_avg_opp_offensive_rebounding_percentage',
    'h_avg_opp_defensive_rebounding_percentage',
    'h_avg_opp_turnover_percentage',
    'h_avg_opp_free_throw_rate',
    'h_avg_opp_assist_rate',
    'h_avg_opp_block_rate',
    'a_avg_opp_offensive_rebounding_percentage',
    'a_avg_opp_defensive_rebounding_percentage',
    'a_avg_opp_turnover_percentage',
    'a_avg_opp_free_throw_rate',
    'a_avg_opp_assist_rate',
    'a_avg_opp_block_rate',
]

features_6 = [
    'h_avg_three_points_made',
    'a_avg_three_points_made',
    'h_avg_three_points_att',
    'a_avg_three_points_att',
    'h_avg_3pt_shot_selection',
    'a_avg_opp_three_points_att',
    'a_avg_opp_three_points_made',
    'h_avg_opp_three_points_made',
    'h_avg_opp_three_points_att',
    'a_avg_opp_assists',
    'h_avg_opp_3pt_shot_selection',
    'h_avg_opp_assists',
    'a_avg_opp_field_goals_made',
    'h_avg_assists',
    'h_avg_opp_field_goals_made',
    'a_avg_net_rating',
    'a_avg_opp_assist_rate',
    'h_avg_points_game',
    'a_avg_3pt_shot_selection',
    'a_avg_opp_points_game',
    'a_avg_opp_defensive_rebounds',
    'a_avg_opp_field_goals_att',
    'h_avg_field_goals_made',
    'h_avg_opp_points_game',
    'a_avg_assists',
    'h_avg_opp_field_goals_att',
    'h_avg_opp_defensive_rebounding_percentage',
    'h_avg_three_points_pct',
    'a_avg_opp_rebounds',
    'h_avg_opp_defensive_rebounds',
    'a_avg_offensive_rebounding_percentage',
    'a_avg_points_game',
    'a_avg_blocks',
    'h_avg_field_goals_att',
    'h_avg_effective_field_goal_percentage',
    'a_avg_three_points_pct',
    'a_avg_field_goals_made',
    'a_avg_field_goals_att',
    'h_avg_possessions',
    'h_avg_opp_possessions',
    'h_avg_turnover_percentage',
    'a_avg_opp_possessions',
    'a_avg_possessions',
    'a_avg_offensive_rebounds',
    'h_avg_opp_block_rate',
    'a_avg_opp_two_points_made',
    'h_avg_opp_effective_field_goal_percentage',
    'a_avg_two_points_att',
    'h_avg_opp_rebounds',
    'h_avg_defensive_rebounds',
    'h_avg_defensive_rebounding_percentage',
    'h_avg_opp_two_points_made',
    'h_avg_free_throw_rate',
    'h_avg_opp_two_points_pct',
    'a_avg_opp_defensive_rating',
    'a_avg_defensive_rebounds',
    'a_avg_turnover_percentage',
    'h_avg_two_points_pct',
    'a_avg_defensive_rating',
    'h_avg_offensive_rebounds',
    'a_avg_opp_two_points_pct',
    'h_avg_two_points_att',
    'a_avg_free_throws_att',
    'a_avg_defensive_rebounding_percentage',
    'h_avg_opp_turnover_percentage',
    'h_avg_offensive_rating',
    'h_avg_blocks',
    'h_avg_free_throws_pct',
    'h_avg_opp_offensive_rebounding_percentage',
    'a_avg_offensive_rating',
    'h_avg_opp_offensive_rating',
    'h_avg_opp_three_points_pct',
    'h_avg_free_throws_att',
    'h_avg_opp_true_shooting_percentage',
    'h_avg_defensive_rating',
    'h_avg_block_rate',
]

features_3_h_and_a = features_3_h[:] + features_3_a[:]

features_1_both_h_and_a_and_2 = features_1_h_and_a[:] + features_2[:]

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

features_ht_1_h_and_a = [
    'h_h1_points',
    'h_h1_three_att',
    'h_h1_three',
    'h_h1_two_att',
    'h_h1_two',
    'h_h1_free_att',
    'h_h1_free',
    'h_h1_off_rebounds',
    'h_h1_rebounds',
    'h_h1_assists',
    'h_h1_blocks',
    'h_h1_turnovers',
    'h_h1_fouls',
    'a_h1_points',
    'a_h1_three_att',
    'a_h1_three',
    'a_h1_two_att',
    'a_h1_two',
    'a_h1_free_att',
    'a_h1_free',
    'a_h1_off_rebounds',
    'a_h1_rebounds',
    'a_h1_assists',
    'a_h1_blocks',
    'a_h1_turnovers',
    'a_h1_fouls'
]

features_ht_1_both = [
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
    'both_h1_fouls',
]

features_ht_1_h_and_a_and_both = features_1_h_and_a[:] + features_ht_1_h_and_a[:] + features_ht_1_both
features_ht_3_h_and_a_and_both = features_3_h_and_a[:] + features_ht_1_h_and_a[:] + features_ht_1_both
features_ht_4 = features_4[:] + features_ht_1_h_and_a[:] + features_ht_1_both
features_ht_5 = features_5[:] + features_ht_1_h_and_a[:] + features_ht_1_both
features_ht_6 = features_ht_1_h_and_a[:] + features_ht_1_both
features_ht_7 = features_ht_1_h_and_a[:] + features_ht_1_both[:] + [
    'h_h1_three_points_pct',
    'a_h1_three_points_pct',
    'h_h1_free_throws_pct',
    'a_h1_free_throws_pct',
    'h_h1_field_goals_made',
    'a_h1_field_goals_made',
    'h_h1_field_goals_att',
    'a_h1_field_goals_att',
    'h_h1_field_goals_pct',
    'a_h1_field_goals_pct',
    'h_h1_possessions',
    'a_h1_possessions',

    'h_h1_score_margin',
    'a_h1_score_margin',

    'h_h1_3pt_shot_selection',
    'a_h1_3pt_shot_selection',

    'h_h1_defensive_rating',
    'h_h1_offensive_rating',
    'h_h1_effective_field_goal_percentage',
    'h_h1_net_rating',
    'h_h1_turnover_percentage',
    'h_h1_true_shooting_percentage',
    'a_h1_defensive_rating',
    'a_h1_offensive_rating',
    'a_h1_effective_field_goal_percentage',
    'a_h1_net_rating',
    'a_h1_turnover_percentage',
    'a_h1_true_shooting_percentage',

    'h_h1_offensive_rebounding_percentage',
    'h_h1_defensive_rebounding_percentage',
    'h_h1_free_throw_rate',
    'h_h1_assist_rate',
    'h_h1_block_rate',
    'a_h1_offensive_rebounding_percentage',
    'a_h1_defensive_rebounding_percentage',
    'a_h1_free_throw_rate',
    'a_h1_assist_rate',
    'a_h1_block_rate',
]

features_ht_7_a = features_ht_1_h_and_a[:] + features_ht_1_both[:] + [
    'h_h1_possessions',
    'a_h1_possessions',
    'both_h1_possessions',
]


def clean_df(df, vars):
    df = df[vars]
    df = df.dropna(axis=0, how='any')

    return df

len(features_ht_6)
