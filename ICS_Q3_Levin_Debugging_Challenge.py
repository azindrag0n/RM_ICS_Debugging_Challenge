import random
#Adam Levin

moves = {"tackle": range(18, 26), "pk thunder": range(10, 36), "psi heal": range(10, 20)

class Character:
    "Define our general Character which we base Ness and Starman off of." #The error isn't what the debug says it is.
    def __init__(self, health):
        self.health = health

    def attack(self, other):
        raise NotImplementedError


class Ness(Character):
    "Ness starts with 100 health and have the choice of three moves"
    def __init__(self, health = 100):
        super().__init__(health)

    def attack(self, other):
        while True:
            choice = str.lower(input("What does Ness do? (Tackle, PK Thunder, or PSI Heal)\n"))

            if choice == "psi heal":
                self.health += int(random.choice(moves[choice]))
                print("Ness's health is now {0.health}.\n".format(self))
                break
            if choice == "tackle" or choice == "pk thunder":
                damage = int(random.choice(moves[choice]))
                other.health -= damage
                print("Ness attacks with {0}, dealing {1} damage.\n".format(choice, damage))
                break
            else:
                print("Not a valid move, try again!")


class Starman(Character):
    "The Starman, also starts with 100 health and chooses moves at random"
    def __init__(self, health = 100):
        super().__init__(health)

    def attack(self, other):
        if self.health <= 35:
            #increasing probability of heal when under 35 health
            moves_1 = ["tackle", "pk thunder", "psi heal", "psi heal", "psi heal", "psi heal", "psi heal"]
            computer_choice = random.choice(moves_1)
        else:
            computer_choice = random.choice(list(moves))
        if computer_choice == "tackle" or computer_choice == "pk thunder":
            damage = int(random.choice(moves[computer_choice]))
            other.health -= damage
            print("The Starman attacks with {0}, dealing {1} damage.\n".format(computer_choice, damage))
        if computer_choice == "psi heal":
            self.health += int(random.choice(moves[computer_choice]))
            print("The Starman uses PSI Heal and its health is now {0.health}.\n".format(self))


def battle(ness, starman):
    print("An Starman suddenly attacks!")
    while ness.health > 0 and starman.health > 0:
        ness.attack(starman)
        if starman.health <= 0:
            break
        print("The health of the Starman is now {0.health}.\n".format(starman))
        starman.attack(ness)
        if ness.health <= 0:
            break
        print("Ness's health is now {0.health}.\n".format(ness))
#outcome
    if ness.health > 0:
        print("Ness defeated the Starman!")
    if starman.health > 0:
        print("Ness was defeated by the Starman!")

battle(Ness(), Starman())