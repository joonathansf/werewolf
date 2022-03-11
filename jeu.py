from chasseur import Chasseur
from loup import Loup
from personnage import Player
from voyante import Voyante

from villageois import Villageois


class Jeux:
    def main(self=False):
        print("Début de la partie.")
        joueurs = []
        jonathan = Villageois(joueurs, "jonathan")
        youness = Villageois(joueurs, "youness")
        joueurs.append(jonathan)
        joueurs.append(youness)
        loups = []
        rami = Loup(joueurs, loups, "rami")
        hamza = Loup(joueurs, loups, "hamza")
        yassine = Voyante(joueurs, "yassine")
        hany = Chasseur(joueurs, "hany")
        joueurs.append(rami)
        joueurs.append(hamza)
        joueurs.append(hany)
        loups.append(rami)
        loups.append(hamza)
        joueurs.append(yassine)
        print("-" * 40)
        while self.alive(joueurs) > (self.alive(loups) * 2) and self.alive(loups) > 0:
            print("\nLe village s'endort\n")
            for joueur in joueurs:
                joueur.action()
            print("\nLe village se réveille\n")
            for joueur in joueurs:
                joueur.reveil()
            self.vote(joueurs, loups)
        print("Fin de partie")
        if (self.alive(joueurs) <= (self.alive(loups) * 2)) and self.alive(loups) > 0:
            print("Victoire des loups !")
        else:
            print("Victoire des villageois !")

    def alive(self, joueurs):
        i = 0
        for e in joueurs:
            if e.is_alive():
                i = i + 1
        return i

    def vote(self, joueurs, loups):
        if (self.alive(joueurs) <= (self.alive(loups) * 2)) or self.alive(loups) <= 0:
            return
        votes = {}
        print("-" * 40)
        print("\nDébut du vote, voici les joueurs en vie : ", end="")
        for e in joueurs:
            votes[e.name] = 0
            print(e.name, end=" ")
        print("")
        for e in joueurs:
            if e.is_alive():
                print("C'est au tour de", e.name, "de voter")
                valid = False
                while not valid:
                    valid = False
                    j = input("Choix : ")
                    for e in joueurs:
                        if e.is_alive() and e.name == j:
                            valid = True
                votes[j] = votes[j] + 1

        max = 0
        max_n = ""
        for e in votes:
            if votes[e] > max:
                max = votes[e]
                max_n = e
        for e in joueurs:
            if e.name == max_n:
                e.kill()
                e.present()
