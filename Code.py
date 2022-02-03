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