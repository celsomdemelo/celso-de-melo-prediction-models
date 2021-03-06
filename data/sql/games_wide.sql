SELECT
    games.game_id AS id,
    games.season AS season,
--    games.status AS status,
--    games.coverage AS coverage,
--    games.neutral_site AS neutral_site,
    games.scheduled_date AS scheduled_date,
    games.conference_game AS conference_game,
    games.tournament AS tournament,
    games.attendance AS attendance,
    games.lead_changes AS lead_changes,
    games.times_tied AS times_tied,
    games.possession_arrow AS possession_arrow,
    games.venue_id AS venue_id,
    games.venue_city AS venue_city,
    games.venue_state AS venue_state,
--    games.venue_address AS venue_address
    games.venue_zip AS venue_zip,
    games.venue_country AS venue_country,
    games.venue_name AS venue_name,
    games.venue_capacity AS venue_capacity,
    games.name AS h_name,
    games.market AS h_market,
    games.team_id AS h_id,
    games.alias AS h_alias,
    games.league_id AS h_league_id,
    games.league_name AS h_league_name,
    games.league_alias AS h_league_alias,
    games.conf_id AS h_conf_id,
    games.conf_name AS h_conf_name,
    games.conf_alias AS h_conf_alias,
    games.division_id AS h_division_id,
    games.division_name AS h_division_name,
    games.division_alias AS h_division_alias,
    games.logo_large AS h_logo_large,
    games.logo_medium AS h_logo_medium,
    games.logo_small AS h_logo_small,
    games.opp_name AS a_name,
    games.opp_market AS a_market,
    games.opp_id AS a_id,
    games.opp_alias AS a_alias,
    games.opp_league_id AS a_league_id,
    games.opp_league_name AS a_league_name,
    games.opp_league_alias AS a_league_alias,
    games.opp_conf_id AS a_conf_id,
    games.opp_conf_name AS a_conf_name,
    games.opp_conf_alias AS a_conf_alias,
    games.opp_division_id AS a_division_id,
    games.opp_division_name AS a_division_name,
    games.opp_division_alias AS a_division_alias,
    games.opp_logo_large AS a_logo_large,
    games.opp_logo_medium AS a_logo_medium,
    games.opp_logo_small AS a_logo_small,
