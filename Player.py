# CLI Adventure Game - Marshall Ferguson - 6/2020

from Character import Character

class Player(Character):
    def __init__(self, gold, inventory):
        self.gold = gold
        self.inventory = inventory