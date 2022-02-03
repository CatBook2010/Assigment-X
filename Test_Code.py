# Test Case; Do not modify.
from unittest import TestCase
__ = TestCase()

# Test if `persons` is a list.
__.assertIsInstance(persons, list, msg='The `persons` variable is not a list.')

# Test if all elements in the list are persons
__.assertTrue(all(isinstance(p, Person) for p in persons), msg='At least one entry in `persons` is not a Person.')

# Check for equality
# We're using a set because our order might be different from yours.
__.assertEqual(
    set(map(str, persons)),
    {'Steve Rogers (103)', 'Bucky Barnes (104)', 'Peter Parker (20)', 'Peter Quill (41)', 'Monica Rambeau (37)', 'Rhodey Rhodes (53)', 'Carol Danvers (57)', 'Tony Stark (45)', 'Wanda Maximoff (32)', 'Bruce Banner (52)', 'Vision (6)'},
    msg="The two lists differ."
)

print("\n\033[37;42;2m  Success! Your code works as intended.  \033[0m\n")

# Test Cell. Do not modify
from unittest import TestCase
__ = TestCase()

# The youngest one is Vision:
__.assertEqual(str(youngest), "Vision (6)")

# The oldest is Bucky Barnes
__.assertEqual(str(oldest), "Bucky Barnes (104)")

print("\n\033[37;42;2m  Success! Your code works as intended.  \033[0m\n")

# Test code, don't modify
from unittest import TestCase
__ = TestCase()

__.assertEqual(set(map(str, gen_x)), {'Tony Stark (45)', 'Rhodey Rhodes (53)', 'Bruce Banner (52)'})

print("\n\033[37;42;2m  Success! Your code works as intended.  \033[0m\n")

