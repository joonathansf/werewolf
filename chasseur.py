from personnage import Player


class Chasseur(Player):
    def __init__(self, joueurs, pseudo="player"):
        super().__init__(pseudo)
        self.joueurs = joueurs
        self.gunLoad = True

    def action(self):
        pass

    def kill(self):
        self.alive = False

    def killPlayer(self):
        print("Chasseur :", self.name)
        print("Voici les joueurs : ", end="")
        for joueur in self.joueurs:
            if (joueur.name != self.name):
                print(joueur.name, end=" ")
        print("")
        valid = False
        while not valid:
            valid = False
            nom = input("Qui souhaitez vous tuer ? : ")
            for joueur in self.joueurs:
                if (joueur.name == nom):
                    joueur.kill()
                    joueur.present()
                    valid = True
		

    def reveil(self):
        if self.alive == False:
            self.present()
        else:
            pass

    def present(self):
        print(self.name, "est mort et son rôle était :", __class__.__name__)
        if self.gunLoad:
            self.killPlayer()
            self.gunLoad = False
        if self in self.joueurs:
            self.joueurs.remove(self)
