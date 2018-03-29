'''
Advanced statistics
'''

__author__ = "Celso M. de Melo"
__email__ = "celsodemelo@eleveninc.com"


def three_points_pct(three, three_att, decimal_places=5):
    if three_att == 0:
        return 0

    return round(100.0 * float(three) / float(three_att), decimal_places)


def free_throws_pct(free, free_att, decimal_places=5):
    if free_att == 0:
        return 0

    return round(100.0 * float(free) / float(free_att), decimal_places)


def three_point_shot_selection(three_points_att, field_goals_att, decimal_places=5):
    if field_goals_att == 0:
        return 0

    return round(float(three_points_att) / float(field_goals_att), decimal_places)


# https://www.sports-reference.com/cbb/about/glossary.html
def possessions(field_goals_att, free_throws_att, offensive_rebounds, turnovers,
                opp_field_goals_att, opp_free_throws_att, opp_offensive_rebounds, opp_turnovers):
    return 0.5 * (field_goals_att + 0.475 * free_throws_att - offensive_rebounds + turnovers) + \
           0.5 * (opp_field_goals_att + 0.475 * opp_free_throws_att - opp_offensive_rebounds + opp_turnovers)
