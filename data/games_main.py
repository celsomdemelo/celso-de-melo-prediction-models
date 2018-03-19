'''

'''

__author__ = "Celso M. de Melo"
__email__ = "celsodemelo@eleveninc.com"

import pandas as pd
import features

df = pd.read_csv('games_wide_v12_mar_17_2018.csv')
df = df[df.h_h1_points != -1]  # Assuming that if this is missing, the others in the NCAA pbp data are too (and vice-versa)

print('Adding game stats...')
features.add_game_stats(df)

print('Adding season stats...')
df = features.add_season_stats(df)

print('Adding both team stats...')
features.add_both_teams_game_stats(df)

df.to_csv('games.csv', index=False)