--    games.points_game AS h_points_game,
--    games.minutes AS h_minutes,
--    games.field_goals_made AS h_field_goals_made,
--    games.field_goals_att AS h_field_goals_att,
--    games.field_goals_pct AS h_field_goals_pct,
--    games.three_points_made AS h_three_points_made,
--    games.three_points_att AS h_three_points_att,
--    games.three_points_pct AS h_three_points_pct,
--    games.two_points_made AS h_two_points_made,
--    games.two_points_att AS h_two_points_att,
--    games.two_points_pct AS h_two_points_pct,
--    games.blocked_att AS h_blocked_att,
--    games.free_throws_made AS h_free_throws_made,
--    games.free_throws_att AS h_free_throws_att,
--    games.free_throws_pct AS h_free_throws_pct,
--    games.offensive_rebounds AS h_offensive_rebounds,
--    games.defensive_rebounds AS h_defensive_rebounds,
--    games.rebounds AS h_rebounds,
--    games.assists AS h_assists,
--    games.turnovers AS h_turnovers,
--    games.blocks AS h_blocks,
--    games.assists_turnover_ratio AS h_assists_turnover_ratio,
--    games.personal_fouls AS h_personal_fouls,
--    games.ejections AS h_ejections,
--    games.foulouts AS h_foulouts,
--    games.points AS h_points,
--    games.fast_break_pts AS h_fast_break_pts,
--    games.second_chance_pts AS h_second_chance_pts,
--    games.team_turnovers AS h_team_turnovers,
--    games.points_off_turnovers AS h_points_off_turnovers,
--    games.team_rebounds AS h_team_rebounds,
--    games.flagrant_fouls AS h_flagrant_fouls,
--    games.player_tech_fouls AS h_player_tech_fouls,
--    games.team_tech_fouls AS h_team_tech_fouls,
--    games.coach_tech_fouls AS h_coach_tech_fouls,
--    games.opp_points_game AS a_points_game,
--    games.opp_minutes AS a_minutes,
--    games.opp_field_goals_made AS a_field_goals_made,
--    games.opp_field_goals_att AS a_field_goals_att,
--    games.opp_field_goals_pct AS a_field_goals_pct,
--    games.opp_three_points_made AS a_three_points_made,
--    games.opp_three_points_att AS a_three_points_att,
--    games.opp_three_points_pct AS a_three_points_pct,
--    games.opp_two_points_made AS a_two_points_made,
--    games.opp_two_points_att AS a_two_points_att,
--    games.opp_two_points_pct AS a_two_points_pct,
--    games.opp_blocked_att AS a_blocked_att,
--    games.opp_free_throws_made AS a_free_throws_made,
--    games.opp_free_throws_att AS a_free_throws_att,
--    games.opp_free_throws_pct AS a_free_throws_pct,
--    games.opp_offensive_rebounds AS a_offensive_rebounds,
--    games.opp_defensive_rebounds AS a_defensive_rebounds,
--    games.opp_rebounds AS a_rebounds,
--    games.opp_assists AS a_assists,
--    games.opp_turnovers AS a_turnovers,
--    games.opp_blocks AS a_blocks,
--    games.opp_assists_turnover_ratio AS a_assists_turnover_ratio,
--    games.opp_personal_fouls AS a_personal_fouls,
--    games.opp_ejections AS a_ejections,
--    games.opp_foulouts AS a_foulouts,
--    games.opp_points AS a_points,
--    games.opp_fast_break_pts AS a_fast_break_pts,
--    games.opp_second_chance_pts AS a_second_chance_pts,
--    games.opp_team_turnovers AS a_team_turnovers,
--    games.opp_points_off_turnovers AS a_points_off_turnovers,
--    games.opp_team_rebounds AS a_team_rebounds,
--    games.opp_flagrant_fouls AS a_flagrant_fouls,
--    games.opp_player_tech_fouls AS a_player_tech_fouls,
--    games.opp_team_tech_fouls AS a_team_tech_fouls,
--    games.opp_coach_tech_fouls AS a_coach_tech_fouls,

    -- SPLITS

    IFNULL(splits.h1_1_points, -1) AS h_h1_1_points,
    IFNULL(splits.h1_2_points, -1) AS h_h1_2_points,
    IFNULL(splits.h1_3_points, -1) AS h_h1_3_points,
    IFNULL(splits.h1_4_points, -1) AS h_h1_4_points,
    (CASE WHEN splits.h1_1_points IS NULL OR splits.h1_2_points IS NULL OR splits.h1_3_points IS NULL OR splits.h1_4_points IS NULL
        THEN -1 ELSE (splits.h1_1_points + splits.h1_2_points + splits.h1_3_points + splits.h1_4_points) END) AS h_h1_points,
    IFNULL(splits.h2_1_points, -1) AS h_h2_1_points,
    IFNULL(splits.h2_2_points, -1) AS h_h2_2_points,
    IFNULL(splits.h2_3_points, -1) AS h_h2_3_points,
    IFNULL(splits.h2_4_points, -1) AS h_h2_4_points,
    (CASE WHEN splits.h2_1_points IS NULL OR splits.h2_2_points IS NULL OR splits.h2_3_points IS NULL OR splits.h2_4_points IS NULL
        THEN -1 ELSE (splits.h2_1_points + splits.h2_2_points + splits.h2_3_points + splits.h2_4_points) END) AS h_h2_points,
    IFNULL(splits.ot_points, -1) AS h_ot_points,

    IFNULL(splits.h1_1_three_att, -1) AS h_h1_1_three_att,
    IFNULL(splits.h1_2_three_att, -1) AS h_h1_2_three_att,
    IFNULL(splits.h1_3_three_att, -1) AS h_h1_3_three_att,
    IFNULL(splits.h1_4_three_att, -1) AS h_h1_4_three_att,
    (CASE WHEN splits.h1_1_three_att IS NULL OR splits.h1_2_three_att IS NULL OR splits.h1_3_three_att IS NULL OR splits.h1_4_three_att IS NULL
        THEN -1 ELSE (splits.h1_1_three_att + splits.h1_2_three_att + splits.h1_3_three_att + splits.h1_4_three_att) END) AS h_h1_three_att,
    IFNULL(splits.h2_1_three_att, -1) AS h_h2_1_three_att,
    IFNULL(splits.h2_2_three_att, -1) AS h_h2_2_three_att,
    IFNULL(splits.h2_3_three_att, -1) AS h_h2_3_three_att,
    IFNULL(splits.h2_4_three_att, -1) AS h_h2_4_three_att,
    (CASE WHEN splits.h2_1_three_att IS NULL OR splits.h2_2_three_att IS NULL OR splits.h2_3_three_att IS NULL OR splits.h2_4_three_att IS NULL
        THEN -1 ELSE (splits.h2_1_three_att + splits.h2_2_three_att + splits.h2_3_three_att + splits.h2_4_three_att) END) AS h_h2_three_att,
    IFNULL(splits.ot_three_att, -1) AS h_ot_three_att,

    IFNULL(splits.h1_1_three, -1) AS h_h1_1_three,
    IFNULL(splits.h1_2_three, -1) AS h_h1_2_three,
    IFNULL(splits.h1_3_three, -1) AS h_h1_3_three,
    IFNULL(splits.h1_4_three, -1) AS h_h1_4_three,
    (CASE WHEN splits.h1_1_three IS NULL OR splits.h1_2_three IS NULL OR splits.h1_3_three IS NULL OR splits.h1_4_three IS NULL
        THEN -1 ELSE (splits.h1_1_three + splits.h1_2_three + splits.h1_3_three + splits.h1_4_three) END) AS h_h1_three,
    IFNULL(splits.h2_1_three, -1) AS h_h2_1_three,
    IFNULL(splits.h2_2_three, -1) AS h_h2_2_three,
    IFNULL(splits.h2_3_three, -1) AS h_h2_3_three,
    IFNULL(splits.h2_4_three, -1) AS h_h2_4_three,
    (CASE WHEN splits.h2_1_three IS NULL OR splits.h2_2_three IS NULL OR splits.h2_3_three IS NULL OR splits.h2_4_three IS NULL
        THEN -1 ELSE (splits.h2_1_three + splits.h2_2_three + splits.h2_3_three + splits.h2_4_three) END) AS h_h2_three,
    IFNULL(splits.ot_three, -1) AS h_ot_three,

    IFNULL(splits.h1_1_two_att, -1) AS h_h1_1_two_att,
    IFNULL(splits.h1_2_two_att, -1) AS h_h1_2_two_att,
    IFNULL(splits.h1_3_two_att, -1) AS h_h1_3_two_att,
    IFNULL(splits.h1_4_two_att, -1) AS h_h1_4_two_att,
    (CASE WHEN splits.h1_1_two_att IS NULL OR splits.h1_2_two_att IS NULL OR splits.h1_3_two_att IS NULL OR splits.h1_4_two_att IS NULL
        THEN -1 ELSE (splits.h1_1_two_att + splits.h1_2_two_att + splits.h1_3_two_att + splits.h1_4_two_att) END) AS h_h1_two_att,
    IFNULL(splits.h2_1_two_att, -1) AS h_h2_1_two_att,
    IFNULL(splits.h2_2_two_att, -1) AS h_h2_2_two_att,
    IFNULL(splits.h2_3_two_att, -1) AS h_h2_3_two_att,
    IFNULL(splits.h2_4_two_att, -1) AS h_h2_4_two_att,
    (CASE WHEN splits.h2_1_two_att IS NULL OR splits.h2_2_two_att IS NULL OR splits.h2_3_two_att IS NULL OR splits.h2_4_two_att IS NULL
        THEN -1 ELSE (splits.h2_1_two_att + splits.h2_2_two_att + splits.h2_3_two_att + splits.h2_4_two_att) END) AS h_h2_two_att,
    IFNULL(splits.ot_two_att, -1) AS h_ot_two_att,

    IFNULL(splits.h1_1_two, -1) AS h_h1_1_two,
    IFNULL(splits.h1_2_two, -1) AS h_h1_2_two,
    IFNULL(splits.h1_3_two, -1) AS h_h1_3_two,
    IFNULL(splits.h1_4_two, -1) AS h_h1_4_two,
    (CASE WHEN splits.h1_1_two IS NULL OR splits.h1_2_two IS NULL OR splits.h1_3_two IS NULL OR splits.h1_4_two IS NULL
        THEN -1 ELSE (splits.h1_1_two + splits.h1_2_two + splits.h1_3_two + splits.h1_4_two) END) AS h_h1_two,
    IFNULL(splits.h2_1_two, -1) AS h_h2_1_two,
    IFNULL(splits.h2_2_two, -1) AS h_h2_2_two,
    IFNULL(splits.h2_3_two, -1) AS h_h2_3_two,
    IFNULL(splits.h2_4_two, -1) AS h_h2_4_two,
    (CASE WHEN splits.h2_1_two IS NULL OR splits.h2_2_two IS NULL OR splits.h2_3_two IS NULL OR splits.h2_4_two IS NULL
        THEN -1 ELSE (splits.h2_1_two + splits.h2_2_two + splits.h2_3_two + splits.h2_4_two) END) AS h_h2_two,
    IFNULL(splits.ot_two, -1) AS h_ot_two,

    IFNULL(splits.h1_1_free_att, -1) AS h_h1_1_free_att,
    IFNULL(splits.h1_2_free_att, -1) AS h_h1_2_free_att,
    IFNULL(splits.h1_3_free_att, -1) AS h_h1_3_free_att,
    IFNULL(splits.h1_4_free_att, -1) AS h_h1_4_free_att,
    (CASE WHEN splits.h1_1_free_att IS NULL OR splits.h1_2_free_att IS NULL OR splits.h1_3_free_att IS NULL OR splits.h1_4_free_att IS NULL
        THEN -1 ELSE (splits.h1_1_free_att + splits.h1_2_free_att + splits.h1_3_free_att + splits.h1_4_free_att) END) AS h_h1_free_att,
    IFNULL(splits.h2_1_free_att, -1) AS h_h2_1_free_att,
    IFNULL(splits.h2_2_free_att, -1) AS h_h2_2_free_att,
    IFNULL(splits.h2_3_free_att, -1) AS h_h2_3_free_att,
    IFNULL(splits.h2_4_free_att, -1) AS h_h2_4_free_att,
    (CASE WHEN splits.h2_1_free_att IS NULL OR splits.h2_2_free_att IS NULL OR splits.h2_3_free_att IS NULL OR splits.h2_4_free_att IS NULL
        THEN -1 ELSE (splits.h2_1_free_att + splits.h2_2_free_att + splits.h2_3_free_att + splits.h2_4_free_att) END) AS h_h2_free_att,
    IFNULL(splits.ot_free_att, -1) AS h_ot_free_att,

    IFNULL(splits.h1_1_free, -1) AS h_h1_1_free,
    IFNULL(splits.h1_2_free, -1) AS h_h1_2_free,
    IFNULL(splits.h1_3_free, -1) AS h_h1_3_free,
    IFNULL(splits.h1_4_free, -1) AS h_h1_4_free,
    (CASE WHEN splits.h1_1_free IS NULL OR splits.h1_2_free IS NULL OR splits.h1_3_free IS NULL OR splits.h1_4_free IS NULL
        THEN -1 ELSE (splits.h1_1_free + splits.h1_2_free + splits.h1_3_free + splits.h1_4_free) END) AS h_h1_free,
    IFNULL(splits.h2_1_free, -1) AS h_h2_1_free,
    IFNULL(splits.h2_2_free, -1) AS h_h2_2_free,
    IFNULL(splits.h2_3_free, -1) AS h_h2_3_free,
    IFNULL(splits.h2_4_free, -1) AS h_h2_4_free,
    (CASE WHEN splits.h2_1_free IS NULL OR splits.h2_2_free IS NULL OR splits.h2_3_free IS NULL OR splits.h2_4_free IS NULL
        THEN -1 ELSE (splits.h2_1_free + splits.h2_2_free + splits.h2_3_free + splits.h2_4_free) END) AS h_h2_free,
    IFNULL(splits.ot_free, -1) AS h_ot_free,

    IFNULL(splits.h1_1_off_rebounds, -1) AS h_h1_1_off_rebounds,
    IFNULL(splits.h1_2_off_rebounds, -1) AS h_h1_2_off_rebounds,
    IFNULL(splits.h1_3_off_rebounds, -1) AS h_h1_3_off_rebounds,
    IFNULL(splits.h1_4_off_rebounds, -1) AS h_h1_4_off_rebounds,
    (CASE WHEN splits.h1_1_off_rebounds IS NULL OR splits.h1_2_off_rebounds IS NULL OR splits.h1_3_off_rebounds IS NULL OR splits.h1_4_off_rebounds IS NULL
        THEN -1 ELSE (splits.h1_1_off_rebounds + splits.h1_2_off_rebounds + splits.h1_3_off_rebounds + splits.h1_4_off_rebounds) END) AS h_h1_off_rebounds,
    IFNULL(splits.h2_1_off_rebounds, -1) AS h_h2_1_off_rebounds,
    IFNULL(splits.h2_2_off_rebounds, -1) AS h_h2_2_off_rebounds,
    IFNULL(splits.h2_3_off_rebounds, -1) AS h_h2_3_off_rebounds,
    IFNULL(splits.h2_4_off_rebounds, -1) AS h_h2_4_off_rebounds,
    (CASE WHEN splits.h2_1_off_rebounds IS NULL OR splits.h2_2_off_rebounds IS NULL OR splits.h2_3_off_rebounds IS NULL OR splits.h2_4_off_rebounds IS NULL
        THEN -1 ELSE (splits.h2_1_off_rebounds + splits.h2_2_off_rebounds + splits.h2_3_off_rebounds + splits.h2_4_off_rebounds) END) AS h_h2_off_rebounds,
    IFNULL(splits.ot_off_rebounds, -1) AS h_ot_off_rebounds,

    IFNULL(splits.h1_1_def_rebounds, -1) AS h_h1_1_def_rebounds,
    IFNULL(splits.h1_2_def_rebounds, -1) AS h_h1_2_def_rebounds,
    IFNULL(splits.h1_3_def_rebounds, -1) AS h_h1_3_def_rebounds,
    IFNULL(splits.h1_4_def_rebounds, -1) AS h_h1_4_def_rebounds,
    (CASE WHEN splits.h1_1_def_rebounds IS NULL OR splits.h1_2_def_rebounds IS NULL OR splits.h1_3_def_rebounds IS NULL OR splits.h1_4_def_rebounds IS NULL
        THEN -1 ELSE (splits.h1_1_def_rebounds + splits.h1_2_def_rebounds + splits.h1_3_def_rebounds + splits.h1_4_def_rebounds) END) AS h_h1_def_rebounds,
    IFNULL(splits.h2_1_def_rebounds, -1) AS h_h2_1_def_rebounds,
    IFNULL(splits.h2_2_def_rebounds, -1) AS h_h2_2_def_rebounds,
    IFNULL(splits.h2_3_def_rebounds, -1) AS h_h2_3_def_rebounds,
    IFNULL(splits.h2_4_def_rebounds, -1) AS h_h2_4_def_rebounds,
    (CASE WHEN splits.h2_1_def_rebounds IS NULL OR splits.h2_2_def_rebounds IS NULL OR splits.h2_3_def_rebounds IS NULL OR splits.h2_4_def_rebounds IS NULL
        THEN -1 ELSE (splits.h2_1_def_rebounds + splits.h2_2_def_rebounds + splits.h2_3_def_rebounds + splits.h2_4_def_rebounds) END) AS h_h2_def_rebounds,
    IFNULL(splits.ot_def_rebounds, -1) AS h_ot_def_rebounds,

    IFNULL(splits.h1_1_rebounds, -1) AS h_h1_1_rebounds,
    IFNULL(splits.h1_2_rebounds, -1) AS h_h1_2_rebounds,
    IFNULL(splits.h1_3_rebounds, -1) AS h_h1_3_rebounds,
    IFNULL(splits.h1_4_rebounds, -1) AS h_h1_4_rebounds,
    (CASE WHEN splits.h1_1_rebounds IS NULL OR splits.h1_2_rebounds IS NULL OR splits.h1_3_rebounds IS NULL OR splits.h1_4_rebounds IS NULL
        THEN -1 ELSE (splits.h1_1_rebounds + splits.h1_2_rebounds + splits.h1_3_rebounds + splits.h1_4_rebounds) END) AS h_h1_rebounds,
    IFNULL(splits.h2_1_rebounds, -1) AS h_h2_1_rebounds,
    IFNULL(splits.h2_2_rebounds, -1) AS h_h2_2_rebounds,
    IFNULL(splits.h2_3_rebounds, -1) AS h_h2_3_rebounds,
    IFNULL(splits.h2_4_rebounds, -1) AS h_h2_4_rebounds,
    (CASE WHEN splits.h2_1_rebounds IS NULL OR splits.h2_2_rebounds IS NULL OR splits.h2_3_rebounds IS NULL OR splits.h2_4_rebounds IS NULL
        THEN -1 ELSE (splits.h2_1_rebounds + splits.h2_2_rebounds + splits.h2_3_rebounds + splits.h2_4_rebounds) END) AS h_h2_rebounds,
    IFNULL(splits.ot_rebounds, -1) AS h_ot_rebounds,

    IFNULL(splits.h1_1_assists, -1) AS h_h1_1_assists,
    IFNULL(splits.h1_2_assists, -1) AS h_h1_2_assists,
    IFNULL(splits.h1_3_assists, -1) AS h_h1_3_assists,
    IFNULL(splits.h1_4_assists, -1) AS h_h1_4_assists,
    (CASE WHEN splits.h1_1_assists IS NULL OR splits.h1_2_assists IS NULL OR splits.h1_3_assists IS NULL OR splits.h1_4_assists IS NULL
        THEN -1 ELSE (splits.h1_1_assists + splits.h1_2_assists + splits.h1_3_assists + splits.h1_4_assists) END) AS h_h1_assists,
    IFNULL(splits.h2_1_assists, -1) AS h_h2_1_assists,
    IFNULL(splits.h2_2_assists, -1) AS h_h2_2_assists,
    IFNULL(splits.h2_3_assists, -1) AS h_h2_3_assists,
    IFNULL(splits.h2_4_assists, -1) AS h_h2_4_assists,
    (CASE WHEN splits.h2_1_assists IS NULL OR splits.h2_2_assists IS NULL OR splits.h2_3_assists IS NULL OR splits.h2_4_assists IS NULL
        THEN -1 ELSE (splits.h2_1_assists + splits.h2_2_assists + splits.h2_3_assists + splits.h2_4_assists) END) AS h_h2_assists,
    IFNULL(splits.ot_assists, -1) AS h_ot_assists,

    IFNULL(splits.h1_1_turnovers, -1) AS h_h1_1_turnovers,
    IFNULL(splits.h1_2_turnovers, -1) AS h_h1_2_turnovers,
    IFNULL(splits.h1_3_turnovers, -1) AS h_h1_3_turnovers,
    IFNULL(splits.h1_4_turnovers, -1) AS h_h1_4_turnovers,
    (CASE WHEN splits.h1_1_turnovers IS NULL OR splits.h1_2_turnovers IS NULL OR splits.h1_3_turnovers IS NULL OR splits.h1_4_turnovers IS NULL
        THEN -1 ELSE (splits.h1_1_turnovers + splits.h1_2_turnovers + splits.h1_3_turnovers + splits.h1_4_turnovers) END) AS h_h1_turnovers,
    IFNULL(splits.h2_1_turnovers, -1) AS h_h2_1_turnovers,
    IFNULL(splits.h2_2_turnovers, -1) AS h_h2_2_turnovers,
    IFNULL(splits.h2_3_turnovers, -1) AS h_h2_3_turnovers,
    IFNULL(splits.h2_4_turnovers, -1) AS h_h2_4_turnovers,
    (CASE WHEN splits.h2_1_turnovers IS NULL OR splits.h2_2_turnovers IS NULL OR splits.h2_3_turnovers IS NULL OR splits.h2_4_turnovers IS NULL
        THEN -1 ELSE (splits.h2_1_turnovers + splits.h2_2_turnovers + splits.h2_3_turnovers + splits.h2_4_turnovers) END) AS h_h2_turnovers,
    IFNULL(splits.ot_turnovers, -1) AS h_ot_turnovers,

    IFNULL(splits.h1_1_blocks, -1) AS h_h1_1_blocks,
    IFNULL(splits.h1_2_blocks, -1) AS h_h1_2_blocks,
    IFNULL(splits.h1_3_blocks, -1) AS h_h1_3_blocks,
    IFNULL(splits.h1_4_blocks, -1) AS h_h1_4_blocks,
    (CASE WHEN splits.h1_1_blocks IS NULL OR splits.h1_2_blocks IS NULL OR splits.h1_3_blocks IS NULL OR splits.h1_4_blocks IS NULL
        THEN -1 ELSE (splits.h1_1_blocks + splits.h1_2_blocks + splits.h1_3_blocks + splits.h1_4_blocks) END) AS h_h1_blocks,
    IFNULL(splits.h2_1_blocks, -1) AS h_h2_1_blocks,
    IFNULL(splits.h2_2_blocks, -1) AS h_h2_2_blocks,
    IFNULL(splits.h2_3_blocks, -1) AS h_h2_3_blocks,
    IFNULL(splits.h2_4_blocks, -1) AS h_h2_4_blocks,
    (CASE WHEN splits.h2_1_blocks IS NULL OR splits.h2_2_blocks IS NULL OR splits.h2_3_blocks IS NULL OR splits.h2_4_blocks IS NULL
        THEN -1 ELSE (splits.h2_1_blocks + splits.h2_2_blocks + splits.h2_3_blocks + splits.h2_4_blocks) END) AS h_h2_blocks,
    IFNULL(splits.ot_blocks, -1) AS h_ot_blocks,

    IFNULL(splits.h1_1_fouls, -1) AS h_h1_1_fouls,
    IFNULL(splits.h1_2_fouls, -1) AS h_h1_2_fouls,
    IFNULL(splits.h1_3_fouls, -1) AS h_h1_3_fouls,
    IFNULL(splits.h1_4_fouls, -1) AS h_h1_4_fouls,
    (CASE WHEN splits.h1_1_fouls IS NULL OR splits.h1_2_fouls IS NULL OR splits.h1_3_fouls IS NULL OR splits.h1_4_fouls IS NULL
        THEN -1 ELSE (splits.h1_1_fouls + splits.h1_2_fouls + splits.h1_3_fouls + splits.h1_4_fouls) END) AS h_h1_fouls,
    IFNULL(splits.h2_1_fouls, -1) AS h_h2_1_fouls,
    IFNULL(splits.h2_2_fouls, -1) AS h_h2_2_fouls,
    IFNULL(splits.h2_3_fouls, -1) AS h_h2_3_fouls,
    IFNULL(splits.h2_4_fouls, -1) AS h_h2_4_fouls,
    (CASE WHEN splits.h2_1_fouls IS NULL OR splits.h2_2_fouls IS NULL OR splits.h2_3_fouls IS NULL OR splits.h2_4_fouls IS NULL
        THEN -1 ELSE (splits.h2_1_fouls + splits.h2_2_fouls + splits.h2_3_fouls + splits.h2_4_fouls) END) AS h_h2_fouls,
    IFNULL(splits.ot_fouls, -1) AS h_ot_fouls,


    IFNULL(opp_splits.h1_1_points, -1) AS a_h1_1_points,
    IFNULL(opp_splits.h1_2_points, -1) AS a_h1_2_points,
    IFNULL(opp_splits.h1_3_points, -1) AS a_h1_3_points,
    IFNULL(opp_splits.h1_4_points, -1) AS a_h1_4_points,
    (CASE WHEN opp_splits.h1_1_points IS NULL OR opp_splits.h1_2_points IS NULL OR opp_splits.h1_3_points IS NULL OR opp_splits.h1_4_points IS NULL
        THEN -1 ELSE (opp_splits.h1_1_points + opp_splits.h1_2_points + opp_splits.h1_3_points + opp_splits.h1_4_points) END) AS a_h1_points,
    IFNULL(opp_splits.h2_1_points, -1) AS a_h2_1_points,
    IFNULL(opp_splits.h2_2_points, -1) AS a_h2_2_points,
    IFNULL(opp_splits.h2_3_points, -1) AS a_h2_3_points,
    IFNULL(opp_splits.h2_4_points, -1) AS a_h2_4_points,
    (CASE WHEN opp_splits.h2_1_points IS NULL OR opp_splits.h2_2_points IS NULL OR opp_splits.h2_3_points IS NULL OR opp_splits.h2_4_points IS NULL
        THEN -1 ELSE (opp_splits.h2_1_points + opp_splits.h2_2_points + opp_splits.h2_3_points + opp_splits.h2_4_points) END) AS a_h2_points,
    IFNULL(opp_splits.ot_points, -1) AS a_ot_points,

    IFNULL(opp_splits.h1_1_three_att, -1) AS a_h1_1_three_att,
    IFNULL(opp_splits.h1_2_three_att, -1) AS a_h1_2_three_att,
    IFNULL(opp_splits.h1_3_three_att, -1) AS a_h1_3_three_att,
    IFNULL(opp_splits.h1_4_three_att, -1) AS a_h1_4_three_att,
    (CASE WHEN opp_splits.h1_1_three_att IS NULL OR opp_splits.h1_2_three_att IS NULL OR opp_splits.h1_3_three_att IS NULL OR opp_splits.h1_4_three_att IS NULL
        THEN -1 ELSE (opp_splits.h1_1_three_att + opp_splits.h1_2_three_att + opp_splits.h1_3_three_att + opp_splits.h1_4_three_att) END) AS a_h1_three_att,
    IFNULL(opp_splits.h2_1_three_att, -1) AS a_h2_1_three_att,
    IFNULL(opp_splits.h2_2_three_att, -1) AS a_h2_2_three_att,
    IFNULL(opp_splits.h2_3_three_att, -1) AS a_h2_3_three_att,
    IFNULL(opp_splits.h2_4_three_att, -1) AS a_h2_4_three_att,
    (CASE WHEN opp_splits.h2_1_three_att IS NULL OR opp_splits.h2_2_three_att IS NULL OR opp_splits.h2_3_three_att IS NULL OR opp_splits.h2_4_three_att IS NULL
        THEN -1 ELSE (opp_splits.h2_1_three_att + opp_splits.h2_2_three_att + opp_splits.h2_3_three_att + opp_splits.h2_4_three_att) END) AS a_h2_three_att,
    IFNULL(opp_splits.ot_three_att, -1) AS a_ot_three_att,

    IFNULL(opp_splits.h1_1_three, -1) AS a_h1_1_three,
    IFNULL(opp_splits.h1_2_three, -1) AS a_h1_2_three,
    IFNULL(opp_splits.h1_3_three, -1) AS a_h1_3_three,
    IFNULL(opp_splits.h1_4_three, -1) AS a_h1_4_three,
    (CASE WHEN opp_splits.h1_1_three IS NULL OR opp_splits.h1_2_three IS NULL OR opp_splits.h1_3_three IS NULL OR opp_splits.h1_4_three IS NULL
        THEN -1 ELSE (opp_splits.h1_1_three + opp_splits.h1_2_three + opp_splits.h1_3_three + opp_splits.h1_4_three) END) AS a_h1_three,
    IFNULL(opp_splits.h2_1_three, -1) AS a_h2_1_three,
    IFNULL(opp_splits.h2_2_three, -1) AS a_h2_2_three,
    IFNULL(opp_splits.h2_3_three, -1) AS a_h2_3_three,
    IFNULL(opp_splits.h2_4_three, -1) AS a_h2_4_three,
    (CASE WHEN opp_splits.h2_1_three IS NULL OR opp_splits.h2_2_three IS NULL OR opp_splits.h2_3_three IS NULL OR opp_splits.h2_4_three IS NULL
        THEN -1 ELSE (opp_splits.h2_1_three + opp_splits.h2_2_three + opp_splits.h2_3_three + opp_splits.h2_4_three) END) AS a_h2_three,
    IFNULL(opp_splits.ot_three, -1) AS a_ot_three,

    IFNULL(opp_splits.h1_1_two_att, -1) AS a_h1_1_two_att,
    IFNULL(opp_splits.h1_2_two_att, -1) AS a_h1_2_two_att,
    IFNULL(opp_splits.h1_3_two_att, -1) AS a_h1_3_two_att,
    IFNULL(opp_splits.h1_4_two_att, -1) AS a_h1_4_two_att,
    (CASE WHEN opp_splits.h1_1_two_att IS NULL OR opp_splits.h1_2_two_att IS NULL OR opp_splits.h1_3_two_att IS NULL OR opp_splits.h1_4_two_att IS NULL
        THEN -1 ELSE (opp_splits.h1_1_two_att + opp_splits.h1_2_two_att + opp_splits.h1_3_two_att + opp_splits.h1_4_two_att) END) AS a_h1_two_att,
    IFNULL(opp_splits.h2_1_two_att, -1) AS a_h2_1_two_att,
    IFNULL(opp_splits.h2_2_two_att, -1) AS a_h2_2_two_att,
    IFNULL(opp_splits.h2_3_two_att, -1) AS a_h2_3_two_att,
    IFNULL(opp_splits.h2_4_two_att, -1) AS a_h2_4_two_att,
    (CASE WHEN opp_splits.h2_1_two_att IS NULL OR opp_splits.h2_2_two_att IS NULL OR opp_splits.h2_3_two_att IS NULL OR opp_splits.h2_4_two_att IS NULL
        THEN -1 ELSE (opp_splits.h2_1_two_att + opp_splits.h2_2_two_att + opp_splits.h2_3_two_att + opp_splits.h2_4_two_att) END) AS a_h2_two_att,
    IFNULL(opp_splits.ot_two_att, -1) AS a_ot_two_att,

    IFNULL(opp_splits.h1_1_two, -1) AS a_h1_1_two,
    IFNULL(opp_splits.h1_2_two, -1) AS a_h1_2_two,
    IFNULL(opp_splits.h1_3_two, -1) AS a_h1_3_two,
    IFNULL(opp_splits.h1_4_two, -1) AS a_h1_4_two,
    (CASE WHEN opp_splits.h1_1_two IS NULL OR opp_splits.h1_2_two IS NULL OR opp_splits.h1_3_two IS NULL OR opp_splits.h1_4_two IS NULL
        THEN -1 ELSE (opp_splits.h1_1_two + opp_splits.h1_2_two + opp_splits.h1_3_two + opp_splits.h1_4_two) END) AS a_h1_two,
    IFNULL(opp_splits.h2_1_two, -1) AS a_h2_1_two,
    IFNULL(opp_splits.h2_2_two, -1) AS a_h2_2_two,
    IFNULL(opp_splits.h2_3_two, -1) AS a_h2_3_two,
    IFNULL(opp_splits.h2_4_two, -1) AS a_h2_4_two,
    (CASE WHEN opp_splits.h2_1_two IS NULL OR opp_splits.h2_2_two IS NULL OR opp_splits.h2_3_two IS NULL OR opp_splits.h2_4_two IS NULL
        THEN -1 ELSE (opp_splits.h2_1_two + opp_splits.h2_2_two + opp_splits.h2_3_two + opp_splits.h2_4_two) END) AS a_h2_two,
    IFNULL(opp_splits.ot_two, -1) AS a_ot_two,

    IFNULL(opp_splits.h1_1_free_att, -1) AS a_h1_1_free_att,
    IFNULL(opp_splits.h1_2_free_att, -1) AS a_h1_2_free_att,
    IFNULL(opp_splits.h1_3_free_att, -1) AS a_h1_3_free_att,
    IFNULL(opp_splits.h1_4_free_att, -1) AS a_h1_4_free_att,
    (CASE WHEN opp_splits.h1_1_free_att IS NULL OR opp_splits.h1_2_free_att IS NULL OR opp_splits.h1_3_free_att IS NULL OR opp_splits.h1_4_free_att IS NULL
        THEN -1 ELSE (opp_splits.h1_1_free_att + opp_splits.h1_2_free_att + opp_splits.h1_3_free_att + opp_splits.h1_4_free_att) END) AS a_h1_free_att,
    IFNULL(opp_splits.h2_1_free_att, -1) AS a_h2_1_free_att,
    IFNULL(opp_splits.h2_2_free_att, -1) AS a_h2_2_free_att,
    IFNULL(opp_splits.h2_3_free_att, -1) AS a_h2_3_free_att,
    IFNULL(opp_splits.h2_4_free_att, -1) AS a_h2_4_free_att,
    (CASE WHEN opp_splits.h2_1_free_att IS NULL OR opp_splits.h2_2_free_att IS NULL OR opp_splits.h2_3_free_att IS NULL OR opp_splits.h2_4_free_att IS NULL
        THEN -1 ELSE (opp_splits.h2_1_free_att + opp_splits.h2_2_free_att + opp_splits.h2_3_free_att + opp_splits.h2_4_free_att) END) AS a_h2_free_att,
    IFNULL(opp_splits.ot_free_att, -1) AS a_ot_free_att,

    IFNULL(opp_splits.h1_1_free, -1) AS a_h1_1_free,
    IFNULL(opp_splits.h1_2_free, -1) AS a_h1_2_free,
    IFNULL(opp_splits.h1_3_free, -1) AS a_h1_3_free,
    IFNULL(opp_splits.h1_4_free, -1) AS a_h1_4_free,
    (CASE WHEN opp_splits.h1_1_free IS NULL OR opp_splits.h1_2_free IS NULL OR opp_splits.h1_3_free IS NULL OR opp_splits.h1_4_free IS NULL
        THEN -1 ELSE (opp_splits.h1_1_free + opp_splits.h1_2_free + opp_splits.h1_3_free + opp_splits.h1_4_free) END) AS a_h1_free,
    IFNULL(opp_splits.h2_1_free, -1) AS a_h2_1_free,
    IFNULL(opp_splits.h2_2_free, -1) AS a_h2_2_free,
    IFNULL(opp_splits.h2_3_free, -1) AS a_h2_3_free,
    IFNULL(opp_splits.h2_4_free, -1) AS a_h2_4_free,
    (CASE WHEN opp_splits.h2_1_free IS NULL OR opp_splits.h2_2_free IS NULL OR opp_splits.h2_3_free IS NULL OR opp_splits.h2_4_free IS NULL
        THEN -1 ELSE (opp_splits.h2_1_free + opp_splits.h2_2_free + opp_splits.h2_3_free + opp_splits.h2_4_free) END) AS a_h2_free,
    IFNULL(opp_splits.ot_free, -1) AS a_ot_free,

    IFNULL(opp_splits.h1_1_off_rebounds, -1) AS a_h1_1_off_rebounds,
    IFNULL(opp_splits.h1_2_off_rebounds, -1) AS a_h1_2_off_rebounds,
    IFNULL(opp_splits.h1_3_off_rebounds, -1) AS a_h1_3_off_rebounds,
    IFNULL(opp_splits.h1_4_off_rebounds, -1) AS a_h1_4_off_rebounds,
    (CASE WHEN opp_splits.h1_1_off_rebounds IS NULL OR opp_splits.h1_2_off_rebounds IS NULL OR opp_splits.h1_3_off_rebounds IS NULL OR opp_splits.h1_4_off_rebounds IS NULL
        THEN -1 ELSE (opp_splits.h1_1_off_rebounds + opp_splits.h1_2_off_rebounds + opp_splits.h1_3_off_rebounds + opp_splits.h1_4_off_rebounds) END) AS a_h1_off_rebounds,
    IFNULL(opp_splits.h2_1_off_rebounds, -1) AS a_h2_1_off_rebounds,
    IFNULL(opp_splits.h2_2_off_rebounds, -1) AS a_h2_2_off_rebounds,
    IFNULL(opp_splits.h2_3_off_rebounds, -1) AS a_h2_3_off_rebounds,
    IFNULL(opp_splits.h2_4_off_rebounds, -1) AS a_h2_4_off_rebounds,
    (CASE WHEN opp_splits.h2_1_off_rebounds IS NULL OR opp_splits.h2_2_off_rebounds IS NULL OR opp_splits.h2_3_off_rebounds IS NULL OR opp_splits.h2_4_off_rebounds IS NULL
        THEN -1 ELSE (opp_splits.h2_1_off_rebounds + opp_splits.h2_2_off_rebounds + opp_splits.h2_3_off_rebounds + opp_splits.h2_4_off_rebounds) END) AS a_h2_off_rebounds,
    IFNULL(opp_splits.ot_off_rebounds, -1) AS a_ot_off_rebounds,

    IFNULL(opp_splits.h1_1_def_rebounds, -1) AS a_h1_1_def_rebounds,
    IFNULL(opp_splits.h1_2_def_rebounds, -1) AS a_h1_2_def_rebounds,
    IFNULL(opp_splits.h1_3_def_rebounds, -1) AS a_h1_3_def_rebounds,
    IFNULL(opp_splits.h1_4_def_rebounds, -1) AS a_h1_4_def_rebounds,
    (CASE WHEN opp_splits.h1_1_def_rebounds IS NULL OR opp_splits.h1_2_def_rebounds IS NULL OR opp_splits.h1_3_def_rebounds IS NULL OR opp_splits.h1_4_def_rebounds IS NULL
        THEN -1 ELSE (opp_splits.h1_1_def_rebounds + opp_splits.h1_2_def_rebounds + opp_splits.h1_3_def_rebounds + opp_splits.h1_4_def_rebounds) END) AS a_h1_def_rebounds,
    IFNULL(opp_splits.h2_1_def_rebounds, -1) AS a_h2_1_def_rebounds,
    IFNULL(opp_splits.h2_2_def_rebounds, -1) AS a_h2_2_def_rebounds,
    IFNULL(opp_splits.h2_3_def_rebounds, -1) AS a_h2_3_def_rebounds,
    IFNULL(opp_splits.h2_4_def_rebounds, -1) AS a_h2_4_def_rebounds,
    (CASE WHEN opp_splits.h2_1_def_rebounds IS NULL OR opp_splits.h2_2_def_rebounds IS NULL OR opp_splits.h2_3_def_rebounds IS NULL OR opp_splits.h2_4_def_rebounds IS NULL
        THEN -1 ELSE (opp_splits.h2_1_def_rebounds + opp_splits.h2_2_def_rebounds + opp_splits.h2_3_def_rebounds + opp_splits.h2_4_def_rebounds) END) AS a_h2_def_rebounds,
    IFNULL(opp_splits.ot_def_rebounds, -1) AS a_ot_def_rebounds,

    IFNULL(opp_splits.h1_1_rebounds, -1) AS a_h1_1_rebounds,
    IFNULL(opp_splits.h1_2_rebounds, -1) AS a_h1_2_rebounds,
    IFNULL(opp_splits.h1_3_rebounds, -1) AS a_h1_3_rebounds,
    IFNULL(opp_splits.h1_4_rebounds, -1) AS a_h1_4_rebounds,
    (CASE WHEN opp_splits.h1_1_rebounds IS NULL OR opp_splits.h1_2_rebounds IS NULL OR opp_splits.h1_3_rebounds IS NULL OR opp_splits.h1_4_rebounds IS NULL
        THEN -1 ELSE (opp_splits.h1_1_rebounds + opp_splits.h1_2_rebounds + opp_splits.h1_3_rebounds + opp_splits.h1_4_rebounds) END) AS a_h1_rebounds,
    IFNULL(opp_splits.h2_1_rebounds, -1) AS a_h2_1_rebounds,
    IFNULL(opp_splits.h2_2_rebounds, -1) AS a_h2_2_rebounds,
    IFNULL(opp_splits.h2_3_rebounds, -1) AS a_h2_3_rebounds,
    IFNULL(opp_splits.h2_4_rebounds, -1) AS a_h2_4_rebounds,
    (CASE WHEN opp_splits.h2_1_rebounds IS NULL OR opp_splits.h2_2_rebounds IS NULL OR opp_splits.h2_3_rebounds IS NULL OR opp_splits.h2_4_rebounds IS NULL
        THEN -1 ELSE (opp_splits.h2_1_rebounds + opp_splits.h2_2_rebounds + opp_splits.h2_3_rebounds + opp_splits.h2_4_rebounds) END) AS a_h2_rebounds,
    IFNULL(opp_splits.ot_rebounds, -1) AS a_ot_rebounds,

    IFNULL(opp_splits.h1_1_assists, -1) AS a_h1_1_assists,
    IFNULL(opp_splits.h1_2_assists, -1) AS a_h1_2_assists,
    IFNULL(opp_splits.h1_3_assists, -1) AS a_h1_3_assists,
    IFNULL(opp_splits.h1_4_assists, -1) AS a_h1_4_assists,
    (CASE WHEN opp_splits.h1_1_assists IS NULL OR opp_splits.h1_2_assists IS NULL OR opp_splits.h1_3_assists IS NULL OR opp_splits.h1_4_assists IS NULL
        THEN -1 ELSE (opp_splits.h1_1_assists + opp_splits.h1_2_assists + opp_splits.h1_3_assists + opp_splits.h1_4_assists) END) AS a_h1_assists,
    IFNULL(opp_splits.h2_1_assists, -1) AS a_h2_1_assists,
    IFNULL(opp_splits.h2_2_assists, -1) AS a_h2_2_assists,
    IFNULL(opp_splits.h2_3_assists, -1) AS a_h2_3_assists,
    IFNULL(opp_splits.h2_4_assists, -1) AS a_h2_4_assists,
    (CASE WHEN opp_splits.h2_1_assists IS NULL OR opp_splits.h2_2_assists IS NULL OR opp_splits.h2_3_assists IS NULL OR opp_splits.h2_4_assists IS NULL
        THEN -1 ELSE (opp_splits.h2_1_assists + opp_splits.h2_2_assists + opp_splits.h2_3_assists + opp_splits.h2_4_assists) END) AS a_h2_assists,
    IFNULL(opp_splits.ot_assists, -1) AS a_ot_assists,

    IFNULL(opp_splits.h1_1_turnovers, -1) AS a_h1_1_turnovers,
    IFNULL(opp_splits.h1_2_turnovers, -1) AS a_h1_2_turnovers,
    IFNULL(opp_splits.h1_3_turnovers, -1) AS a_h1_3_turnovers,
    IFNULL(opp_splits.h1_4_turnovers, -1) AS a_h1_4_turnovers,
    (CASE WHEN opp_splits.h1_1_turnovers IS NULL OR opp_splits.h1_2_turnovers IS NULL OR opp_splits.h1_3_turnovers IS NULL OR opp_splits.h1_4_turnovers IS NULL
        THEN -1 ELSE (opp_splits.h1_1_turnovers + opp_splits.h1_2_turnovers + opp_splits.h1_3_turnovers + opp_splits.h1_4_turnovers) END) AS a_h1_turnovers,
    IFNULL(opp_splits.h2_1_turnovers, -1) AS a_h2_1_turnovers,
    IFNULL(opp_splits.h2_2_turnovers, -1) AS a_h2_2_turnovers,
    IFNULL(opp_splits.h2_3_turnovers, -1) AS a_h2_3_turnovers,
    IFNULL(opp_splits.h2_4_turnovers, -1) AS a_h2_4_turnovers,
    (CASE WHEN opp_splits.h2_1_turnovers IS NULL OR opp_splits.h2_2_turnovers IS NULL OR opp_splits.h2_3_turnovers IS NULL OR opp_splits.h2_4_turnovers IS NULL
        THEN -1 ELSE (opp_splits.h2_1_turnovers + opp_splits.h2_2_turnovers + opp_splits.h2_3_turnovers + opp_splits.h2_4_turnovers) END) AS a_h2_turnovers,
    IFNULL(opp_splits.ot_turnovers, -1) AS a_ot_turnovers,

    IFNULL(opp_splits.h1_1_blocks, -1) AS a_h1_1_blocks,
    IFNULL(opp_splits.h1_2_blocks, -1) AS a_h1_2_blocks,
    IFNULL(opp_splits.h1_3_blocks, -1) AS a_h1_3_blocks,
    IFNULL(opp_splits.h1_4_blocks, -1) AS a_h1_4_blocks,
    (CASE WHEN opp_splits.h1_1_blocks IS NULL OR opp_splits.h1_2_blocks IS NULL OR opp_splits.h1_3_blocks IS NULL OR opp_splits.h1_4_blocks IS NULL
        THEN -1 ELSE (opp_splits.h1_1_blocks + opp_splits.h1_2_blocks + opp_splits.h1_3_blocks + opp_splits.h1_4_blocks) END) AS a_h1_blocks,
    IFNULL(opp_splits.h2_1_blocks, -1) AS a_h2_1_blocks,
    IFNULL(opp_splits.h2_2_blocks, -1) AS a_h2_2_blocks,
    IFNULL(opp_splits.h2_3_blocks, -1) AS a_h2_3_blocks,
    IFNULL(opp_splits.h2_4_blocks, -1) AS a_h2_4_blocks,
    (CASE WHEN opp_splits.h2_1_blocks IS NULL OR opp_splits.h2_2_blocks IS NULL OR opp_splits.h2_3_blocks IS NULL OR opp_splits.h2_4_blocks IS NULL
        THEN -1 ELSE (opp_splits.h2_1_blocks + opp_splits.h2_2_blocks + opp_splits.h2_3_blocks + opp_splits.h2_4_blocks) END) AS a_h2_blocks,
    IFNULL(opp_splits.ot_blocks, -1) AS a_ot_blocks,

    IFNULL(opp_splits.h1_1_fouls, -1) AS a_h1_1_fouls,
    IFNULL(opp_splits.h1_2_fouls, -1) AS a_h1_2_fouls,
    IFNULL(opp_splits.h1_3_fouls, -1) AS a_h1_3_fouls,
    IFNULL(opp_splits.h1_4_fouls, -1) AS a_h1_4_fouls,
    (CASE WHEN opp_splits.h1_1_fouls IS NULL OR opp_splits.h1_2_fouls IS NULL OR opp_splits.h1_3_fouls IS NULL OR opp_splits.h1_4_fouls IS NULL
        THEN -1 ELSE (opp_splits.h1_1_fouls + opp_splits.h1_2_fouls + opp_splits.h1_3_fouls + opp_splits.h1_4_fouls) END) AS a_h1_fouls,
    IFNULL(opp_splits.h2_1_fouls, -1) AS a_h2_1_fouls,
    IFNULL(opp_splits.h2_2_fouls, -1) AS a_h2_2_fouls,
    IFNULL(opp_splits.h2_3_fouls, -1) AS a_h2_3_fouls,
    IFNULL(opp_splits.h2_4_fouls, -1) AS a_h2_4_fouls,
    (CASE WHEN opp_splits.h2_1_fouls IS NULL OR opp_splits.h2_2_fouls IS NULL OR opp_splits.h2_3_fouls IS NULL OR opp_splits.h2_4_fouls IS NULL
        THEN -1 ELSE (opp_splits.h2_1_fouls + opp_splits.h2_2_fouls + opp_splits.h2_3_fouls + opp_splits.h2_4_fouls) END) AS a_h2_fouls,
    IFNULL(opp_splits.ot_fouls, -1) AS a_ot_fouls
FROM `stardust-development.temp.teams_games_wide_v15`
WHERE games.home_team=true