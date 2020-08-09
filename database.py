# Board game database
# Title, Director, Year, Genre
# =============================
# TODO: Add AWS RDS connection string

games = [
    {"title": "7 Wonders", "year": 2010, "designer": "Antoine Bauza", "time": 30, "players": 7, "rating": 7.8,
     "played": False},
    {"title": "Wingspan", "year": 2020, "designer": "Stonemeir Games", "time": 30, "players": 5, "rating": 9,
     "played": False}
]


def db_read():
    return games


def db_add_game(title, year, designer, time, players, rating, played):
    class Game:
        def __init__(self, mtitle, myear, mdesigner, mtime, mplayers, mrating, mplayed):
            self.title = mtitle
            self.year = myear
            self.designer = mdesigner
            self.time = mtime
            self.players = mplayers
            self.rating = mrating
            self.played = mplayed

        def __repr__(self):
            return self.title

        def __str__(self):
            return f"Game Object for {self.title}."

        def mdict(self):
            return {"title": self.title, "year": self.year, "designer": self.designer, "time": self.time,
                    "players": self.players, "rating": self.rating, "played": self.played}

    new_game = Game(title, year, designer, time, players, rating, played)

    try:
        games.append(new_game.mdict())
        return new_game
    except TypeError:
        print('This is not the right type of object.')
        raise


def db_mark_game_played(name):
    for game in games:
        if name == game['title']:
            print(game)
            if not game['played']:
                game['played'] = True
            else:
                game['played'] = False
            print(game)


def db_delete_game(name):
    for i in range(len(games)):
        if games[i]['title'] == name:
            del games[i]


def db_search_games(name):
    for i in range(len(games)):
        if games[i]['title'] == name:
            return games[i]

            # TODO Make search more robust using regex
            # TODO return printed display of output
