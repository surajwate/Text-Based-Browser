"""The file animals.txt has a list of animals, each written on a new line. For example:

rabbit
cat
turtle

Create a new file, animals_new.txt, where those animals are written on a single line and separated by whitespace.
    """

animal_file = open('animals.txt', 'r')
animals = animal_file.read()
animals = animals.replace('\n', ' ')  # replace new line with space

new_animal_file = open('animals_new.txt', 'w', encoding='utf-8')
new_animal_file.write(animals)

animal_file.close()
new_animal_file.close()