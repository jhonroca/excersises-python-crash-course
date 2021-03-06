# Make an empty list to store people in.
people = []

# Define some people, and add them to the list.
person = {
    'first_name': 'eric',
    'last_name': 'matthes',
    'age': 43,
    'city': 'sitka',
}
people.append(person)

person = {
    'first_name': 'ever',
    'last_name': 'matthes',
    'age': 5,
    'city': 'sitka',
}
people.append(person)

person = {
    'first_name': 'willie',
    'last_name': 'matthes',
    'age': 8,
    'city': 'sitka',
}
people.append(person)

# Display all of the information in the dictionary.
for person in people:
    name = person['first_name'].title() + " " + person['last_name'].title()
    age = str(person['age'])
    city = person['city'].title()

    print(name + ", of " + city + ", is " + age + " years old.")


# PETS
# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'python',
    'name': 'john',
    'owner': 'guido',
    'weight': 43,
    'eats': 'bugs',
}
pets.append(pet)

pet = {
    'animal type': 'chicken',
    'name': 'clarence',
    'owner': 'tiffany',
    'weight': 2,
    'eats': 'seeds',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'peso',
    'owner': 'eric',
    'weight': 37,
    'eats': 'shoes',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))

# FAVORITES PLACES

favorite_places = {
    'paul': 'piramides',
    'meli': 'caribe',
    'vale': 'disney',
}
for name, places in favorite_places.items():
    print(f"\t{name.title()}, le gusta ir a {places}!")


print("hola mundo!!!")

print("hola jeropas!!!")

print("como estan amigos")

print("duermen mis niñas")

# 6.11 CITIES

cities = {
    'lima': {
        'country': 'peru',
        'population': '30 millones',
        'echo': 'rusia 2018',
    },

    'new york': {
        'country': 'eeuu',
        'population': '230 millones',
        'echo': 'torres gemelas',
    },

    'berlin': {
        'country': 'alemania',
        'population': '100 millones',
        'echo': 'holocausto',
    },
}
for city, city_info in cities.items():
    print(f"\nCity: {city}")
    country = city_info['country']
    population = city_info['population']
    echo = city_info['echo']

    print(f"\tCountry: {country.title()}")
    print(f"\tPopulation: {population.title()}")
    print(f"\tEcho: {echo.title()}")

# FAVORITE NUMBERS
favorite_numbers = {
    'paul': ['10', '4'],
    'melissa': ['7', '5'],
    'vale': ['9', '2', '8'],
    'ariana': ['2', '1', '0'],
    'margaracha': ['60'],
}
for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number.title()}")
