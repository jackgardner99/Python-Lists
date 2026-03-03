"""
this module provides basic python practice    
"""

favorite_movies = []

def add_movie(movie):
    """Add a movie """
    favorite_movies.append(movie)
    print(f"Movie '{movie}' added.")

def remove_movie(movie):
    """Remove Movie"""
    if movie in favorite_movies:
        favorite_movies.remove(movie)
        print(f"Movie '{movie}' removed.")
    else:
        print(f"Movie '{movie}' not found.")

def display_movies():
    """Display Movies"""
    print("Movies List:")
    for movie in favorite_movies:
        print(f"- {movie}")

def count_movies():
    """Count Movies"""
    count = 0
    for movie in favorite_movies:
        if movie:
            count += 1
    print(f"{count} movies")

def find_movie(movie):
    """find Movie"""
    for found in favorite_movies:
        if found == movie:
            break
        print(found)

def clear_movies():
    """clear Movies"""
    favorite_movies.clear()

add_movie("Jurassic Park")
add_movie("Star Wars")
add_movie("Star Trek")

display_movies()
