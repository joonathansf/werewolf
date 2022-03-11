class Player:

    def __init__(self, pseudo="player"):
        self.name = pseudo
        self.alive = True
        print(pseudo, "a rejoint la partie !")

    def action(self):
        pass

    def reveil(self):
        pass

    def is_alive(self):
        return self.alive

    def kill(self):
        self.alive = False

    def present(self):
        print(self.name, "est mort et son rôle était :", __class__.__name__, ".")
