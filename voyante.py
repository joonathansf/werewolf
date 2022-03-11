from personnage import Player


class Voyante(Player):
    def __init__(self, joueurs, pseudo="player"):
        super().__init__(pseudo)
        self.joueurs = joueurs

    def action(self):
        print("Voyante :", self.name)
        print("Voici les joueurs : ", end="")
        for joueur in self.joueurs:
            if (joueur.name != self.name):
                print(joueur.name, end=" ")
        print("")
        valid = False
        while not valid:
            valid = False
            nom = input("Quel rôle souhaitez vous voir ? : ")
            for joueur in self.joueurs:
                if (joueur.name == nom):
                    print(joueur.name, "est", type(joueur).__name__)
                    valid = True
        print("-" * 40)

    def kill(self):
        self.alive = False

    def reveil(self):
        if self.alive == False:
            self.present()

    def present(self):
        print(self.name, "est mort et son rôle était :", __class__.__name__)
        if self in self.joueurs:
            self.joueurs.remove(self)
