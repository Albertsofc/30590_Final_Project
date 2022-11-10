class Player:
    """
    This class represents a player playing the text adventure.
    He has an inventory of a list containing item and a weapon slot with an
    ammo pouch.
    """
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.weapon = None
        self.ammo_pouch = 0

    def add_inventory(self, item):
        self.inventory.append(item)

    def assign_weapon(self, weapon):
        self.weapon = weapon

    def add_ammo(self, quantity):
        self.ammo_pouch += quantity


class Pistol:
    """
    This class is a pistol. It can shoot or reload.
    It has a defined magazine size and has ammo in each magazine.
    """
    def __init__(self, magazine, ammo):
        self.magazine = magazine
        self.ammo = ammo

    def shoot(self):
        if self.ammo > 0:
            self.ammo -= 1

    def reload(self, player):
        while self.ammo < self.magazine and player.ammo_pouch > 0:
            player.ammo_pouch -= 1
            self.ammo += 1


if __name__ == '__main__':
    p1 = Player("Ricardo")
    p1.add_ammo(1)
    g1 = Pistol(6, 6)
    g1.reload(p1)
    print("Ammo in gun")
    print(g1.ammo)
    print("Ammo in pouch")
    print(p1.ammo_pouch)
