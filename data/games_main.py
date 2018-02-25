'''

'''

__author__ = "Celso M. de Melo"
__email__ = "celsodemelo@eleveninc.com"

import pandas as pd
import features

df = pd.read_csv('games_wide_v9_feb_11_2018.csv')

print('Adding game stats...')
features.add_game_stats(df)

print('Adding season stats...')
df = features.add_season_stats(df)

print('Adding both team stats...')
features.add_both_teams_game_stats(df)

df.to_csv('games.csv', index=False)
