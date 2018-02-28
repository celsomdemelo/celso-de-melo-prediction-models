--- teams_games
---
--- This view provides stat totals by 5 min. fixed windows in each half, as
--- well as the half totals and full game totals.
---
--- This data is based on [play_by_play].ncaa_pbp_mbb] which is missing games that are
--- contained in [stardust.games_v*].
---
--- This view contains 2 rows per game. One for home team, one for away team.
---
--- For example, opp_splits.h2_4_off_rebounds is the total number of
--- offensive rebounds for the oppponent in the fourth 5 minute window of the 2ND half.
---
--- OT totals are for all OT periods. Hence you will see - H1, H2, and OT.
---
--- Game totals are for the entire game, including OT.
---
--- NOTE: This view only contains D1 vs D1 games.


SELECT
  *,
  # game points
  (h1_points + h2_points + ot_points) as score,
  # game three_att
  (h1_three_att + h2_three_att + ot_three_att) as three_att,
  # game three
  (h1_three + h2_three + ot_three) as three,
  # game two_att
  (h1_two_att + h2_two_att + ot_two_att) as two_att,
  # game two
  (h1_two + h2_two + ot_two) as two,
  # gamee free_att
  (h1_free_att + h2_free_att + ot_free_att) as free_att,
  # gamee free
  (h1_free + h2_free + ot_free) as free,
  # game off_rebounds
  (h1_off_rebounds + h2_off_rebounds + ot_off_rebounds) as off_rebounds,
  # game def_rebounds
  (h1_def_rebounds + h2_def_rebounds + ot_def_rebounds) as def_rebounds,
  # game rebounds
  (h1_rebounds + h2_rebounds + ot_rebounds) as rebounds,
  # game assists
  (h1_assists + h2_assists + ot_assists) as assists,
  # game turnovers
  (h1_turnovers + h2_turnovers + ot_turnovers) as turnovers,
  # game blocks
  (h1_blocks + h2_blocks + ot_blocks) as blocks,
  # game fouls
  (h1_fouls + h2_fouls + ot_fouls) as fouls
