import json
import mysql.connector

# Get credentials from
with open("connectionstring.json") as file:
    contents = json.load(file)


def create_game_table():
    mydb = mysql.connector.connect(
        host=contents['host'],
        port=contents['port'],
        user=contents['user'],
        password=contents['password'],
        database=contents['database'],
    )

    mycursor = mydb.cursor()
    mycursor.execute('''CREATE TABLE games(id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), year SMALLINT(4),
    designer VARCHAR(255), time SMALLINT(3), players SMALLINT(2), rating FLOAT(3), played BOOLEAN)''')

    mydb.commit()
    mydb.close()


def db_read():
    mydb = mysql.connector.connect(
        host=contents['host'],
        port=contents['port'],
        user=contents['user'],
        password=contents['password'],
        database=contents['database'],
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM games")
    myresult = mycursor.fetchall()

    return myresult

    mydb.commit()
    mydb.close()


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
        mydb = mysql.connector.connect(
            host=contents['host'],
            port=contents['port'],
            user=contents['user'],
            password=contents['password'],
            database=contents['database'],
        )

        mycursor = mydb.cursor()
        sql = "INSERT INTO games (title, year, designer, time, players, rating, played) VALUES (%s, %s, %s, %s, %s, " \
              "%s, %s)"
        val = (new_game.title, new_game.year, new_game.designer, new_game.time, new_game.players, new_game.rating,
               new_game.played)
        mycursor.execute(sql, val)

        mydb.commit()
        mydb.close()

        print(mycursor.rowcount, "record inserted.")

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
