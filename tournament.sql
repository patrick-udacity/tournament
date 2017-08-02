-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
--
-- We will want to cleanup from any previous impmentations of this database.
-- To make this easy we can make that cleanup part of the install.
-- To start the install, run the following after connected to PSQL
-- \i tournament.sql

--First delete, any previous 'tournament' database that might exist.
DROP DATABASE IF EXISTS tournament;

--Second, create the new tournament database
CREATE DATABASE tournament;

-- Connect to the newly created database
\c tournament;


--************************************
--   Tables Used in the Tournament DB 
--************************************

-- List of tournament players player id's and their names
CREATE TABLE players (
    player_id serial PRIMARY KEY,
    player_name text
); 

CREATE TABLE matches (
    match_id serial PRIMARY KEY,
    match_date TIMESTAMP DEFAULT NOW()
);

-- type used for playerStandings table
CREATE TYPE match_result AS ENUM ('won', 'lost', 'draw');

-- for each match, shows whether a player won, lost, or if it was a draw
CREATE TABLE all_match_results  (
    player int REFERENCES players(player_id),
    match int REFERENCES matches(match_id),
    result match_result 
);

--overall standing for each registered player.
CREATE TABLE player_standings (
    player_id int REFERENCES players(player_id),
    player_name text,
    wins int DEFAULT 0,
    matches_played int DEFAULT 0
);

