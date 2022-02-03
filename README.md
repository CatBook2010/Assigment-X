Assignment X
This is Assignment X (between Assignments 3 and 4). There will not be a Quiz regarding this assignment. However, the concepts of Object-Orientation and the methods and approaches used in this assignment will be present in future Assignments and Quizzes.

Please read the task description carefully and implement only what the tasks wants you to implement. Follow the instructions from the task description. There might be tasks that require you to write things you would do differently but you have to stay with the description. The test cases below each input cell is the gold standard. Because of the variability of different possible implementations, there will not be a test case for each task.

Try to implement the tasks yourself or in a small group. If you blindly copy a solution from the internet or other students, you will not learn anything from it. Understand the solution! This takes practice.

This assignment expects you to transfer knowledge from the lecture. There might be tasks where you have to read and investigate the Python Standard Library to find the documentation for a function that is used or that you want to use.

For any given task, all in Python included modules are "allowed" to use. No task requires you to install a third-party module.

Do not modify the test cells, by doing so you cheat your solution which is not helpful for your learning process.

Task 1: Using a class
The following class Person will be used throughout this whole assingment.

Read and understand what this class represents and which instance methods it provides.

 
# We define following class `Person`.

# Do not change this cell but you have to run it to have
# the Person class in scope.

class Person:
    """
    This is a Person class.
    Each person has a name (str) and a year_of_birth (int).
    Also, each instance of a Person can compute their own age
    by calling .compute_age().
    Printing a person is done calling the __str__ method: we want
    the name of the person followed by their age in parentheses.
    """
    def __init__(self, name, year_of_birth):
        """
        Constructor: We have to set the name and year_of_birth.

        name: str
        year_of_birth: int
        """
        self.name = name
        self.year_of_birth = year_of_birth

    def compute_age(self):
        """
        We compute the age of a person by subtracting their
        year of birth from 2021.
        """
        return 2021 - self.year_of_birth

    def __str__(self):
        """
        We use a format string to return the Person converted to a string
        in the following format: "Name (Age)"
        Example:
            str(Person("Guido van Rossum", 1956))
            >>> "Guido van Rossum (65)"
        """
        return f"{self.name} ({self.compute_age()})"
Task 1.1
Use the given Person class to instantantiate a list named persons with the following persons:

Bucky Barnes, born 1917
Steve Rogers, born 1918
Tony Stark, born 1976
Bruce Banner, born 1969
Rhodey Rhodes, born 1968
Wanda Maximoff, born 1989
Vision, born 2015
Peter Parker, born 2001
Peter Quill, born 1980
Monica Rambeau, born 1984
Carol Danvers, born 1964
 
# Add your code here:

 
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


  Success! Your code works as intended.  

Task 1.2: Minimum and Maximum
Find the youngest and oldest person in the given list. Save them in the variables youngest and oldest. Save the actual instance of the person in the variable and not just a string.

Hint: The easiest solution is using a for loop. However, you could use the min and max functions with a self-defined lambda function as comparator.

 
# Add your code here:


 
# Test Cell. Do not modify
from unittest import TestCase
__ = TestCase()

# The youngest one is Vision:
__.assertEqual(str(youngest), "Vision (6)")

# The oldest is Bucky Barnes
__.assertEqual(str(oldest), "Bucky Barnes (104)")

print("\n\033[37;42;2m  Success! Your code works as intended.  \033[0m\n")


  Success! Your code works as intended.  

Task 1.3: f-strings
Use format strings (f"") to print a table of all persons in the following format.

The result should look like this: (there is no test case)

Name           Year of Birth Age
--------------------------------
Bucky Barnes            1917 104
Steve Rogers            1918 103
Tony Stark              1976  45
Bruce Banner            1969  52
Rhodey Rhodes           1968  53
Wanda Maximoff          1989  32
Vision                  2015   6
Peter Parker            2001  20
Peter Quill             1980  41
Monica Rambeau          1984  37
Carol Danvers           1964  57
(It is enough if it looks roughly the same. As an advanced challege, try to make it look exactly the same: The name must be left-aligned, year of birth and age right-aligned.)

 
# Add your code here:



Name           Year of Birth   Age
----------------------------------
Bucky Barnes            1917   104
Steve Rogers            1918   103
Tony Stark              1976    45
Bruce Banner            1969    52
Rhodey Rhodes           1968    53
Wanda Maximoff          1989    32
Vision                  2015     6
Peter Parker            2001    20
Peter Quill             1980    41
Monica Rambeau          1984    37
Carol Danvers           1964    57
Task 1.4: Filter
Use a filter function call to extract exactly these Person(s) out of the persons list that are said to be in Generation X (born between 1965 and 1979 (inclusive))

Store the result in a list called gen_x.
Afterwards, try to print the resulting list? What happens here and why doesn't it work?

 
# Add your code here:


 
# Test code, don't modify
from unittest import TestCase
__ = TestCase()

__.assertEqual(set(map(str, gen_x)), {'Tony Stark (45)', 'Rhodey Rhodes (53)', 'Bruce Banner (52)'})

print("\n\033[37;42;2m  Success! Your code works as intended.  \033[0m\n")


  Success! Your code works as intended.  

 
# Try to understand the output: Why can't we see the nicely formatted Person objects?
print(gen_x)

[<__main__.Person object at 0x7f819f305ad0>, <__main__.Person object at 0x7f819f305c10>, <__main__.Person object at 0x7f819f3058d0>]
Task 2: Superheroes
Apart from being a Person, we can have Superheroes.

