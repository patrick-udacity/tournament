# Swiss-system Tournament Planner

#### Udacity Full Stack Developer - Tournament Project.

### Schedule rank-based tournament matchups
In this project, you’ll be writing a Python module that uses the PostgreSQL database to keep track of players and matches in a game tournament.
The game tournament will use the Swiss system for pairing up players in each round: players are not eliminated, and each player should be paired with another player with the same number of wins, or as close as possible.

For a reference to the **Swiss Elimination Tournament Planner** see [Swiss-system](https://en.wikipedia.org/wiki/Swiss-system_tournament).

### Installation
1. If you don't already have Vagrant VM, you can [download it here](https://www.virtualbox.org/wiki/Downloads) and install it on your machine.
2. Download the [latest release of this project](https://github.com/patrick-udacity/tournament) from GitHub.
3. Extract the zipped files to your Vagrant directory.
4. From the terminal, change to your working directory using ` cd /vagrant`.
5. Type `vagrant up` to launch the virtual machine. Then type `vagrant ssh` to log in.
6. In the VM, `cd` to the `/tournament` folder.
7. Setup the PostgreSQL database with the command, `psql -f tournament.sql`

### Usage
Add players into database with the `register_player()` function which takes a single string argument.
```
Example:
register_player("Roger Wilco")
```
Almost all of the other functions have the optional `tournament_id` argument, which specifies the tournament of which the match belonged. This allows the **Swiss-system Tournament Planner** to track, archive, and calculate the ranking for each player.

Report and archive match results with the `report_match()` function. Insert the id's of the winner and loser of a match.
```
Example:
report_match(12,17)
```
Simply call the `swiss_pairings()` function, and the module will calculate the next pair of player matchups for a given tournament. Finally, `player_standings()` returns the current rankings/standings of the given tournament.

### What's included
Inside the **Tournament** directory, you'll find the following files:
```
Swiss Tournament Planner/
    ├──tournament.py
    ├──tournament.sql
    ├──tournament_test.sql
    └──README.md
```

### Contact:
patrick.udacity@gmail.com