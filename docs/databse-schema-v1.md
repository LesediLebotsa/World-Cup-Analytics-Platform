teams
-----
* id
* name
* country_code
* fifa_rank
* created_at

matches
-------
* id
* match_date
* home_team_id
* away_team_id
* home_score
* away_score
* tournament
* city
* country
* neutral

world_cups
-----------
* id
* year
* host_country
* winner
* runner_up
* teams_entered
* matches_played

users
------
* id
* email
* password_hash
* role
* is_active
* created_at

predictions
------------
* id
* user_id
* team_a_id
* team_b_id
* predicted_winner_id
* probability
* model_type
* created_at