planet_list = ["Mercury", "Mars"]

def add_planets(planet):
    planet_list.append(planet)

add_planets("Jupiter")
add_planets("Saturn")

print(planet_list)

continued_list = ["Neptune", "Uranus"]

planet_list.extend(continued_list)

print(planet_list)

planet_list.insert(2, "Earth")
planet_list.insert(1, "Venus")

add_planets("Pluto")

print(planet_list)