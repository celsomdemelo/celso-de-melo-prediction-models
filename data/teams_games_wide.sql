--- teams_games_wide
---
--- This view joins TEAMS_GAMES to NCAA_SPLITS to provide intra-game totals.
---
--- NCAAA_SPLITS provides stat totals by 5 min. windows in each half, as
--  well as the half totals and full game totals.
---
--- For example, opp_splits.h2_4_off_rebounds is the total number of
--- offensive rebounds for the oppponent in the fourth 5 minute window of the 2ND half.
---
--- All NCAA_SPLITS OT totals are for all OT periods. Hence you will see - H1, H2, and OT.
---
--- All NCAA_SPLITS game totals are for the entire game, including OT.
---
--- NOTE: TEAMS_GAMES is missing a significant number of games for 2013; however,
--- most of the these games are picked up in the NCAA_SPLITS. Missing games in TEAMS_GAMES
--- show up with NULL and or -1 values for metric totals.
---
--- NOTE: NCAA_SPLITS does have missing games.  There are games in TEAMS_GAMES that are not
--- in the NCAA_SPLITS. These show up as null.
---
--- NOTE: NCAA_SPLITS only contains D1 games.
---

WITH games AS (
   SELECT
      *,
      id as game_id,
      DATE(DATETIME(`timestamp`, "America/Los_Angeles")) as game_date,
      # 3 POINT ATT
      ROUND(AVG(three_points_att) over (partition by season, team_id order by `timestamp`), 2) as three_points_att_avg_season,
      ROUND(AVG(three_points_att) over (partition by season, team_id order by `timestamp` ROWS BETWEEN 7 PRECEDING AND 1 PRECEDING), 2) as three_points_att_avg_last7,
      ROUND(AVG(three_points_att) over (partition by season, team_id order by `timestamp` ROWS BETWEEN 3 PRECEDING AND 1 PRECEDING), 2) as three_points_att_avg_last3,
      MAX(three_points_att) over (partition by season, team_id order by `timestamp` ROWS BETWEEN 1 PRECEDING AND 1 PRECEDING) as three_points_att_last,
       # 3 POINT MADE
      ROUND(AVG(three_points_made) over (partition by season, team_id order by `timestamp`), 2) as three_points_made_avg_season,
      ROUND(AVG(three_points_made) over (partition by season, team_id order by `timestamp` ROWS BETWEEN 7 PRECEDING AND 1 PRECEDING), 2) as three_points_made_avg_last7,
      ROUND(AVG(three_points_made) over (partition by season, team_id order by `timestamp` ROWS BETWEEN 3 PRECEDING AND 1 PRECEDING), 2) as three_points_made_avg_last3,
      MAX(three_points_made) over (partition by season, team_id order by `timestamp` ROWS BETWEEN 1 PRECEDING AND 1 PRECEDING) as three_points_made_last
  FROM
    `stardust-development.stardust.teams_games_v9`
   WHERE
    division_name = "NCAA Division I"
    AND opp_division_name = "NCAA Division I"
), splits AS (
  SELECT
    *
  FROM
    `stardust-development.temp.teams_games_v10`
), opp_splits AS (
  SELECT
    *
  FROM
    `stardust-development.temp.teams_games_v10`
)
SELECT
  games,
  splits,
  opp_splits
FROM
  games
LEFT JOIN
  splits
ON
  games.season = splits.season
  AND games.game_date = splits.game_date
  AND games.team_id = splits.team_id
LEFT JOIN
  opp_splits
ON
  games.season = opp_splits.season
  AND games.game_date = opp_splits.game_date
  AND games.opp_id = opp_splits.team_id
ORDER BY
  games.season DESC