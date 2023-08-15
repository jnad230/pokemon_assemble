""" Pokemon classes. 

This module consists of the Charmaner, Bulbasaur, Squirtle pokemon 
classes that implement the abstract methods defined in PokemonBase.

"""

__author__ = "Javeriya Aanam Nadaf"

from pokemon_base import PokemonBase

class Charmander:
    DEFENCE_CHAR = 4
    CLASS_EFFECTIVENESS = {"WATER": 0.5,
                            "GRASS": 2,
                            "FIRE": 1}

    def __init__(self):
            PokemonBase.__init__(self, 7, "FIRE")

    def __str__():
        """ Magic string method that prints out the pokemons stats
         after retrieving them from PokemonBase.""" 
        return str(PokemonBase.get_poke_name()) + "'s health = " + str(PokemonBase.hp) + " and level = " + str(PokemonBase.level)
    
    def get_speed(self):
        return 8 + self.level

    def get_defence(self):
        return self.DEFENCE_CHAR

    def get_attack_damage(self):
        return 6 + self.level
    
class Bulbasaur:
    DEFENCE_CHAR = 5
    ATTACK_BULB = 5
    CLASS_EFFECTIVENESS = {"WATER": 2,
                            "GRASS": 1,
                            "FIRE": 0.5}    
    
    def __init__(self):
            PokemonBase.__init__(self, 9, "GRASS")

    def __str__(self):
         """ Magic string method that prints out the pokemons stats
         after retrieving them from PokemonBase.""" 
        return str(self.get_poke_name()) + "'s health = " + str(self.hp) + " and level = " + str(self.level)
    
    def get_speed(self):
        return 7 + self.level//2

    def get_defence(self):
        return self.DEFENCE_CHAR

    def get_attack_damage(self):
        return self.ATTACK_BULB

class Squirtle:
    SPEED_SQUIRTLE = 7
    CLASS_EFFECTIVENESS = {"WATER": 1,
                            "GRASS": 0.5,
                            "FIRE": 2}
    
    def __init__(self):
            PokemonBase.__init__(self, 8, "WATER")

    def __str__(self):
        """ Magic string method that prints out the pokemons stats
         after retrieving them from PokemonBase."""
        return str(self.get_poke_name()) + "'s health = " + str(self.hp) + " and level = " + str(self.level)
    
    def get_speed(self):
        return self.SPEED_SQUIRTLE

    def get_defence(self):
        return 6 + self.level

    def get_attack_damage(self):
        return 4 + self.level//2


