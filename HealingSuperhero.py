from Superhero import Superhero

class HealingSuperhero(Superhero):
    def heal(self, other):
        other.powerlevel += self.powerlevel // 2
        self.powerlevel -= self.powerlevel // 2
