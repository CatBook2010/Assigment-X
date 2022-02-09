from Superhero import Superhero

class HealingSuperhero(Superhero):

    def heal(self, other: Superhero):
        other.powerlevel += self.powerlevel
