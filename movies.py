# TODO: README documentation and requirements

# Movie database
# Title, Director, Year, Genre
# =============================
movies = [
    {"title": "John Wick", "director": "Chad Stahelski", "year": 2014, "genre": "action", "rating": 7.4}
]

# TODO: Add AWS RDS connection string


# =============================
# App UI
# =============================
def menu():
    print("======================================================================================================")
    print("Welcome to Jeremy's Movie Database")
    print("View all movies (v), Add a new movie (a), Search for movie by title (s), Quit app (q)")
    print("======================================================================================================")
    print()
    ui = input("What would you like to do? ")

    user_options = {
        "v": list_all,
        "a": add_movie,
        "s": search_movies
    }

    if ui in user_options:
        selected_command = user_options[ui]
        selected_command()
    elif ui == 'q':
        quit()
    else:
        print("unknown command. please try again.")

    # TODO Modify user interface to make easier to use


# =============================
# List all movies in collection
# =============================
def list_all():
    for movie in movies:
        # variables
        title = movie["title"]
        director = movie["director"]
        year = movie['year']
        genre = movie['genre']
        rating = movie['rating']

        print(title, year, director, genre, rating, sep=" | ")

    print()


# Add new movies to collection
def add_movie():
    title = input("What is the title? ").title()
    director = input("Who is the director? ").title()
    year = int(input("When was the film released? "))
    genre = input("What kind of movie is it? ").lower()
    rating = float(input("What was the movie's IMDB rating? "))

    class Movie:
        def __init__(self, mtitle, mdirector, myear, mgenre, mrating):
            self.title = mtitle
            self.director = mdirector
            self.year = myear
            self.genre = mgenre
            self.rating = mrating

        def __len__(self):
            return len(self.title)

        def __repr__(self):
            return self.title

        def __str__(self):
            return f"Movie object {self.title} with len {len(self)}"

        #@property
        def mdict(self):
            return {"title": self.title, "director": self.director, "year": self.year, "genre": self.genre,
                    "rating": self.rating}

    new_movie = Movie(title, director, year, genre, rating)
    movies.append(new_movie.mdict())

    print(new_movie)
    print()

    # TODO Change to a class
    # TODO Add comprehensive data entry validation


# Find a movie by title
def search_movies():
    q = input("What movie are you looking for? ").title()
    for movie in movies:
        # variables
        title = movie["title"]
        director = movie["director"]
        year = movie['year']
        genre = movie['genre']
        rating = movie['rating']

        if q == movie["title"]:
            print(title, year, director, genre, rating, sep=" | ")
            print()
        else:
            print("movie not found in database")
            print()

    # TODO search result should only
    # TODO Make search more robust using regex


if __name__ == "__main__":
    while True:
        menu()