FROM(
  SELECT
    *,
    # half points
    (h1_1_points + h1_2_points + h1_3_points + h1_4_points) as h1_points,
    (h2_1_points + h2_2_points + h2_3_points + h2_4_points) as h2_points,
    # half three_att
    (h1_1_three_att + h1_2_three_att + h1_3_three_att + h1_4_three_att) as h1_three_att,
    (h2_1_three_att + h2_2_three_att + h2_3_three_att + h2_4_three_att) as h2_three_att,
    # half three
    (h1_1_three + h1_2_three + h1_3_three + h1_4_three) as h1_three,
    (h2_1_three + h2_2_three + h2_3_three + h2_4_three) as h2_three,
    # half two_att
    (h1_1_two_att + h1_2_two_att + h1_3_two_att + h1_4_two_att) as h1_two_att,
    (h2_1_two_att + h2_2_two_att + h2_3_two_att + h2_4_two_att) as h2_two_att,
    # half two_att
    (h1_1_two + h1_2_two + h1_3_two + h1_4_two) as h1_two,
    (h2_1_two + h2_2_two + h2_3_two + h2_4_two) as h2_two,
    # half free_att
    (h1_1_free_att + h1_2_free_att + h1_3_free_att + h1_4_free_att) as h1_free_att,
    (h2_1_free_att + h2_2_free_att + h2_3_free_att + h2_4_free_att) as h2_free_att,
    # half free
    (h1_1_free + h1_2_free + h1_3_free + h1_4_free) as h1_free,
    (h2_1_free + h2_2_free + h2_3_free + h2_4_free) as h2_free,
    # half off_rebounds
    (h1_1_off_rebounds + h1_2_off_rebounds + h1_3_off_rebounds + h1_4_off_rebounds) as h1_off_rebounds,
    (h2_1_off_rebounds + h2_2_off_rebounds + h2_3_off_rebounds + h2_4_off_rebounds) as h2_off_rebounds,
    # half def_rebounds
    (h1_1_def_rebounds + h1_2_def_rebounds + h1_3_def_rebounds + h1_4_def_rebounds) as h1_def_rebounds,
    (h2_1_def_rebounds + h2_2_def_rebounds + h2_3_def_rebounds + h2_4_def_rebounds) as h2_def_rebounds,
    # half rebounds
    (h1_1_rebounds + h1_2_rebounds + h1_3_rebounds + h1_4_rebounds) as h1_rebounds,
    (h2_1_rebounds + h2_2_rebounds + h2_3_rebounds + h2_4_rebounds) as h2_rebounds,
    # half assists
    (h1_1_assists + h1_2_assists + h1_3_assists + h1_4_assists) as h1_assists,
    (h2_1_assists + h2_2_assists + h2_3_assists + h2_4_assists) as h2_assists,
    # half turnovers
    (h1_1_turnovers + h1_2_turnovers + h1_3_turnovers + h1_4_turnovers) as h1_turnovers,
    (h2_1_turnovers + h2_2_turnovers + h2_3_turnovers + h2_4_turnovers) as h2_turnovers,
    # half blocks
    (h1_1_blocks + h1_2_blocks + h1_3_blocks + h1_4_blocks) as h1_blocks,
    (h2_1_blocks + h2_2_blocks + h2_3_blocks + h2_4_blocks) as h2_blocks,
    # half fouls
    (h1_1_fouls + h1_2_fouls + h1_3_fouls + h1_4_fouls) as h1_fouls,
    (h2_1_fouls + h2_2_fouls + h2_3_fouls + h2_4_fouls) as h2_fouls
  FROM(
    SELECT
      season,
      game_date,
      game_id,
      team_name,
      team_id,
      alignment,
      # map points
      MAX(h1_1_points) as h1_1_points,
      MAX(h1_2_points) as h1_2_points,
      MAX(h1_3_points) as h1_3_points,
      MAX(h1_4_points) as h1_4_points,
      MAX(h2_1_points) as h2_1_points,
      MAX(h2_2_points) as h2_2_points,
      MAX(h2_3_points) as h2_3_points,
      MAX(h2_4_points) as h2_4_points,
      MAX(ot_points) as ot_points,
      # map three_att
      MAX(h1_1_three_att) as h1_1_three_att,
      MAX(h1_2_three_att) as h1_2_three_att,
      MAX(h1_3_three_att) as h1_3_three_att,
      MAX(h1_4_three_att) as h1_4_three_att,
      MAX(h2_1_three_att) as h2_1_three_att,
      MAX(h2_2_three_att) as h2_2_three_att,
      MAX(h2_3_three_att) as h2_3_three_att,
      MAX(h2_4_three_att) as h2_4_three_att,
      MAX(ot_three_att) as ot_three_att,
      # map two
      MAX(h1_1_three) as h1_1_three,
      MAX(h1_2_three) as h1_2_three,
      MAX(h1_3_three) as h1_3_three,
      MAX(h1_4_three) as h1_4_three,
      MAX(h2_1_three) as h2_1_three,
      MAX(h2_2_three) as h2_2_three,
      MAX(h2_3_three) as h2_3_three,
      MAX(h2_4_three) as h2_4_three,
      MAX(ot_three) as ot_three,
      # map two_att
      MAX(h1_1_two_att) as h1_1_two_att,
      MAX(h1_2_two_att) as h1_2_two_att,
      MAX(h1_3_two_att) as h1_3_two_att,
      MAX(h1_4_two_att) as h1_4_two_att,
      MAX(h2_1_two_att) as h2_1_two_att,
      MAX(h2_2_two_att) as h2_2_two_att,
      MAX(h2_3_two_att) as h2_3_two_att,
      MAX(h2_4_two_att) as h2_4_two_att,
      MAX(ot_two_att) as ot_two_att,
       # map two
      MAX(h1_1_two) as h1_1_two,
      MAX(h1_2_two) as h1_2_two,
      MAX(h1_3_two) as h1_3_two,
      MAX(h1_4_two) as h1_4_two,
      MAX(h2_1_two) as h2_1_two,
      MAX(h2_2_two) as h2_2_two,
      MAX(h2_3_two) as h2_3_two,
      MAX(h2_4_two) as h2_4_two,
      MAX(ot_two) as ot_two,
      # map free_att
      MAX(h1_1_free_att) as h1_1_free_att,
      MAX(h1_2_free_att) as h1_2_free_att,
      MAX(h1_3_free_att) as h1_3_free_att,
      MAX(h1_4_free_att) as h1_4_free_att,
      MAX(h2_1_free_att) as h2_1_free_att,
      MAX(h2_2_free_att) as h2_2_free_att,
      MAX(h2_3_free_att) as h2_3_free_att,
      MAX(h2_4_free_att) as h2_4_free_att,
      MAX(ot_free_att) as ot_free_att,
      # map free_att
      MAX(h1_1_free) as h1_1_free,
      MAX(h1_2_free) as h1_2_free,
      MAX(h1_3_free) as h1_3_free,
      MAX(h1_4_free) as h1_4_free,
      MAX(h2_1_free) as h2_1_free,
      MAX(h2_2_free) as h2_2_free,
      MAX(h2_3_free) as h2_3_free,
      MAX(h2_4_free) as h2_4_free,
      MAX(ot_free) as ot_free,
       # map off_rebounds
      MAX(h1_1_off_rebounds) as h1_1_off_rebounds,
      MAX(h1_2_off_rebounds) as h1_2_off_rebounds,
      MAX(h1_3_off_rebounds) as h1_3_off_rebounds,
      MAX(h1_4_off_rebounds) as h1_4_off_rebounds,
      MAX(h2_1_off_rebounds) as h2_1_off_rebounds,
      MAX(h2_2_off_rebounds) as h2_2_off_rebounds,
      MAX(h2_3_off_rebounds) as h2_3_off_rebounds,
      MAX(h2_4_off_rebounds) as h2_4_off_rebounds,
      MAX(ot_off_rebounds) as ot_off_rebounds,
       # map def_rebounds
      MAX(h1_1_def_rebounds) as h1_1_def_rebounds,
      MAX(h1_2_def_rebounds) as h1_2_def_rebounds,
      MAX(h1_3_def_rebounds) as h1_3_def_rebounds,
      MAX(h1_4_def_rebounds) as h1_4_def_rebounds,
      MAX(h2_1_def_rebounds) as h2_1_def_rebounds,
      MAX(h2_2_def_rebounds) as h2_2_def_rebounds,
      MAX(h2_3_def_rebounds) as h2_3_def_rebounds,
      MAX(h2_4_def_rebounds) as h2_4_def_rebounds,
      MAX(ot_def_rebounds) as ot_def_rebounds,
       # map rebounds
      MAX(h1_1_rebounds) as h1_1_rebounds,
      MAX(h1_2_rebounds) as h1_2_rebounds,
      MAX(h1_3_rebounds) as h1_3_rebounds,
      MAX(h1_4_rebounds) as h1_4_rebounds,
      MAX(h2_1_rebounds) as h2_1_rebounds,
      MAX(h2_2_rebounds) as h2_2_rebounds,
      MAX(h2_3_rebounds) as h2_3_rebounds,
      MAX(h2_4_rebounds) as h2_4_rebounds,
      MAX(ot_rebounds) as ot_rebounds,
       # map assists
      MAX(h1_1_assists) as h1_1_assists,
      MAX(h1_2_assists) as h1_2_assists,
      MAX(h1_3_assists) as h1_3_assists,
      MAX(h1_4_assists) as h1_4_assists,
      MAX(h2_1_assists) as h2_1_assists,
      MAX(h2_2_assists) as h2_2_assists,
      MAX(h2_3_assists) as h2_3_assists,
      MAX(h2_4_assists) as h2_4_assists,
      MAX(ot_assists) as ot_assists,
       # map turnovers
      MAX(h1_1_turnovers) as h1_1_turnovers,
      MAX(h1_2_turnovers) as h1_2_turnovers,
      MAX(h1_3_turnovers) as h1_3_turnovers,
      MAX(h1_4_turnovers) as h1_4_turnovers,
      MAX(h2_1_turnovers) as h2_1_turnovers,
      MAX(h2_2_turnovers) as h2_2_turnovers,
      MAX(h2_3_turnovers) as h2_3_turnovers,
      MAX(h2_4_turnovers) as h2_4_turnovers,
      MAX(ot_turnovers) as ot_turnovers,
       # map blocks
      MAX(h1_1_blocks) as h1_1_blocks,
      MAX(h1_2_blocks) as h1_2_blocks,
      MAX(h1_3_blocks) as h1_3_blocks,
      MAX(h1_4_blocks) as h1_4_blocks,
      MAX(h2_1_blocks) as h2_1_blocks,
      MAX(h2_2_blocks) as h2_2_blocks,
      MAX(h2_3_blocks) as h2_3_blocks,
      MAX(h2_4_blocks) as h2_4_blocks,
      MAX(ot_blocks) as ot_blocks,
       # map fouls
      MAX(h1_1_fouls) as h1_1_fouls,
      MAX(h1_2_fouls) as h1_2_fouls,
      MAX(h1_3_fouls) as h1_3_fouls,
      MAX(h1_4_fouls) as h1_4_fouls,
      MAX(h2_1_fouls) as h2_1_fouls,
      MAX(h2_2_fouls) as h2_2_fouls,
      MAX(h2_3_fouls) as h2_3_fouls,
      MAX(h2_4_fouls) as h2_4_fouls,
      MAX(ot_fouls) as ot_fouls
    FROM(
      SELECT
        season,
        game_date,
        game_id,
        team_name,
        team_id,
        alignment,
        # map points
        IF(half = "H1" and half_segment = 1, points, 0) as h1_1_points,
        IF(half = "H1" and half_segment = 2, points, 0) as h1_2_points,
        IF(half = "H1" and half_segment = 3, points, 0) as h1_3_points,
        IF(half = "H1" and half_segment = 4, points, 0) as h1_4_points,
        IF(half = "H2" and half_segment = 1, points, 0) as h2_1_points,
        IF(half = "H2" and half_segment = 2, points, 0) as h2_2_points,
        IF(half = "H2" and half_segment = 3, points, 0) as h2_3_points,
        IF(half = "H2" and half_segment = 4, points, 0) as h2_4_points,
        IF(half = "OT", points, 0) as ot_points,
        # map three_att
        IF(half = "H1" and half_segment = 1, three_att, 0) as h1_1_three_att,
        IF(half = "H1" and half_segment = 2, three_att, 0) as h1_2_three_att,
        IF(half = "H1" and half_segment = 3, three_att, 0) as h1_3_three_att,
        IF(half = "H1" and half_segment = 4, three_att, 0) as h1_4_three_att,
        IF(half = "H2" and half_segment = 1, three_att, 0) as h2_1_three_att,
        IF(half = "H2" and half_segment = 2, three_att, 0) as h2_2_three_att,
        IF(half = "H2" and half_segment = 3, three_att, 0) as h2_3_three_att,
        IF(half = "H2" and half_segment = 4, three_att, 0) as h2_4_three_att,
        IF(half = "OT", three_att, 0) as ot_three_att,
        # map three
        IF(half = "H1" and half_segment = 1, three, 0) as h1_1_three,
        IF(half = "H1" and half_segment = 2, three, 0) as h1_2_three,
        IF(half = "H1" and half_segment = 3, three, 0) as h1_3_three,
        IF(half = "H1" and half_segment = 4, three, 0) as h1_4_three,
        IF(half = "H2" and half_segment = 1, three, 0) as h2_1_three,
        IF(half = "H2" and half_segment = 2, three, 0) as h2_2_three,
        IF(half = "H2" and half_segment = 3, three, 0) as h2_3_three,
        IF(half = "H2" and half_segment = 4, three, 0) as h2_4_three,
        IF(half = "OT", three, 0) as ot_three,
         # map two_att
        IF(half = "H1" and half_segment = 1, two_att, 0) as h1_1_two_att,
        IF(half = "H1" and half_segment = 2, two_att, 0) as h1_2_two_att,
        IF(half = "H1" and half_segment = 3, two_att, 0) as h1_3_two_att,
        IF(half = "H1" and half_segment = 4, two_att, 0) as h1_4_two_att,
        IF(half = "H2" and half_segment = 1, two_att, 0) as h2_1_two_att,
        IF(half = "H2" and half_segment = 2, two_att, 0) as h2_2_two_att,
        IF(half = "H2" and half_segment = 3, two_att, 0) as h2_3_two_att,
        IF(half = "H2" and half_segment = 4, two_att, 0) as h2_4_two_att,
        IF(half = "OT", two_att, 0) as ot_two_att,
         # map two
        IF(half = "H1" and half_segment = 1, two, 0) as h1_1_two,
        IF(half = "H1" and half_segment = 2, two, 0) as h1_2_two,
        IF(half = "H1" and half_segment = 3, two, 0) as h1_3_two,
        IF(half = "H1" and half_segment = 4, two, 0) as h1_4_two,
        IF(half = "H2" and half_segment = 1, two, 0) as h2_1_two,
        IF(half = "H2" and half_segment = 2, two, 0) as h2_2_two,
        IF(half = "H2" and half_segment = 3, two, 0) as h2_3_two,
        IF(half = "H2" and half_segment = 4, two, 0) as h2_4_two,
        IF(half = "OT", two, 0) as ot_two,
         # map free_att
        IF(half = "H1" and half_segment = 1, free_att, 0) as h1_1_free_att,
        IF(half = "H1" and half_segment = 2, free_att, 0) as h1_2_free_att,
        IF(half = "H1" and half_segment = 3, free_att, 0) as h1_3_free_att,
        IF(half = "H1" and half_segment = 4, free_att, 0) as h1_4_free_att,
        IF(half = "H2" and half_segment = 1, free_att, 0) as h2_1_free_att,
        IF(half = "H2" and half_segment = 2, free_att, 0) as h2_2_free_att,
        IF(half = "H2" and half_segment = 3, free_att, 0) as h2_3_free_att,
        IF(half = "H2" and half_segment = 4, free_att, 0) as h2_4_free_att,
        IF(half = "OT", free_att, 0) as ot_free_att,
        # map free
        IF(half = "H1" and half_segment = 1, free, 0) as h1_1_free,
        IF(half = "H1" and half_segment = 2, free, 0) as h1_2_free,
        IF(half = "H1" and half_segment = 3, free, 0) as h1_3_free,
        IF(half = "H1" and half_segment = 4, free, 0) as h1_4_free,
        IF(half = "H2" and half_segment = 1, free, 0) as h2_1_free,
        IF(half = "H2" and half_segment = 2, free, 0) as h2_2_free,
        IF(half = "H2" and half_segment = 3, free, 0) as h2_3_free,
        IF(half = "H2" and half_segment = 4, free, 0) as h2_4_free,
        IF(half = "OT", free, 0) as ot_free,
        # map off rebounds
        IF(half = "H1" and half_segment = 1, off_rebounds, 0) as h1_1_off_rebounds,
        IF(half = "H1" and half_segment = 2, off_rebounds, 0) as h1_2_off_rebounds,
        IF(half = "H1" and half_segment = 3, off_rebounds, 0) as h1_3_off_rebounds,
        IF(half = "H1" and half_segment = 4, off_rebounds, 0) as h1_4_off_rebounds,
        IF(half = "H2" and half_segment = 1, off_rebounds, 0) as h2_1_off_rebounds,
        IF(half = "H2" and half_segment = 2, off_rebounds, 0) as h2_2_off_rebounds,
        IF(half = "H2" and half_segment = 3, off_rebounds, 0) as h2_3_off_rebounds,
        IF(half = "H2" and half_segment = 4, off_rebounds, 0) as h2_4_off_rebounds,
        IF(half = "OT", off_rebounds, 0) as ot_off_rebounds,
        # map def rebounds
        IF(half = "H1" and half_segment = 1, def_rebounds, 0) as h1_1_def_rebounds,
        IF(half = "H1" and half_segment = 2, def_rebounds, 0) as h1_2_def_rebounds,
        IF(half = "H1" and half_segment = 3, def_rebounds, 0) as h1_3_def_rebounds,
        IF(half = "H1" and half_segment = 4, def_rebounds, 0) as h1_4_def_rebounds,
        IF(half = "H2" and half_segment = 1, def_rebounds, 0) as h2_1_def_rebounds,
        IF(half = "H2" and half_segment = 2, def_rebounds, 0) as h2_2_def_rebounds,
        IF(half = "H2" and half_segment = 3, def_rebounds, 0) as h2_3_def_rebounds,
        IF(half = "H2" and half_segment = 4, def_rebounds, 0) as h2_4_def_rebounds,
        IF(half = "OT", def_rebounds, 0) as ot_def_rebounds,
        # map rebounds
        IF(half = "H1" and half_segment = 1, (off_rebounds + def_rebounds), 0) as h1_1_rebounds,
        IF(half = "H1" and half_segment = 2, (off_rebounds + def_rebounds), 0) as h1_2_rebounds,
        IF(half = "H1" and half_segment = 3, (off_rebounds + def_rebounds), 0) as h1_3_rebounds,
        IF(half = "H1" and half_segment = 4, (off_rebounds + def_rebounds), 0) as h1_4_rebounds,
        IF(half = "H2" and half_segment = 1, (off_rebounds + def_rebounds), 0) as h2_1_rebounds,
        IF(half = "H2" and half_segment = 2, (off_rebounds + def_rebounds), 0) as h2_2_rebounds,
        IF(half = "H2" and half_segment = 3, (off_rebounds + def_rebounds), 0) as h2_3_rebounds,
        IF(half = "H2" and half_segment = 4, (off_rebounds + def_rebounds), 0) as h2_4_rebounds,
        IF(half = "OT", (off_rebounds + def_rebounds), 0) as ot_rebounds,
        # map assists
        IF(half = "H1" and half_segment = 1, assists, 0) as h1_1_assists,
        IF(half = "H1" and half_segment = 2, assists, 0) as h1_2_assists,
        IF(half = "H1" and half_segment = 3, assists, 0) as h1_3_assists,
        IF(half = "H1" and half_segment = 4, assists, 0) as h1_4_assists,
        IF(half = "H2" and half_segment = 1, assists, 0) as h2_1_assists,
        IF(half = "H2" and half_segment = 2, assists, 0) as h2_2_assists,
        IF(half = "H2" and half_segment = 3, assists, 0) as h2_3_assists,
        IF(half = "H2" and half_segment = 4, assists, 0) as h2_4_assists,
        IF(half = "OT", assists, 0) as ot_assists,
        # map turnovers
        IF(half = "H1" and half_segment = 1, turnovers, 0) as h1_1_turnovers,
        IF(half = "H1" and half_segment = 2, turnovers, 0) as h1_2_turnovers,
        IF(half = "H1" and half_segment = 3, turnovers, 0) as h1_3_turnovers,
        IF(half = "H1" and half_segment = 4, turnovers, 0) as h1_4_turnovers,
        IF(half = "H2" and half_segment = 1, turnovers, 0) as h2_1_turnovers,
        IF(half = "H2" and half_segment = 2, turnovers, 0) as h2_2_turnovers,
        IF(half = "H2" and half_segment = 3, turnovers, 0) as h2_3_turnovers,
        IF(half = "H2" and half_segment = 4, turnovers, 0) as h2_4_turnovers,
        IF(half = "OT", turnovers, 0) as ot_turnovers,
        # map blocks
        IF(half = "H1" and half_segment = 1, blocks, 0) as h1_1_blocks,
        IF(half = "H1" and half_segment = 2, blocks, 0) as h1_2_blocks,
        IF(half = "H1" and half_segment = 3, blocks, 0) as h1_3_blocks,
        IF(half = "H1" and half_segment = 4, blocks, 0) as h1_4_blocks,
        IF(half = "H2" and half_segment = 1, blocks, 0) as h2_1_blocks,
        IF(half = "H2" and half_segment = 2, blocks, 0) as h2_2_blocks,
        IF(half = "H2" and half_segment = 3, blocks, 0) as h2_3_blocks,
        IF(half = "H2" and half_segment = 4, blocks, 0) as h2_4_blocks,
        IF(half = "OT", blocks, 0) as ot_blocks,
        # map fouls
        IF(half = "H1" and half_segment = 1, fouls, 0) as h1_1_fouls,
        IF(half = "H1" and half_segment = 2, fouls, 0) as h1_2_fouls,
        IF(half = "H1" and half_segment = 3, fouls, 0) as h1_3_fouls,
        IF(half = "H1" and half_segment = 4, fouls, 0) as h1_4_fouls,
        IF(half = "H2" and half_segment = 1, fouls, 0) as h2_1_fouls,
        IF(half = "H2" and half_segment = 2, fouls, 0) as h2_2_fouls,
        IF(half = "H2" and half_segment = 3, fouls, 0) as h2_3_fouls,
        IF(half = "H2" and half_segment = 4, fouls, 0) as h2_4_fouls,
        IF(half = "OT", fouls, 0) as ot_fouls
      FROM(
        SELECT
          season,
          game_date,
          game_id,
          team_name,
          team_id,
          alignment,
          MAX(periods_played) as periods_played,
          half,
          half_segment,
          SUM(points) as points,
          SUM(three_att) as three_att,
          SUM(three) as three,
          SUM(two_att) as two_att,
          SUM(two) as two,
          SUM(free_att) as free_att,
          SUM(free) as free,
          SUM(off_rebounds) as off_rebounds,
          SUM(def_rebounds) as def_rebounds,
          SUM(turnovers) as turnovers,
          SUM(assists) as assists,
          SUM(blocks) as blocks,
          SUM(fouls) as fouls,
          SUM(tech_fouls) as tech_fouls,
          SUM(subs) as subs,
          SUM(timeouts) as timeouts,
          MIN(first_timeout) as first_timeout,
          SUM(fast_break_pts) as fast_break_points
        FROM(
          SELECT
            season,
            game_date,
            game_id,
            team_name,
            team_id,
            alignment,
            MAX(period) as periods_played,
            half,
            half_segment,
            (SUM(three_made)*3) + (SUM(two_made)*2) + SUM(ft_made) as points,
            SUM(three_pa) as three_att,
            SUM(three_made) as three,
            ROUND(IF(SUM(three_pa)>0,SUM(three_made)/SUM(three_pa), 0), 3) as three_pct,
            SUM(two_pa) as two_att,
            SUM(two_made) as two,
            ROUND(IF(SUM(two_pa)>0,SUM(two_made)/SUM(two_pa), 0), 3) as two_pct,
            SUM(ft_attempt) as free_att,
            SUM(ft_made) as free,
            ROUND(IF(SUM(ft_made)>0,SUM(ft_made)/SUM(ft_attempt), 0), 3) as free_pct,
            SUM(three_pa + two_pa) as field_goal_att,
            SUM(three_made + two_made) as field_goal,
            ROUND(IF(SUM(three_made + two_made)>0,SUM(three_made + two_made)/SUM(three_pa + two_pa), 0), 3) as field_goal_pct,
            SUM(off_rebound) as off_rebounds,
            SUM(def_rebound) as def_rebounds,
            SUM(off_rebound) + SUM(def_rebound) as tot_rebounds,
            SUM(turnover) as turnovers,
            SUM(assist) as assists,
            SUM(steal) as steals,
            SUM(block) as blocks,
            SUM(foul) as fouls,
            SUM(tech_foul) as tech_fouls,
            SUM(sub)/2 as subs,
            SUM(timeout) as timeouts,
            MIN(timeout_time) as first_timeout,
            SUM(fast_break_pt) as fast_break_pts,
            ROUND(SUM(three_pa + two_pa) - SUM(off_rebound) + SUM(turnover) + (0.475 * SUM(ft_attempt)), 2) as possessions
          FROM(
            SELECT
             season,
             home_name,
             away_name,
             DATE(DATETIME(TIMESTAMP(scheduled_date))) as game_date,
             game_id,
             team_name,
             team_id,
             period,
             IF(period = 1, "H1", IF(period = 2, "H2", IF(period > 2, "OT", "-"))) as half,
             elapsed_time_sec/60 as minute,
             CAST(CEIL(IF(period = 1, (elapsed_time_sec/60)/5, IF(period = 2, ((elapsed_time_sec/60)-20)/5, 0))) AS INT64) as half_segment,
             IF(team_name = home_name, "HOME", "AWAY") as alignment,
             IF(shot_type = "3PTR", 1, 0) as three_pa,
             IF(shot_type = "3PTR" and event_type = "GOOD", 1, 0) as three_made,
             IF(shot_type = "FT", 1, 0) as ft_attempt,
             IF(shot_type = "FT" AND event_type = "GOOD", 1, 0) as ft_made,
             IF(shot_type IN ("JUMPER", "TIPIN", "LAYUP", "DUNK", "TIPIN"), 1, 0) as two_pa,
             IF(shot_type IN ("JUMPER", "TIPIN", "LAYUP", "DUNK", "TIPIN") AND event_type = "GOOD" , 1, 0) as two_made,
             IF(event_type = "REBOUND" AND rebound_type = "OFF" , 1, 0) as off_rebound,
             IF(event_type = "REBOUND" AND rebound_type = "DEF" , 1, 0) as def_rebound,
             IF(event_type = "TURNOVER", 1, 0) as turnover,
             IF(event_type = "ASSIST", 1, 0) as assist,
             IF(event_type = "STEAL", 1, 0) as steal,
             IF(event_type = "BLOCK", 1, 0) as block,
             IF(event_type = "FOUL", 1, 0) as foul,
             IF(event_type = "FOUL" AND foul_type = "TECH", 1, 0) as tech_foul,
             IF(event_type = "SUB", 1, 0) as sub,
             IF(event_type = "TIMEOUT", 1, 0) as timeout,
             IF(fast_break_pt = "Y", points_scored, 0) as fast_break_pt,
             IF(event_type = "TIMEOUT", elapsed_time_sec, null) as timeout_time
            FROM
             `stardust-development.play_by_play.ncaa_pbp_mbb`
            WHERE
              away_division_alias = "D1"
              AND home_division_alias = "D1"
              AND team_id IS NOT NULL
              --AND scheduled_date != "False"
          )
          GROUP BY
            season,
            game_date,
            game_id,
            team_name,
            team_id,
            alignment,
            half,
            half_segment
        )
        GROUP BY
          season,
          game_date,
          game_id,
          team_name,
          team_id,
          alignment,
          half,
          half_segment
      )
    )
    GROUP BY
      season,
      game_date,
      game_id,
      team_id,
      team_name,
      alignment
  )
)
ORDER BY
  season DESC,
  game_date DESC,
  game_id,
  alignment