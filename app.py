import database

# TODO: README documentation and requirements


# =============================
# App UI
# =============================
def menu():
    #database.create_game_table()

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

        ui = input("What would you like to do? ")
        # raise(f"User entered '{ui}'. This is not a menu option. Please enter v, a, or s.")
    # except TypeError:
    #     raise(f"User entered '{ui}'. This command does not have a value.")
    # except NotImplemented:
    #     raise(f"User entered '{ui}'. This command has not been implemented yet.")

    # TODO Modify user interface to make easier to use
    # TODO Try and add raise exceptions based on user input type


# List all movies in collection
def list_all():
    games = database.db_read()

    for game in games:
        # variables
        title = game[1]
        year = game[2]
        designer = game[3]
        time = game[4]
        players = game[5]
        rating = game[6]
        played = game[7]
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

    new_game = database.db_add_game(title, year, designer, time, players, rating, played=False)

    print(new_game)
    print()

    # TODO Add comprehensive data entry validation and cleaning
    # TODO Use error handling in code


# Find a movie by title
def search_games():
    q = input("What game are you looking for? ")
    search_result = database.db_search_games(q)
    print(search_result)


def mark_played():
    q = input("What game have you played? ")
    database.db_mark_game_played(q)


def delete_game():
    q = input("What game do you want to delete? ")
    database.db_delete_game(q)


if __name__ == "__main__":
    menu()

