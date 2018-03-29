'''
Functions to calculate relevant features

Reference for basketball stats: https://www.basketball-reference.com/about/glossary.html
'''

__author__ = "Celso M. de Melo"
__email__ = "celsodemelo@eleveninc.com"

import sys
import pickle

from data.stats import three_points_pct, free_throws_pct,  \
    three_point_shot_selection, possessions


def add_game_stats(df):
    stats = dict()

    df['h_points_game'] = -1
    df['a_points_game'] = -1

    df['h_field_goals_made'] = -1
    df['a_field_goals_made'] = -1
    df['h_field_goals_att'] = -1
    df['a_field_goals_att'] = -1
    df['h_field_goals_pct'] = 0.0
    df['a_field_goals_pct'] = 0.0

    df['h_three_points_made'] = -1
    df['a_three_points_made'] = -1
    df['h_three_points_att'] = -1
    df['a_three_points_att'] = -1
    df['h_three_points_pct'] = 0.0
    df['a_three_points_pct'] = 0.0

    df['h_two_points_made'] = -1
    df['a_two_points_made'] = -1
    df['h_two_points_att'] = -1
    df['a_two_points_att'] = -1
    df['h_two_points_pct'] = 0.0
    df['a_two_points_pct'] = 0.0

    df['h_blocks'] = -1
    df['a_blocks'] = -1

    df['h_free_throws_made'] = -1
    df['a_free_throws_made'] = -1
    df['h_free_throws_att'] = -1
    df['a_free_throws_att'] = -1
    df['h_free_throws_pct'] = 0.0
    df['a_free_throws_pct'] = 0.0

    df['h_offensive_rebounds'] = -1
    df['a_offensive_rebounds'] = -1

    df['h_defensive_rebounds'] = -1
    df['a_defensive_rebounds'] = -1

    df['h_rebounds'] = -1
    df['a_rebounds'] = -1

    df['h_assists'] = -1
    df['a_assists'] = -1

    df['h_turnovers'] = -1
    df['a_turnovers'] = -1

    df['h_personal_fouls'] = -1
    df['a_personal_fouls'] = -1

    df['h_score_margin'] = -1
    df['a_score_margin'] = -1

    df['h_3pt_shot_selection'] = -1.0
    df['a_3pt_shot_selection'] = -1.0

    # https://www.sports-reference.com/cbb/about/glossary.html
    df['h_possessions'] = -1.0
    df['h_defensive_rating'] = -1.0
    df['h_offensive_rating'] = -1.0
    df['h_effective_field_goal_percentage'] = -1.0
    df['h_net_rating'] = -1.0
    df['h_turnover_percentage'] = -1.0
    df['h_true_shooting_percentage'] = -1.0
    df['a_possessions'] = -1.0
    df['a_defensive_rating'] = -1.0
    df['a_offensive_rating'] = -1.0
    df['a_effective_field_goal_percentage'] = -1.0
    df['a_net_rating'] = -1.0
    df['a_turnover_percentage'] = -1.0
    df['a_true_shooting_percentage'] = -1.0

    # https://kenpom.com/blog/stats-explained/
    df['h_offensive_rebounding_percentage'] = -1.0
    df['h_defensive_rebounding_percentage'] = -1.0
    df['h_turnover_percentage'] = -1.0
    df['h_free_throw_rate'] = -1.0
    df['h_assist_rate'] = -1.0
    df['h_block_rate'] = -1.0
    df['a_offensive_rebounding_percentage'] = -1.0
    df['a_defensive_rebounding_percentage'] = -1.0
    df['a_turnover_percentage'] = -1.0
    df['a_free_throw_rate'] = -1.0
    df['a_assist_rate'] = -1.0
    df['a_block_rate'] = -1.0

    df['h_h1_three_points_pct'] = 0.0
    df['a_h1_three_points_pct'] = 0.0
    df['h_h1_free_throws_pct'] = 0.0
    df['a_h1_free_throws_pct'] = 0.0
    df['h_h1_field_goals_made'] = 0
    df['a_h1_field_goals_made'] = 0
    df['h_h1_field_goals_att'] = 0
    df['a_h1_field_goals_att'] = 0
    df['h_h1_field_goals_pct'] = 0.0
    df['a_h1_field_goals_pct'] = 0.0
    df['h_h1_possessions'] = -1.0
    df['a_h1_possessions'] = -1.0

    df['h_h1_score_margin'] = -1
    df['a_h1_score_margin'] = -1

    df['h_h1_3pt_shot_selection'] = -1.0
    df['a_h1_3pt_shot_selection'] = -1.0

    df['h_h1_defensive_rating'] = -1.0
    df['h_h1_offensive_rating'] = -1.0
    df['h_h1_effective_field_goal_percentage'] = -1.0
    df['h_h1_net_rating'] = -1.0
    df['h_h1_true_shooting_percentage'] = -1.0
    df['a_h1_defensive_rating'] = -1.0
    df['a_h1_offensive_rating'] = -1.0
    df['a_h1_effective_field_goal_percentage'] = -1.0
    df['a_h1_net_rating'] = -1.0
    df['a_h1_true_shooting_percentage'] = -1.0

    df['h_h1_offensive_rebounding_percentage'] = -1.0
    df['h_h1_defensive_rebounding_percentage'] = -1.0
    df['h_h1_turnover_percentage'] = -1.0
    df['h_h1_free_throw_rate'] = -1.0
    df['h_h1_assist_rate'] = -1.0
    df['h_h1_block_rate'] = -1.0
    df['a_h1_offensive_rebounding_percentage'] = -1.0
    df['a_h1_defensive_rebounding_percentage'] = -1.0
    df['a_h1_turnover_percentage'] = -1.0
    df['a_h1_free_throw_rate'] = -1.0
    df['a_h1_assist_rate'] = -1.0
    df['a_h1_block_rate'] = -1.0

    df['h_h2_three_points_pct'] = 0.0
    df['a_h2_three_points_pct'] = 0.0
    df['h_h2_free_throws_pct'] = 0.0
    df['a_h2_free_throws_pct'] = 0.0
    df['h_h2_field_goals_made'] = 0
    df['a_h2_field_goals_made'] = 0
    df['h_h2_field_goals_att'] = 0
    df['a_h2_field_goals_att'] = 0
    df['h_h2_field_goals_pct'] = 0.0
    df['a_h2_field_goals_pct'] = 0.0
    df['h_h2_possessions'] = -1.0
    df['a_h2_possessions'] = -1.0

    decimal_places = 5

    for index, row in df.iterrows():
        stat = 'h_points_game'
        stats[stat] = (row['h_h1_points'] + row['h_h2_points'])
        df.set_value(index, stat, stats[stat])
        stat = 'a_points_game'
        stats['a_points_game'] = (row['a_h1_points'] + row['a_h2_points'])
        df.set_value(index, stat, stats[stat])

        stat = 'h_field_goals_made'
        stats[stat] = (row['h_h1_two'] + row['h_h2_two'] + row['h_h1_three'] + row['h_h2_three'])
        df.set_value(index, stat, stats[stat])
        stat = 'a_field_goals_made'
        stats[stat] = (row['a_h1_two'] + row['a_h2_two'] + row['a_h1_three'] + row['a_h2_three'])
        df.set_value(index, stat, stats[stat])
        stat = 'h_field_goals_att'
        stats[stat] = (row['h_h1_two_att'] + row['h_h2_two_att'] + row['h_h1_three_att'] + row['h_h2_three_att'])
        df.set_value(index, stat, stats[stat])
        stat = 'a_field_goals_att'
        stats[stat] = (row['a_h1_two_att'] + row['a_h2_two_att'] + row['a_h1_three_att'] + row['a_h2_three_att'])
        df.set_value(index, stat, stats[stat])
        stat = 'h_field_goals_pct'
        if stats['h_field_goals_att'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = (
                round(100.0 * float(stats['h_field_goals_made']) / float(stats['h_field_goals_att']), decimal_places))
        df.set_value(index, stat, stats[stat])
        stat = 'a_field_goals_pct'
        if stats['a_field_goals_att'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = (
                round(100.0 * float(stats['a_field_goals_made']) / float(stats['a_field_goals_att']), decimal_places))
        df.set_value(index, stat, stats[stat])

        stat = 'h_three_points_made'
        stats[stat] = (row['h_h1_three'] + row['h_h2_three'])
        df.set_value(index, stat, stats[stat])
        stat = 'a_three_points_made'
        stats[stat] = (row['a_h1_three'] + row['a_h2_three'])
        df.set_value(index, stat, stats[stat])
        stat = 'h_three_points_att'
        stats[stat] = (row['h_h1_three_att'] + row['h_h2_three_att'])
        df.set_value(index, stat, stats[stat])
        stat = 'a_three_points_att'
        stats[stat] = (row['a_h1_three_att'] + row['a_h2_three_att'])
        df.set_value(index, stat, stats[stat])
        stat = 'h_three_points_pct'
        if stats['h_three_points_att'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = (
                round(100.0 * float(stats['h_three_points_made']) / float(stats['h_three_points_att']), decimal_places))
        df.set_value(index, stat, stats[stat])
        stat = 'a_three_points_pct'
        if stats['a_three_points_att'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = (
                round(100.0 * float(stats['a_three_points_made']) / float(stats['a_three_points_att']), decimal_places))
        df.set_value(index, stat, stats[stat])

        stat = 'h_two_points_made'
        stats[stat] = (row['h_h1_two'] + row['h_h2_two'])
        df.set_value(index, stat, stats[stat])
        stat = 'a_two_points_made'
        stats[stat] = (row['a_h1_two'] + row['a_h2_two'])
        df.set_value(index, stat, stats[stat])
        stat = 'h_two_points_att'
        stats[stat] = (row['h_h1_two_att'] + row['h_h2_two_att'])
        df.set_value(index, stat, stats[stat])
        stat = 'a_two_points_att'
        stats[stat] = (row['a_h1_two_att'] + row['a_h2_two_att'])
        df.set_value(index, stat, stats[stat])
        stat = 'h_two_points_pct'
        if stats['h_two_points_att'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = (
                round(100.0 * float(stats['h_two_points_made']) / float(stats['h_two_points_att']), decimal_places))
        df.set_value(index, stat, stats[stat])
        stat = 'a_two_points_pct'
        if stats['a_two_points_att'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = (
                round(100.0 * float(stats['a_two_points_made']) / float(stats['a_two_points_att']), decimal_places))
        df.set_value(index, stat, stats[stat])

        stat = 'h_blocks'
        stats[stat] = (row['h_h1_blocks'] + row['h_h2_blocks'])
        df.set_value(index, stat, stats[stat])
        stat = 'a_blocks'
        stats['a_blocks'] = (row['a_h1_blocks'] + row['a_h2_blocks'])
        df.set_value(index, stat, stats[stat])

        stat = 'h_free_throws_made'
        stats[stat] = (row['h_h1_free'] + row['h_h2_free'])
        df.set_value(index, stat, stats[stat])
        stat = 'a_free_throws_made'
        stats[stat] = (row['a_h1_free'] + row['a_h2_free'])
        df.set_value(index, stat, stats[stat])
        stat = 'h_free_throws_att'
        stats[stat] = (row['h_h1_free_att'] + row['h_h2_free_att'])
        df.set_value(index, stat, stats[stat])
        stat = 'a_free_throws_att'
        stats[stat] = (row['a_h1_free_att'] + row['a_h2_free_att'])
        df.set_value(index, stat, stats[stat])
        stat = 'h_free_throws_pct'
        if stats['h_free_throws_att'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = (
                round(100.0 * float(stats['h_free_throws_made']) / float(stats['h_free_throws_att']), decimal_places))
        df.set_value(index, stat, stats[stat])
        stat = 'a_free_throws_pct'
        if stats['a_free_throws_att'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = (
                round(100.0 * float(stats['a_free_throws_made']) / float(stats['a_free_throws_att']), decimal_places))
        df.set_value(index, stat, stats[stat])

        stat = 'h_offensive_rebounds'
        stats[stat] = (row['h_h1_off_rebounds'] + row['h_h2_off_rebounds'])
        df.set_value(index, stat, stats[stat])
        stat = 'a_offensive_rebounds'
        stats[stat] = (row['a_h1_off_rebounds'] + row['a_h2_off_rebounds'])
        df.set_value(index, stat, stats[stat])
        stat = 'h_defensive_rebounds'
        stats[stat] = (row['h_h1_def_rebounds'] + row['h_h2_def_rebounds'])
        df.set_value(index, stat, stats[stat])
        stat = 'a_defensive_rebounds'
        stats[stat] = (row['a_h1_def_rebounds'] + row['a_h2_def_rebounds'])
        df.set_value(index, stat, stats[stat])
        stat = 'h_rebounds'
        stats[stat] = (row['h_h1_rebounds'] + row['h_h2_rebounds'])
        df.set_value(index, stat, stats[stat])
        stat = 'a_rebounds'
        stats[stat] = (row['a_h1_rebounds'] + row['a_h2_rebounds'])
        df.set_value(index, stat, stats[stat])

        stat = 'h_assists'
        stats[stat] = (row['h_h1_assists'] + row['h_h2_assists'])
        df.set_value(index, stat, stats[stat])
        stat = 'a_assists'
        stats[stat] = (row['a_h1_assists'] + row['a_h2_assists'])
        df.set_value(index, stat, stats[stat])
        stat = 'h_turnovers'
        stats[stat] = (row['h_h1_turnovers'] + row['h_h2_turnovers'])
        df.set_value(index, stat, stats[stat])
        stat = 'a_turnovers'
        stats[stat] = (row['a_h1_turnovers'] + row['a_h2_turnovers'])
        df.set_value(index, stat, stats[stat])
        stat = 'h_personal_fouls'
        stats[stat] = (row['h_h1_fouls'] + row['h_h2_fouls'])
        df.set_value(index, stat, stats[stat])
        stat = 'a_personal_fouls'
        stats[stat] = (row['a_h1_fouls'] + row['a_h2_fouls'])
        df.set_value(index, stat, stats[stat])

        stat = 'h_score_margin'
        stats[stat] = stats['h_points_game'] - stats['a_points_game']
        df.set_value(index, stat, stats[stat])
        stat = 'a_score_margin'
        stats[stat] = stats['a_points_game'] - stats['h_points_game']
        df.set_value(index, stat, stats[stat])
        stat = 'h_3pt_shot_selection'
        if stats['h_three_points_att'] == -1 or stats['h_field_goals_att'] == -1 or stats['h_field_goals_att'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = three_point_shot_selection(
                stats['h_three_points_att'], stats['h_field_goals_att'], decimal_places)
        df.set_value(index, stat, stats[stat])
        stat = 'a_3pt_shot_selection'
        if stats['a_three_points_att'] == -1 or stats['a_field_goals_att'] == -1 or stats['a_field_goals_att'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = three_point_shot_selection(
                stats['a_three_points_att'], stats['a_field_goals_att'], decimal_places)
        df.set_value(index, stat, stats[stat])

        stat = 'h_possessions'
        if stats['h_field_goals_att'] == -1:
            stats[stat] = -1
        else:
            stats[stat] = possessions(stats['h_field_goals_att'], stats['h_free_throws_att'],
                                      stats['h_offensive_rebounds'], stats['h_turnovers'],
                                      stats['a_field_goals_att'], stats['a_free_throws_att'],
                                      stats['a_offensive_rebounds'], stats['a_turnovers'])
        df.set_value(index, stat, stats[stat])
        stat = 'h_defensive_rating'
        if stats['h_possessions'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = 100 * (stats['a_points_game'] / stats['h_possessions'])
        df.set_value(index, stat, stats[stat])
        stat = 'h_offensive_rating'
        if stats['h_possessions'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = 100 * (stats['h_points_game'] / stats['h_possessions'])
        df.set_value(index, stat, stats[stat])
        stat = 'h_effective_field_goal_percentage'
        if stats['h_field_goals_att'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = (stats['h_field_goals_made'] + 0.5 * stats['h_three_points_made']) / stats[
                'h_field_goals_att']
        df.set_value(index, stat, stats[stat])
        stat = 'h_net_rating'
        if stats['h_possessions'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = 100 * ((stats['h_points_game'] - stats['a_points_game']) / stats['h_possessions'])
        df.set_value(index, stat, stats[stat])
        stat = 'h_turnover_percentage'
        if stats['h_field_goals_att'] == 0 and stats['a_free_throws_att'] == 0 and stats['h_turnovers'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = 100 * stats['h_turnovers'] / (
                stats['h_field_goals_att'] + 0.475 * stats['a_free_throws_att'] + stats['h_turnovers'])
        df.set_value(index, stat, stats[stat])
        stat = 'h_true_shooting_percentage'
        if stats['h_field_goals_att'] == 0 and stats['a_free_throws_att'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = stats['h_points_game'] / (
                2 * (stats['h_field_goals_att'] + 0.475 * stats['a_free_throws_att']))
        df.set_value(index, stat, stats[stat])
        stat = 'a_possessions'
        if stats['a_field_goals_att'] == -1:
            stats[stat] = -1
        else:
            stats[stat] = possessions(stats['a_field_goals_att'], stats['a_free_throws_att'],
                                      stats['a_offensive_rebounds'], stats['a_turnovers'],
                                      stats['h_field_goals_att'], stats['h_free_throws_att'],
                                      stats['h_offensive_rebounds'], stats['h_turnovers'])
        df.set_value(index, stat, stats[stat])
        stat = 'a_defensive_rating'
        if stats['a_possessions'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = 100 * (stats['h_points_game'] / stats['a_possessions'])
        df.set_value(index, stat, stats[stat])
        stat = 'a_offensive_rating'
        if stats['a_possessions'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = 100 * (stats['a_points_game'] / stats['a_possessions'])
        df.set_value(index, stat, stats[stat])
        stat = 'a_effective_field_goal_percentage'
        if stats['a_field_goals_att'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = (stats['a_field_goals_made'] + 0.5 * stats['a_three_points_made']) / stats[
                'a_field_goals_att']
        df.set_value(index, stat, stats[stat])
        stat = 'a_net_rating'
        if stats['a_possessions'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = 100 * ((stats['a_points_game'] - stats['h_points_game']) / stats['a_possessions'])
        df.set_value(index, stat, stats[stat])
        stat = 'a_turnover_percentage'
        if stats['a_field_goals_att'] == 0 and stats['h_free_throws_att'] == 0 and stats['a_turnovers'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = 100 * stats['a_turnovers'] / (
                stats['a_field_goals_att'] + 0.475 * stats['h_free_throws_att'] + stats['a_turnovers'])
        df.set_value(index, stat, stats[stat])
        stat = 'a_true_shooting_percentage'
        if stats['a_field_goals_att'] == 0 and stats['h_free_throws_att'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = stats['a_points_game'] / (
                2 * (stats['a_field_goals_att'] + 0.475 * stats['h_free_throws_att']))
        df.set_value(index, stat, stats[stat])
        
        stat = 'h_offensive_rebounding_percentage'
        if stats['h_offensive_rebounds'] == 0 and stats['h_defensive_rebounds'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = stats['h_offensive_rebounds'] / (
                stats['h_offensive_rebounds'] + stats['h_defensive_rebounds'])
        df.set_value(index, stat, stats[stat])
        stat = 'h_defensive_rebounding_percentage'
        if stats['h_offensive_rebounds'] == 0 and stats['h_defensive_rebounds'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = stats['h_defensive_rebounds'] / (
                stats['h_offensive_rebounds'] + stats['h_defensive_rebounds'])
        df.set_value(index, stat, stats[stat])
        stat = 'h_turnover_percentage'
        if stats['h_possessions'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = stats['h_turnovers'] / stats['h_possessions']
        df.set_value(index, stat, stats[stat])
        stat = 'h_free_throw_rate'
        if stats['h_field_goals_att'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = stats['a_free_throws_att'] / stats['h_field_goals_att']
        df.set_value(index, stat, stats[stat])
        stat = 'h_assist_rate'
        if stats['h_field_goals_made'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = stats['h_assists'] / stats['h_field_goals_made']
        df.set_value(index, stat, stats[stat])
        stat = 'h_block_rate'
        if stats['a_two_points_att'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = stats['h_blocks'] / stats['a_two_points_att']
        df.set_value(index, stat, stats[stat])
        stat = 'a_offensive_rebounding_percentage'
        if stats['a_offensive_rebounds'] == 0 and stats['a_defensive_rebounds'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = stats['a_offensive_rebounds'] / (
                stats['a_offensive_rebounds'] + stats['a_defensive_rebounds'])
        df.set_value(index, stat, stats[stat])
        stat = 'a_defensive_rebounding_percentage'
        if stats['a_offensive_rebounds'] == 0 and stats['a_defensive_rebounds'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = stats['a_defensive_rebounds'] / (
                stats['a_offensive_rebounds'] + stats['a_defensive_rebounds'])
        df.set_value(index, stat, stats[stat])
        stat = 'a_turnover_percentage'
        if stats['a_possessions'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = stats['a_turnovers'] / stats['a_possessions']
        df.set_value(index, stat, stats[stat])
        stat = 'a_free_throw_rate'
        if stats['a_field_goals_att'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = stats['h_free_throws_att'] / stats['a_field_goals_att']
        df.set_value(index, stat, stats[stat])
        stat = 'a_assist_rate'
        if stats['a_field_goals_made'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = stats['a_assists'] / stats['a_field_goals_made']
        df.set_value(index, stat, stats[stat])
        stat = 'a_block_rate'
        if stats['h_two_points_att'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = stats['a_blocks'] / stats['h_two_points_att']
        df.set_value(index, stat, stats[stat])

        stat = 'h_h1_three_points_pct'
        if row['h_h1_three'] == -1 or row['h_h1_three_att'] == -1 or row['h_h1_three_att'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = three_points_pct(row['h_h1_three'], row['h_h1_three_att'], decimal_places)
        df.set_value(index, stat, stats[stat])
        stat = 'a_h1_three_points_pct'
        if row['a_h1_three'] == -1 or row['a_h1_three_att'] == -1 or row['a_h1_three_att'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = three_points_pct(row['a_h1_three'], row['a_h1_three_att'], decimal_places)
        df.set_value(index, stat, stats[stat])
        stat = 'h_h1_free_throws_pct'
        if row['h_h1_free'] == -1 or row['h_h1_free_att'] == -1 or row['h_h1_free_att'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = free_throws_pct(row['h_h1_free'], row['h_h1_free_att'], decimal_places)
        df.set_value(index, stat, stats[stat])
        stat = 'a_h1_free_throws_pct'
        if row['a_h1_free'] == -1 or row['a_h1_free_att'] == -1 or row['a_h1_free_att'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = free_throws_pct(row['a_h1_free'], row['a_h1_free_att'], decimal_places)
        df.set_value(index, stat, stats[stat])
        stat = 'h_h1_field_goals_made'
        if row['h_h1_three'] == -1 or row['h_h1_two'] == -1:
            stats[stat] = -1
        else:
            stats[stat] = (row['h_h1_three'] + row['h_h1_two'])
        df.set_value(index, stat, stats[stat])
        stat = 'a_h1_field_goals_made'
        if row['a_h1_three'] == -1 or row['a_h1_two'] == -1:
            stats[stat] = -1
        else:
            stats[stat] = (row['a_h1_three'] + row['a_h1_two'])
        df.set_value(index, stat, stats[stat])
        stat = 'h_h1_field_goals_att'
        if row['h_h1_three_att'] == -1 or row['h_h1_two_att'] == -1:
            stats[stat] = -1
        else:
            stats[stat] = (row['h_h1_three_att'] + row['h_h1_two_att'])
        df.set_value(index, stat, stats[stat])
        stat = 'a_h1_field_goals_att'
        if row['a_h1_three_att'] == -1 or row['a_h1_two_att'] == -1:
            stats[stat] = -1
        else:
            stats[stat] = (row['a_h1_three_att'] + row['a_h1_two_att'])
        df.set_value(index, stat, stats[stat])
        stat = 'h_h1_field_goals_pct'
        if stats['h_h1_field_goals_att'] == -1 or stats['h_h1_field_goals_att'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = (
                round(100.0 * float(row['h_h1_three'] + row['h_h1_two']) / float(stats['h_h1_field_goals_att']),
                      decimal_places))
        df.set_value(index, stat, stats[stat])
        stat = 'a_h1_field_goals_pct'
        if stats['a_h1_field_goals_att'] == -1 or stats['a_h1_field_goals_att'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = (
                round(100.0 * float(row['a_h1_three'] + row['a_h1_two']) / float(stats['a_h1_field_goals_att']),
                      decimal_places))
        df.set_value(index, stat, stats[stat])
        stat = 'h_h1_possessions'
        if row['h_h1_field_goals_att'] == -1 or row['h_h1_turnovers'] == -1 or row['h_h1_free_att'] == -1 or row[
            'h_h1_off_rebounds'] == -1:
            stats[stat] = -1
        else:
            stats[stat] = ((
                stats['h_h1_field_goals_att'] + row['h_h1_turnovers'] + 0.475 * row['h_h1_free_att'] -
                row['h_h1_off_rebounds']))
        df.set_value(index, stat, stats[stat])
        stat = 'a_h1_possessions'
        if row['a_h1_field_goals_att'] == -1 or row['a_h1_turnovers'] == -1 or row['a_h1_free_att'] == -1 or row[
            'a_h1_off_rebounds'] == -1:
            stats[stat] = -1
        else:
            stats[stat] = ((
                stats['a_h1_field_goals_att'] + row['a_h1_turnovers'] + 0.475 * row['a_h1_free_att'] -
                row['a_h1_off_rebounds']))
        df.set_value(index, stat, stats[stat])

        stat = 'h_h1_score_margin'
        stats[stat] = row['h_h1_points'] - row['a_h1_points']
        df.set_value(index, stat, stats[stat])
        stat = 'a_h1_score_margin'
        stats[stat] = row['a_h1_points'] - row['h_h1_points']
        df.set_value(index, stat, stats[stat])

        stat = 'h_h1_3pt_shot_selection'
        if row['h_h1_three_att'] == -1 or stats['h_h1_field_goals_att'] == -1 or stats[
            'h_h1_field_goals_att'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = three_point_shot_selection(
                row['h_h1_three_att'], stats['h_h1_field_goals_att'], decimal_places)
        df.set_value(index, stat, stats[stat])
        stat = 'a_h1_3pt_shot_selection'
        if row['a_h1_three_att'] == -1 or stats['a_h1_field_goals_att'] == -1 or stats['a_h1_field_goals_att'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = three_point_shot_selection(
                row['a_h1_three_att'], stats['a_h1_field_goals_att'], decimal_places)
        df.set_value(index, stat, stats[stat])

        stat = 'h_h1_defensive_rating'
        if stats['h_h1_possessions'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = 100 * (row['a_h1_points'] / stats['h_h1_possessions'])
        df.set_value(index, stat, stats[stat])
        stat = 'h_h1_offensive_rating'
        if stats['h_h1_possessions'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = 100 * (row['h_h1_points'] / stats['h_h1_possessions'])
        df.set_value(index, stat, stats[stat])
        stat = 'h_h1_effective_field_goal_percentage'
        if stats['h_h1_field_goals_att'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = (stats['h_h1_field_goals_made'] + 0.5 * row['h_h1_three']) / stats['h_h1_field_goals_att']
        df.set_value(index, stat, stats[stat])
        stat = 'h_h1_net_rating'
        if stats['h_h1_possessions'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = 100 * ((row['h_h1_points'] - row['a_h1_points']) / stats['h_h1_possessions'])
        df.set_value(index, stat, stats[stat])
        stat = 'h_h1_turnover_percentage'
        if stats['h_h1_field_goals_att'] == 0 and row['a_h1_free_att'] == 0 and row['h_h1_turnovers'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = 100 * row['h_h1_turnovers'] / (
                        stats['h_h1_field_goals_att'] + 0.475 * row['a_h1_free_att'] + row['h_h1_turnovers'])
        df.set_value(index, stat, stats[stat])
        stat = 'h_h1_true_shooting_percentage'
        if stats['h_h1_field_goals_att'] == 0 and row['a_h1_free_att'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = row['h_h1_points'] / (
                        2 * (stats['h_h1_field_goals_att'] + 0.475 * row['a_h1_free_att']))
        df.set_value(index, stat, stats[stat])

        stat = 'a_h1_defensive_rating'
        if stats['a_h1_possessions'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = 100 * (row['h_h1_points'] / stats['a_h1_possessions'])
        df.set_value(index, stat, stats[stat])
        stat = 'a_h1_offensive_rating'
        if stats['a_h1_possessions'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = 100 * (row['a_h1_points'] / stats['a_h1_possessions'])
        df.set_value(index, stat, stats[stat])
        stat = 'a_h1_effective_field_goal_percentage'
        if stats['a_h1_field_goals_att'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = (stats['a_h1_field_goals_made'] + 0.5 * row['a_h1_three']) / stats['a_h1_field_goals_att']
        df.set_value(index, stat, stats[stat])
        stat = 'a_h1_net_rating'
        if stats['a_h1_possessions'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = 100 * ((row['a_h1_points'] - row['h_h1_points']) / stats['a_h1_possessions'])
        df.set_value(index, stat, stats[stat])
        stat = 'a_h1_turnover_percentage'
        if stats['a_h1_field_goals_att'] == 0 and row['h_h1_free_att'] == 0 and row['a_h1_turnovers'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = 100 * row['a_h1_turnovers'] / (
                        stats['a_h1_field_goals_att'] + 0.475 * row['h_h1_free_att'] + row['a_h1_turnovers'])
        df.set_value(index, stat, stats[stat])
        stat = 'a_h1_true_shooting_percentage'
        if stats['a_h1_field_goals_att'] == 0 and row['h_h1_free_att'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = row['a_h1_points'] / (
                        2 * (stats['a_h1_field_goals_att'] + 0.475 * row['h_h1_free_att']))
        df.set_value(index, stat, stats[stat])
        
        stat = 'h_h1_offensive_rebounding_percentage'
        if row['h_h1_off_rebounds'] == 0 and row['h_h1_def_rebounds'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = row['h_h1_off_rebounds'] / (
                        row['h_h1_off_rebounds'] + row['h_h1_def_rebounds'])
        df.set_value(index, stat, stats[stat])
        stat = 'h_h1_defensive_rebounding_percentage'
        if row['h_h1_off_rebounds'] == 0 and row['h_h1_def_rebounds'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = row['h_h1_def_rebounds'] / (
                        row['h_h1_off_rebounds'] + row['h_h1_def_rebounds'])
        df.set_value(index, stat, stats[stat])
        stat = 'h_h1_turnover_percentage'
        if stats['h_h1_possessions'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = row['h_h1_turnovers'] / stats['h_h1_possessions']
        df.set_value(index, stat, stats[stat])
        stat = 'h_h1_free_throw_rate'
        if stats['h_h1_field_goals_att'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = row['a_h1_free_att'] / stats['h_h1_field_goals_att']
        df.set_value(index, stat, stats[stat])
        stat = 'h_h1_assist_rate'
        if stats['h_h1_field_goals_made'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = row['h_h1_assists'] / stats['h_h1_field_goals_made']
        df.set_value(index, stat, stats[stat])
        stat = 'h_h1_block_rate'
        if row['a_h1_two_att'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = row['h_h1_blocks'] / row['a_h1_two_att']
        df.set_value(index, stat, stats[stat])
        
        stat = 'a_h1_offensive_rebounding_percentage'
        if row['a_h1_off_rebounds'] == 0 and row['a_h1_def_rebounds'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = row['a_h1_off_rebounds'] / (
                        row['a_h1_off_rebounds'] + row['a_h1_def_rebounds'])
        df.set_value(index, stat, stats[stat])
        stat = 'a_h1_defensive_rebounding_percentage'
        if row['a_h1_off_rebounds'] == 0 and row['a_h1_def_rebounds'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = row['a_h1_def_rebounds'] / (
                        row['a_h1_off_rebounds'] + row['a_h1_def_rebounds'])
        df.set_value(index, stat, stats[stat])
        stat = 'a_h1_turnover_percentage'
        if stats['a_h1_possessions'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = row['a_h1_turnovers'] / stats['a_h1_possessions']
        df.set_value(index, stat, stats[stat])
        stat = 'a_h1_free_throw_rate'
        if stats['a_h1_field_goals_att'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = row['h_h1_free_att'] / stats['a_h1_field_goals_att']
        df.set_value(index, stat, stats[stat])
        stat = 'a_h1_assist_rate'
        if stats['a_h1_field_goals_made'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = row['a_h1_assists'] / stats['a_h1_field_goals_made']
        df.set_value(index, stat, stats[stat])
        stat = 'a_h1_block_rate'
        if row['h_h1_two_att'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = row['a_h1_blocks'] / row['h_h1_two_att']
        df.set_value(index, stat, stats[stat])

        stat = 'h_h2_three_points_pct'
        if row['h_h2_three'] == -1 or row['h_h2_three_att'] == -1 or row['h_h2_three_att'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = (round(100.0 * float(row['h_h2_three']) / float(row['h_h2_three_att']), decimal_places))
        df.set_value(index, stat, stats[stat])
        stat = 'a_h2_three_points_pct'
        if row['a_h2_three'] == -1 or row['a_h2_three_att'] == -1 or row['a_h2_three_att'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = (round(100.0 * float(row['a_h2_three']) / float(row['a_h2_three_att']), decimal_places))
        df.set_value(index, stat, stats[stat])
        stat = 'h_h2_free_throws_pct'
        if row['h_h2_free'] == -1 or row['h_h2_free_att'] == -1 or row['h_h2_free_att'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = (round(100.0 * float(row['h_h2_free']) / float(row['h_h2_free_att']), decimal_places))
        df.set_value(index, stat, stats[stat])
        stat = 'a_h2_free_throws_pct'
        if row['a_h2_free'] == -1 or row['a_h2_free_att'] == -1 or row['a_h2_free_att'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = (
                round(100.0 * float(row['a_h2_free']) / float(row['a_h2_free_att']), decimal_places))
        df.set_value(index, stat, stats[stat])
        stat = 'h_h2_field_goals_made'
        if row['h_h2_three'] == -1 or row['h_h2_two'] == -1:
            stats[stat] = -1
        else:
            stats[stat] = (row['h_h2_three'] + row['h_h2_two'])
        df.set_value(index, stat, stats[stat])
        stat = 'a_h2_field_goals_made'
        if row['a_h2_three'] == -1 or row['a_h2_two'] == -1:
            stats[stat] = -1
        else:
            stats[stat] = (row['a_h2_three'] + row['a_h2_two'])
        df.set_value(index, stat, stats[stat])
        stat = 'h_h2_field_goals_att'
        if row['h_h2_three_att'] == -1 or row['h_h2_two_att'] == -1:
            stats[stat] = -1
        else:
            stats[stat] = (row['h_h2_three_att'] + row['h_h2_two_att'])
        df.set_value(index, stat, stats[stat])
        stat = 'a_h2_field_goals_att'
        if row['a_h2_three_att'] == -1 or row['a_h2_two_att'] == -1:
            stats[stat] = -1
        else:
            stats[stat] = (row['a_h2_three_att'] + row['a_h2_two_att'])
        df.set_value(index, stat, stats[stat])
        stat = 'h_h2_field_goals_pct'
        if stats['h_h2_field_goals_att'] == -1 or stats['h_h2_field_goals_att'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = (
                round(100.0 * float(row['h_h2_three'] + row['h_h2_two']) / float(stats['h_h2_field_goals_att']),
                      decimal_places))
        df.set_value(index, stat, stats[stat])
        stat = 'a_h2_field_goals_pct'
        if stats['a_h2_field_goals_att'] == -1 or stats['a_h2_field_goals_att'] == 0:
            stats[stat] = -1
        else:
            stats[stat] = (
                round(100.0 * float(row['a_h2_three'] + row['a_h2_two']) / float(stats['a_h2_field_goals_att']),
                      decimal_places))
        df.set_value(index, stat, stats[stat])
        stat = 'h_h2_possessions'
        if row['h_h2_field_goals_att'] == -1 or row['h_h2_turnovers'] == -1 or row['h_h2_free_att'] == -1 or row[
            'h_h2_off_rebounds'] == -1:
            stats[stat] = -1
        else:
            stats[stat] = stats[stat] = ((
                stats['h_h2_field_goals_att'] + row['h_h2_turnovers'] + 0.475 * row['h_h2_free_att'] -
                row['h_h2_off_rebounds']))
        df.set_value(index, stat, stats[stat])
        stat = 'a_h2_possessions'
        if row['a_h2_field_goals_att'] == -1 or row['a_h2_turnovers'] == -1 or row['a_h2_free_att'] == -1 or row[
            'a_h2_off_rebounds'] == -1:
            stats[stat] = -1
        else:
            stats[stat] = ((
                stats['a_h2_field_goals_att'] + row['a_h2_turnovers'] + 0.475 * row['a_h2_free_att'] -
                row['a_h2_off_rebounds']))
        df.set_value(index, stat, stats[stat])

    opp_vars = []
    for v in list(stats.keys()):
        if 'h_' in v[:2]:
            opp_vars.append(v[2:])

    for ov in opp_vars:
        df['h_opp_' + ov] = -1.0
        df['a_opp_' + ov] = -1.0

    for index, row in df.iterrows():
        for ov in opp_vars:
            df.set_value(index, 'h_opp_' + ov, row['a_' + ov])
            df.set_value(index, 'a_opp_' + ov, row['h_' + ov])


def add_season_stats(df):
    df = df.sort_values(by='scheduled_date')

    vars = []
    for v in df:
        if 'h_' in v[:2] and 'h_ht_' not in v[:5] and (df[v].dtype != 'O'):
            vars.append(v[2:])

    df['h_wins'] = 0
    df['h_rank_wins'] = 0
    df['h_losses'] = 0
    df['h_rank_losses'] = 0
    df['h_streak'] = 0
    df['h_n_games'] = 0
    df['a_wins'] = 0
    df['a_rank_wins'] = 0
    df['a_losses'] = 0
    df['a_rank_losses'] = 0
    df['a_streak'] = 0
    df['a_n_games'] = 0
    df['both_wins'] = 0
    df['both_losses'] = 0

    for v in vars:
        df['h_avg_' + v] = 0.0
        df['h_total_' + v] = 0.0
        df['h_rank_total_' + v] = 0
        df['h_rank_avg_' + v] = 0
        df['a_avg_' + v] = 0.0
        df['a_total_' + v] = 0.0
        df['a_rank_total_' + v] = 0
        df['a_rank_avg_' + v] = 0
        df['both_avg_' + v] = 0.0
        df['both_total_' + v] = 0.0

    def create_empty_stats_record():
        rec = dict()

        rec['W'] = 0
        rec['L'] = 0
        rec['S'] = 0
        rec['n_games'] = 0

        rec['rank_W'] = 0
        rec['rank_L'] = 0

        for v in vars:
            rec['total_' + v] = 0.0
            rec['avg_' + v] = 0.0
            rec['rank_total_' + v] = 0
            rec['rank_avg_' + v] = 0

        return rec

    def reset_table_stats():
        stats = dict()
        for index, row in df.iterrows():
            if row['h_market'] not in stats:
                stats[row['h_market']] = create_empty_stats_record()
            if row['a_market'] not in stats:
                stats[row['a_market']] = create_empty_stats_record()
        return stats

    def save_table_stats(name, ts):
        pickle_out = open(name, "wb")
        pickle.dump(ts, pickle_out)
        pickle_out.close()

    season = -1

    def set_rankings(stats, var):
        sorted_stats = sorted(stats.items(), key=lambda stat: stat[1][var], reverse=True)
        rank = 1
        effective_rank = 1
        effective_rank_value = sys.maxsize
        if sorted_stats[0][1][var] != sorted_stats[len(sorted_stats) - 1][1][var]:
            for stat in sorted_stats:
                if stats[stat[0]][var] != effective_rank_value:
                    effective_rank_value = stats[stat[0]][var]
                    effective_rank = rank
                stats[stat[0]]['rank_' + var] = (effective_rank)
                rank += 1
        else:  # Data for this variable is likely missing
            for stat in sorted_stats:
                stats[stat[0]]['rank_' + var] = (0)

    row_count = 0
    for index, row in df.iterrows():
        if row_count % 500 == 0:
            print('game #' + str(row_count))
        row_count += 1

        if row['season'] != season:
            season = row['season']
            table_stats = reset_table_stats()

        df.set_value(index, 'h_wins', table_stats[row['h_market']]['W'])
        df.set_value(index, 'h_rank_wins', table_stats[row['h_market']]['rank_W'])
        df.set_value(index, 'h_losses', table_stats[row['h_market']]['L'])
        df.set_value(index, 'h_rank_losses', table_stats[row['h_market']]['rank_L'])
        df.set_value(index, 'h_n_games', table_stats[row['h_market']]['n_games'])
        df.set_value(index, 'h_streak', table_stats[row['h_market']]['S'])
        df.set_value(index, 'a_wins', table_stats[row['a_market']]['W'])
        df.set_value(index, 'a_rank_wins', table_stats[row['a_market']]['rank_W'])
        df.set_value(index, 'a_losses', table_stats[row['a_market']]['L'])
        df.set_value(index, 'a_rank_losses', table_stats[row['a_market']]['rank_L'])
        df.set_value(index, 'a_streak', table_stats[row['a_market']]['S'])
        df.set_value(index, 'a_n_games', table_stats[row['a_market']]['n_games'])
        df.set_value(index, 'both_wins', table_stats[row['h_market']]['W'] + table_stats[row['a_market']]['W'])
        df.set_value(index, 'both_losses', table_stats[row['h_market']]['L'] + table_stats[row['a_market']]['L'])

        if row['a_points_game'] > row['h_points_game']:
            table_stats[row['a_market']]['W'] += 1
            table_stats[row['h_market']]['L'] += 1

            if table_stats[row['h_market']]['S'] >= 0:
                table_stats[row['h_market']]['S'] = -1
            else:
                table_stats[row['h_market']]['S'] -= 1

            if table_stats[row['a_market']]['S'] < 0:
                table_stats[row['a_market']]['S'] = 1
            else:
                table_stats[row['a_market']]['S'] += 1
        else:
            table_stats[row['h_market']]['W'] += 1
            table_stats[row['a_market']]['L'] += 1

            if table_stats[row['a_market']]['S'] >= 0:
                table_stats[row['a_market']]['S'] = -1
            else:
                table_stats[row['a_market']]['S'] -= 1

            if table_stats[row['h_market']]['S'] < 0:
                table_stats[row['h_market']]['S'] = 1
            else:
                table_stats[row['h_market']]['S'] += 1

        table_stats[row['h_market']]['n_games'] += 1
        table_stats[row['a_market']]['n_games'] += 1

        set_rankings(table_stats, 'W')
        set_rankings(table_stats, 'L')

        decimal_places = 5

        for v in vars:
            df.set_value(index, 'h_avg_' + v, round(table_stats[row['h_market']]['avg_' + v], decimal_places))
            df.set_value(index, 'h_total_' + v, round(table_stats[row['h_market']]['total_' + v]), decimal_places)
            df.set_value(index, 'h_rank_total_' + v, table_stats[row['h_market']]['rank_total_' + v])
            df.set_value(index, 'h_rank_avg_' + v, table_stats[row['h_market']]['rank_avg_' + v])
            df.set_value(index, 'a_avg_' + v, round(table_stats[row['a_market']]['avg_' + v]), decimal_places)
            df.set_value(index, 'a_total_' + v, round(table_stats[row['a_market']]['total_' + v]), decimal_places)
            df.set_value(index, 'a_rank_total_' + v, table_stats[row['a_market']]['rank_total_' + v])
            df.set_value(index, 'a_rank_avg_' + v, table_stats[row['a_market']]['rank_avg_' + v])
            df.set_value(index, 'both_avg_' + v, round(
                (float(table_stats[row['a_market']]['avg_' + v]) +
                 float(table_stats[row['h_market']]['avg_' + v])) / 2.0), decimal_places)
            df.set_value(index, 'both_total_' + v, round(
                table_stats[row['a_market']]['total_' + v] + table_stats[row['h_market']]['total_' + v]),
                         decimal_places)

            if row['h_' + v] != -1:
                table_stats[row['h_market']]['total_' + v] += row['h_' + v]
            table_stats[row['h_market']]['avg_' + v] = round(table_stats[row['h_market']]['total_' + v] /
                                                             table_stats[row['h_market']]['n_games'], decimal_places)
            if row['a_' + v] != -1:
                table_stats[row['a_market']]['total_' + v] += row['a_' + v]
            table_stats[row['a_market']]['avg_' + v] = round(table_stats[row['a_market']]['total_' + v] /
                                                             table_stats[row['a_market']]['n_games'], decimal_places)

            set_rankings(table_stats, 'total_' + v)
            set_rankings(table_stats, 'avg_' + v)
    save_table_stats('season_stats_' + str(season) + '.pkl', table_stats)

    return df


def add_both_teams_game_stats(df):
    vars = []
    for v in df:
        if ('h_' in v[:2]) and ('_total_' not in v) and ('_avg_' not in v) and ('rank' not in v) and (
                    df[v].dtype != 'O'):
            vars.append(v[2:])

    decimal_places = 5

    for index, row in df.iterrows():
        for v in vars:
            df.set_value(index, 'both_' + v, round(row['h_' + v] + row['a_' + v]), decimal_places)
