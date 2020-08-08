import database

# TODO: README documentation and requirements


# =============================
# App UI
# =============================
def menu():
    print("======================================================================================================")
    print("Welcome to Jeremy's Board Game Database")
    print('''View all games (l), Add a new game (a), Search for a game by title (s), Mark game as played (p), 
          "Delete game (d), Quit app (q)''')
    print("======================================================================================================")
    print()

    ui = input("What would you like to do? ")

    while ui != "q":
        user_options = {
            "l": list_all,
            "a": add_game,
            "s": search_games,
            "p": mark_played,
            "d": delete_game
        }

        try:
            selected_command = user_options[ui]
            selected_command()
        except KeyError:
            raise

        menu()
        # raise(f"User entered '{ui}'. This is not a menu option. Please enter v, a, or s.")
    # except TypeError:
    #     raise(f"User entered '{ui}'. This command does not have a value.")
    # except NotImplemented:
    #     raise(f"User entered '{ui}'. This command has not been implemented yet.")

    # TODO Modify user interface to make easier to use
    # TODO Try and add raise exceptions based on user input type


# =============================
# List all movies in collection
# =============================
def list_all():
    for game in database.games:
        # variables
        title = game["title"]
        year = game['year']
        designer = game["designer"]
        time = game['time']
        players = game['players']
        rating = game['rating']
        played = game['played']

        print(title, year, designer, time, players, rating, played, sep=" | ")

    print()


# Add new movies to collection
def add_game():
    title = input("What is the title? ").title().strip()
    year = int(input("When was the game released? ").strip())
    designer = input("Who is the game designer? ").title().strip()
    time = input("How long does the game take to play? ").lower().strip()
    players = input("How many players? ")
    rating = float(input("What was the game's rating? ").strip())
    played = False

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
        database.games.append(new_game.mdict())
    except TypeError:
        print('This is not the right type of object.')
        raise

    print(new_game)
    print()

    # TODO Change to a class
    # TODO Add comprehensive data entry validation
    # TODO Use error handling in code


# Find a movie by title
def search_games():
    q = input("What game are you looking for? ")

    for i in range(len(database.games)):
        if database.games[i]['title'] == q:
            print(database.games[i])


        # if q == game['title']:
        #     # variables
        #     title = game["title"]
        #     year = game['year']
        #     designer = game["designer"]
        #     time = game['time']
        #     players = game['players']
        #     rating = game['rating']
        #
        #     print(title, year, designer, time, players, rating, sep=" | ")
        #     print()
        # else:
        #     print("movie not found in database")
        #     print()

    # TODO search result should only
    # TODO Make search more robust using regex


def mark_played():
    q = input("What game have you played? ")

    for game in database.games:
        if q == game['title']:
            print(game)
            if not game['played']:
                game['played'] = True
            else:
                game['played'] = False
            print(game)


def delete_game():
    q = input("What game do you want to delete? ")

    for i in range(len(database.games)):
        if database.games[i]['title'] == q:
            del database.games[i]


if __name__ == "__main__":
    menu()

