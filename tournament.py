#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection and cursor."""
    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    return DB, c

def deleteMatches():
    """Remove all the match records from the database."""
    query = ("DELETE FROM MATCHES;")
    DB, c = connect()
    c.execute(query,)
    DB.commit()
    DB.close()
    return
    


def deletePlayers():
    """Remove all the player records from the database."""
    query = ("DELETE FROM PLAYERS;")
    DB, c = connect()
    c.execute(query,)
    DB.commit()
    DB.close()
    return

def countPlayers():
    """Returns the number of players currently registered."""
    query = ("SELECT COUNT(PLAYER_NAME) FROM PLAYERS;")
    DB, c = connect()
    c.execute(query,)
    result = c.fetchone()[0]
    DB.commit()
    DB.close()
    return result  


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.

    Args:
      name: the player's full name (need not be unique).

    Returns:
      The ID number assigned to this player (as an int)
    """
    query = ("INSERT INTO players (player_name) "
             "VALUES (%s) "
             "RETURNING player_id")
    param = (name,)

    DB, c = connect()

    #Register the player.
    c.execute(query, param)
    id = c.fetchall()[0][0]

    #Add the player to player_standings table with no wins or matches.
    query = ("INSERT INTO player_standings (player_id, player_name, wins, matches_played) "
        "VALUES (%s) "
        "RETURNING player_id")

    param = (int(id), str(name), int(0), int(0),)
    c.execute(query, param)    
    DB.commit()
    DB.close()
    return id


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """


