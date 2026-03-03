planet_list = ["Mercury", "Mars"]

def add_planets(planet):
    planet_list.append(planet)

add_planets("Jupiter")
add_planets("Saturn")

print(planet_list)

continued_list = ["Neptune", "Uranus"]

planet_list.extend(continued_list)

print(planet_list)

planet_list.insert(1, "Earth")
planet_list.insert(1, "Venus")

add_planets("Pluto")

print(planet_list)

x = slice(0, 4)
rocky_planets = []

rocky_planets.append(planet_list[x])

print(rocky_planets)
print(planet_list)

del planet_list[8]

print(planet_list)

spacecraft_list = [
    ("Mariner 10", "Mercury", "Venus"),
    ("MESSENGER", "Mercury", "Venus"),
    ("Venera 1-16", "Venus"),
    ("Mariner 2", "Venus"),
    ("Mariner 5", "Venus"),
    ("Pioneer Venus 1 and 2", "Venus"),
    ("Vega 1 and 2", "Venus"),
    ("Magellan", "Venus"),
    ("Venus Express", "Venus"),
    ("Parker Solar Probe", "Venus"),
    ("Mariner 4", "Mars"),
    ("Mariner 6 and 7", "Mars"),
    ("Mariner 9", "Mars"),
    ("Viking 1 and 2", "Mars"),
    ("Mars Pathfinder", "Mars"),
    ("Mars Odyssey", "Mars"),
    ("Spirit", "Mars"),
    ("Opportunity", "Mars"),
    ("Phoenix", "Mars"),
    ("Dawn", "Mars"),
    ("Curiosity", "Mars"),
    ("InSight", "Mars"),
    ("Perseverance", "Mars"),
    ("Pioneer 10 and 11", "Jupiter"),
    ("Voyager 1 and 2", "Jupiter", "Saturn", "Uranus", "Neptune"),
    ("Ulysses", "Jupiter"),
    ("Galileo", "Venus", "Jupiter"),
    ("Cassini", "Venus", "Jupiter", "Saturn"),
    ("New Horizons", "Jupiter", "Pluto"),
    ("Juno", "Jupiter"),
    ("Pioneer 11", "Jupiter", "Saturn"),
]

for craft in spacecraft_list:
    spacecraft = craft[0:1]
    planets = craft[1:]
    print(f"{spacecraft[0]} has visited")
    print("-------------------")
    for planet in planets:
        print(f"{planet}")
