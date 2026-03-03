favorite_movies = []

def add_movie(movie):
    favorite_movies.append(movie)
    print(f"Movie '{movie}' added.")

def remove_movie(movie):
    if movie in favorite_movies:
        favorite_movies.remove(movie)
        print(f"Movie '{movie}' removed.")
    else:
        print(f"Movie '{movie}' not found.")

def display_movies():
    print("Movies List:")
    for movie in favorite_movies:
        print(f"- {movie}")

def count_movies():
    count = 0
    for movie in favorite_movies:
        count += 1
    print(f"{count} movies")

def find_movie(movie):
    for found in favorite_movies:
        if found == movie:
            break
        print(found)

def clear_movies():
    favorite_movies.clear()