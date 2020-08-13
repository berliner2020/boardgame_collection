import json
import mysql.connector

# Get connection string from local
with open("connectionstring.json") as file:
    contents = json.load(file)

# DB Connection
mydb = mysql.connector.connect(
    host=contents['host'],
    port=contents['port'],
    user=contents['user'],
    password=contents['password'],
    database=contents['database'],
)


def create_game_table():
    mydb
    mycursor = mydb.cursor()
    mycursor.execute('''CREATE TABLE IF NOT EXISTS games(id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), 
    year SMALLINT(4),
    designer VARCHAR(255), time SMALLINT(3), players SMALLINT(2), rating FLOAT(3), played BOOLEAN)''')
    mydb.commit()


def db_read():
    mydb
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM games")
    games = mycursor.fetchall()
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
        mydb
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
    mydb
    mycursor = mydb.cursor()
    mycursor.execute("UPDATE games SET played = 1 WHERE title = %s", (name,))
    mydb.commit()


def db_delete_game(name):
    print(name)
    mycursor = mydb.cursor()
    mycursor.execute("DELETE FROM games WHERE title = %s", (name,))
    mydb.commit()


def db_search_games(name):
    print(name)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM games WHERE title = %s", (name,))
    myresult = mycursor.fetchall()
    return myresult


    # for i in range(len(games)):
    #     if games[i]['title'] == name:
    #         return games[i]

    # TODO Make search more robust using regex
    # TODO return printed display of output
