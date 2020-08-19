# Create a file planets.txt and write the names of the Solar system planets there, each on a new line. In total,
# the file should contain 8 lines with the following planets: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus,
# and Neptune.

planets = "Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune"
file = open('planets.txt', 'w', encoding='utf-8')

planets = planets.replace(',', '')
planets = planets.replace(' ', '\n')

file.writelines(planets)
file.close()
