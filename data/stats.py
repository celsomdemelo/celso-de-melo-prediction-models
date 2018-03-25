'''
Advanced statistics
'''

__author__ = "Celso M. de Melo"
__email__ = "celsodemelo@eleveninc.com"


# https://www.sports-reference.com/cbb/about/glossary.html
def possessions(field_goals_att, free_throws_att, offensive_rebounds, turnovers,
                opp_field_goals_att, opp_free_throws_att, opp_offensive_rebounds, opp_turnovers):
    return 0.5 * (field_goals_att + 0.475 * free_throws_att - offensive_rebounds + turnovers) + \
           0.5 * (opp_field_goals_att + 0.475 * opp_free_throws_att - opp_offensive_rebounds + opp_turnovers)
