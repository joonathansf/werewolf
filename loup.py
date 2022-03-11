from personnage import Player


class Loup(Player):

    def __init__(self, joueurs, loups, pseudo="player"):
        super().__init__(pseudo)
        self.loups = loups
        self.joueurs = joueurs
        self.v = False

    def vote(self):
        print("Loup :", self.name)
        print("Voici les joueurs non loups : ", end="")
        for joueur in self.joueurs:
            if (joueur not in self.loups):
                print(joueur.name, end=" ")
        print("")
        valid = False
        while not valid:
            valid = False
            nom = input("Qui souhaitez vous tuer ? : ")
            for joueur in self.joueurs:
                if joueur.name == nom:
                    valid = True
        print("-" * 40)
        self.v = True
        return nom

    def action(self):
        k = {}
        for e in self.joueurs:
            k[e.name] = 0
        if not self.v:
            for l in self.loups:
                if (l.alive):
                    s = l.vote()
                    k[s] = k[s] + 1

        max = 0
        max_n = ""
        for e in k:
            if k[e] > max:
                max = k[e]
                max_n = e
        for e in self.joueurs:
            if e.name == max_n:
                e.kill()

    def reveil(self):
        self.v = False

    def present(self):
        print(self.name, "est mort et son rôle était :", __class__.__name__)
        self.joueurs.remove(self)