Task 2.1: The Class Superhero
Your task is to define a new class called Superhero that inherits from the Person class but has the additional required instance variables alias (the superhero name as a str) and a powerlevel (int).

Task 2.2 The dunder methods: __str__ and __repr__
Implement the __str__ instance method of the Superhero class that prints the alias and the powerlevel. If the powerlevel is smaller or equal to 0, it must use DEFEATED instead of the integer value.

Example:

print(hulk) 
>>> "Hulk: 600"
or when powerlevel ≤ 0:

print(hulk) 
>>> "Hulk: DEFEATED"
In the __repr__ instance method, add to the string the other information of the Superhero from the superclass (name and age). Do not duplicate the code from the Person class but call the actual __str__ method of the superclass.

hulk
>>> "Hulk: 600 (Bruce Banner (52))"
or when powerlevel ≤ 0:

hulk
>>> "Hulk: DEFEATED (Bruce Banner (52))"
Task 2.3: The .fight() instance method
A superhero in addtion has the ability to fight another superhero: this is modelled by the instance method fight(self, enemy). The argument enemy is an instance of Superhero.

A fight is modeled by subtracting half the powerlevels from one another (use integer divison //). A powerlevel can't be lower than 0. So if the incoming damage is too high, set it to 0 anyway.

When Hulk fights Vision: Hulk has a current powerlevel of 600. Vision has a current powerlevel of 850. We subtract 600//2 from Vision's powerlevel and 850//2 from Hulks powerlevel.

Meaning the new powerlevel of Hulk is 175 and Vision's will be 525.

(Use the current powerlevel to compute the difference and be careful not to subtract the already subtracted result.)

Task 2.4: The Fight
Read below to let the instantiated superheroes fight.

After each fight, print the result, meaning calling the __str__ function of the involved superheroes implicitly (either with str() or a f-string).

It should look similar to this:

Fight between Scarlett Witch and Iron-Man:
     Scarlett Witch: 825 
     Iron-Man: DEFEATED
 
# Add your code here:


The Fight

Steve fights Bucky
Tony fights Steve
Wanda fights Vision
Vision fights Rhodey
Spiderman fights Starlord
Tony fights Starlord
Hulk fights Tony
Carol fights Vision
Wanda fights Photon.
Photon fights Hulk.
Note, that after each call to .fight(), the powerlevel of both heroes changes. Run the cell below to reset the instances.

After the fight, print all 'DEFEATED' heroes by using the repr() function.

 
# We instantiate a few heros (Don't modify this cell.)
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
 
# Add your code here:


Fight between Captain America and Winter Soldier:
	 Captain America: 225 
	 Winter Soldier: DEFEATED

Fight between Iron-Man and Captain America:
	 Iron-Man: 38 
	 Captain America: 150

Fight between Scarlett Witch and Vision:
	 Scarlett Witch: 475 
	 Vision: 400

Fight between Vision and War Machine:
	 Vision: 350 
	 War Machine: DEFEATED

Fight between Spider-Man and Starlord:
	 Spider-Man: 175 
	 Starlord: DEFEATED

Fight between Iron-Man and Starlord:
	 Iron-Man: 38 
	 Starlord: DEFEATED

Fight between Hulk and Iron-Man:
	 Hulk: 581 
	 Iron-Man: DEFEATED

Fight between Captain Marvel and Vision:
	 Captain Marvel: 825 
	 Vision: DEFEATED

Fight between Scarlett Witch and Photon:
	 Scarlett Witch: 75 
	 Photon: 563

Fight between Photon and Hulk:
	 Photon: 273 
	 Hulk: 300

 
print("Fallen Heroes:\n")

# Add your code here:


Fallen Heroes:

Winter Soldier: DEFEATED (Bucky Barnes (104))
Iron-Man: DEFEATED (Tony Stark (45))
War Machine: DEFEATED (Rhodey Rhodes (53))
Vision: DEFEATED (Vision (6))
Starlord: DEFEATED (Peter Quill (41))
Task 2.5:
Now, there is Iron Fist, who is able to heal others with his power.

We model this by again inherting from Superhero and calling the new class HealingSuperhero. They have an additional .heal() instance method that receives another Superhero and similar to the .fight() method, adds their own powerlevel to the other hero.

Define the class HealingSuperhero with the additional instance method .heal(self, other)
Create a variable danny and instantiate a new HealingSuperhero. His civial name is "Danny Rand", he is born on April 1st, 1991, and has a powerlevel of 250.
Use his additional power to heal all other superheroes. (In the Marvel Universe(s) nobody ever dies.)
 
# Add your code here:


 
for superhero in superheroes:
    print(superhero)

Winter Soldier: 250
Captain America: 400
Iron-Man: 250
Hulk: 550
War Machine: 250
Scarlett Witch: 325
Vision: 250
Spider-Man: 425
Starlord: 250
Photon: 523
Captain Marvel: 1075
When you look at the values of all heroes, the following result must be present:

Name           Year of Birth Age Alias           Powerlevel
-----------------------------------------------------------
Bucky Barnes            1917 104 Winter Soldier         250
Steve Rogers            1918 103 Captain America        400
Tony Stark              1976  45 Iron-Man               250
Bruce Banner            1969  52 Hulk                   568
Rhodey Rhodes           1968  53 War Machine            250
Wanda Maximoff          1989  32 Scarlett Witch         250
Vision                  2015   6 Vision                 250
Peter Parker            2001  20 Spider-Man             425
Peter Quill             1980  41 Starlord               250
Monica Rambeau          1984  37 Photon                 486
Carol Danvers           1964  57 Captain Marvel        1075
Danny Rand              1991  30 Iron Fist              250`