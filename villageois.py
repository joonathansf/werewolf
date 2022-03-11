from personnage import Player


class Villageois(Player):

    def __init__(self, joueurs, pseudo="player"):
        super().__init__(pseudo)
        self.joueurs = joueurs

    def action(self):
        pass

    def present(self):
        print(self.name, "est mort et son rôle était :", __class__.__name__)
        if self in self.joueurs:
            self.joueurs.remove(self)

    def reveil(self):
        if self.alive == False:
            self.present()
