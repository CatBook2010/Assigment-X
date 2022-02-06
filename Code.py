from Person import Person
from Superhero import Superhero
from HealingSuperhero import HealingSuperhero

# We define following class `Person`.

# Do not change this cell but you have to run it to have
# the Person class in scope.


# Use the given Person class to instantantiate a list named persons with the following persons:

steve_rogers = Person("Steve Rogers", 1918)
bucky_barnes = Person("Bucky Barnes", 1917)
tony_stark = Person("Tony Stark", 1976)
bruce_banner = Person("Bruce Banner", 1969)
rhodey_rhodes = Person("Rhodey Rhodes", 1968)
wanda_maximoff = Person("Wanda Maximoff", 1989)
vision = Person("Vision", 2015)
peter_parker = Person("Peter Parker", 2001)
peter_quill = Person("Peter Quill", 1980)
monica_rambeau = Person("Monica Rambeau", 1984)
carol_danvers = Person("Carol Danvers", 1964)

persons = [steve_rogers, bucky_barnes, tony_stark, bruce_banner, rhodey_rhodes, wanda_maximoff, vision, peter_parker, peter_quill, monica_rambeau, carol_danvers]




# ## Task 1.2: Minimum and Maximum
# Find the **youngest** and **oldest** person in the given list.
# Save them in the variables `youngest` and `oldest`. Save the actual instance of the person in the variable and **not** just a string.

age_persons = {}

for person in persons:
    age_persons[person.compute_age()] = person

youngest = age_persons[min(age_persons.keys())]
oldest = age_persons[max(age_persons.keys())]

# def get_young_old(persons: list) -> tuple:
#     youngest = persons[0]
#     youngest_age = youngest.compute_age()
#     oldest = persons[0]
#     oldest_age = oldest.compute_age()

#     for person in persons:

#         if person.compute_age() < youngest_age:
#             youngest_age = person.compute_age()
#             youngest = person

#         elif person.compute_age() > oldest_age:
#             oldest_age = person.compute_age()
#             oldest = person

#     return youngest, oldest

# youngest, oldest = get_young_old(persons)
        

## Task 1.3: f-strings

# Use format strings (`f""`) to `print` a table of all `persons` in the following format.

# The result should look like this: 

# ```
# Name           Year of Birth Age
# --------------------------------
# Bucky Barnes            1917 104
# Steve Rogers            1918 103
# Tony Stark              1976  45
# Bruce Banner            1969  52
# Rhodey Rhodes           1968  53
# Wanda Maximoff          1989  32
# Vision                  2015   6
# Peter Parker            2001  20
# Peter Quill             1980  41
# Monica Rambeau          1984  37
# Carol Danvers           1964  57
# ```

# (It is enough if it looks roughly the same. As an advanced challege, try to make it look exactly the same: The name must be left-aligned, year of birth and age right-aligned.)

def print_persons(persons:list) -> None:
    print('Name             Year of Birth Age')    
    print('----------------------------------')
    for person in persons:
        long_space = " " * (26 - len(person.name))
        short_space = " " * (4 - len(str(person.compute_age())))
        print(f"{person.name}{long_space}{person.year_of_birth}{short_space}{person.compute_age()}")
        # print(str(person.name) + ' ' * (24  - len(person.name)) + str(person.year_of_birth) + ' ' * (4 - len(str(person.compute_age()))) + str(person.compute_age()))

    # for person in persons:
    #     print(f"{person.name:<15} {person.year_of_birth:>12} {person.compute_age():>5}")

print_persons(persons)


# Task 1.4: Filter
# Use a `filter` function call to extract exactly these `Person`(s) out of the `persons` list that are said to be in *Generation X* (born between 1965 and 1979 (inclusive))

# - Store the result in a `list` called `gen_x`.

# Afterwards, try to `print` the resulting list? What happens here and why doesn't it work?

def is_gen_X(person):
    if 1965 <= person.year_of_birth <= 1979:
        return True
    return False

gen_X_people = list(filter(is_gen_X, persons))
print(", ".join(map(str, gen_X_people)))

bucky     = Superhero("Bucky Barnes",   1917, 'Winter Soldier',   50)
steve     = Superhero("Steve Rogers",   1918, 'Captain America', 250)
tony      = Superhero("Tony Stark",     1976, 'Iron-Man',        150)
hulk      = Superhero("Bruce Banner",   1969, 'Hulk',            600)
rhodey    = Superhero("Rhodey Rhodes",  1968, 'War Machine',     100)
wanda     = Superhero("Wanda Maximoff", 1989, 'Scarlett Witch',  900)
vision    = Superhero("Vision",         2015, 'Vision',          850)
spiderman = Superhero("Peter Parker",   2001, 'Spider-Man',      180)
starlord  = Superhero("Peter Quill",    1980, 'Starlord',         10)
photon    = Superhero("Monica Rambeau", 1984, 'Photon',          800)
carol     = Superhero("Carol Danvers",  1964, 'Captain Marvel', 1000)

# For later, we'll add them to a list:
superheroes = [bucky, steve, tony, hulk, rhodey, wanda, vision, spiderman, starlord, photon, carol]

order = [
    (steve, bucky),
    (tony, steve),
    (wanda, vision),
    (vision, rhodey),
    (spiderman, starlord),
    (tony, starlord),
    (hulk, tony),
    (carol, vision),
    (wanda, photon),
    (photon, hulk)
]

for couple in order:
    couple = list(couple)
    couple[0].fight(couple[1])

danny = HealingSuperhero('Danny Rand', 1991, 'Iron Fist', 250)

for superhero in superheroes:
    danny.heal(superhero)

print('Name             Year of Birth Age Allias        Powerlevel')    
print('-----------------------------------------------------------')

for person in superheroes:
    print(f"{person.name:<15} {person.year_of_birth:>12} {person.compute_age():>5} {person.allias:<20}{person.powerlevel:>4}")      