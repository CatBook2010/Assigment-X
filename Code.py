from Person import Person

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

# def get_young_old(persons: list):
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

