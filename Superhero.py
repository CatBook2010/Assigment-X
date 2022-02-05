from Person import Person

class Superhero(Person):
    def __init__(self, name, year_of_birth, allias: str, powerlevel: int):

        super().__init__(name, year_of_birth)
        self.allias = allias
        self.powerlevel = powerlevel

    def __str__(self):
        # if self.powerlevel > 0:
        #     return f"{self.allias}"
        # else:
        #     return f"{self.allias} DEFEATED"

        return f"{self.allias} {self.powerlevel if self.powerlevel > 0 else 'DEFEATED'}"

    def __repr__(self):
        return f"{self} ({super().__str__()})"

## Task 2.3: The `.fight()` instance method
# A superhero in addtion has the ability to fight another superhero: this is modelled by the instance method `fight(self, enemy)`. The argument `enemy` is an instance of `Superhero`.

# A fight is modeled by subtracting **half** the powerlevels from one another (use integer divison //). A powerlevel can't be lower than 0. So if the incoming damage is too high, set it to 0 anyway.

# When _Hulk_ fights _Vision_:
# Hulk has a current powerlevel of 600.
# Vision has a current powerlevel of 850.
# We subtract 600//2 from Vision's powerlevel and 850//2 from Hulks powerlevel.

# Meaning the new powerlevel of Hulk is 175 and Vision's will be 525.

# (Use the *current* powerlevel to compute the difference and be careful **not** to subtract the already subtracted result.)






# ## Task 2.4: The Fight
# Read below to let the instantiated superheroes fight.

# After each fight, print the result, meaning calling the `__str__` function of the involved superheroes **implicitly** (either with `str()` or a f-string).

# It should look similar to this:
# ```
# Fight between Scarlett Witch and Iron-Man:
# 	 Scarlett Witch: 825 
# 	 Iron-Man: DEFEATED
# ```








# ---
## Task 2.5:

# Now, there is **Iron Fist**, who is able to heal others with his power.

# We model this by again inherting from `Superhero` and calling the new class `HealingSuperhero`. They have an additional `.heal()` instance method that receives another `Superhero` and similar to the `.fight()` method, adds their own powerlevel to the other hero.

# - Define the class `HealingSuperhero` with the additional instance method `.heal(self, other)`
# - Create a variable `danny` and instantiate a new `HealingSuperhero`. His civial name is "Danny Rand", he is born on April 1st, 1991, and has a powerlevel of 250.
# - Use his additional power to heal all other superheroes. (In the Marvel Universe(s) nobody ever dies.)




# When you look at the values of all heroes, the following result must be present:
# ```
# Name           Year of Birth Age Alias           Powerlevel
# -----------------------------------------------------------
# Bucky Barnes            1917 104 Winter Soldier         250
# Steve Rogers            1918 103 Captain America        400
# Tony Stark              1976  45 Iron-Man               250
# Bruce Banner            1969  52 Hulk                   568
# Rhodey Rhodes           1968  53 War Machine            250
# Wanda Maximoff          1989  32 Scarlett Witch         250
# Vision                  2015   6 Vision                 250
# Peter Parker            2001  20 Spider-Man             425
# Peter Quill             1980  41 Starlord               250
# Monica Rambeau          1984  37 Photon                 486
# Carol Danvers           1964  57 Captain Marvel        1075
# Danny Rand              1991  30 Iron Fist              250
# ```
