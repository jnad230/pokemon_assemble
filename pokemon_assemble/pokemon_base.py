""" Abstract class. 

This module consists of the edited pokemon_base file to contain the abstract class
called PokemonBase which will form the basis abstract class of all of the upcoming classses as required.

Variables: hp, level, poke_class. """

__author__ = "Javeriya Aanam Nadaf"

from abc import abstractclassmethod, abstractmethod

class PokemonBase:

    BASE_LEVEL = 1

    def __init__(self, hp: int, poke_class: str) -> None:
        """ Initializes health of a pokemon and poke_class of a pokemon.

        :param arg1: health power of a pokemon
        :param arg2: the class type of a pokemon
        :raises ValueError: if the hp is less than 
        :raises TypeError: if the type class string is not a valid class
        """

        self.level = PokemonBase.BASE_LEVEL

        if hp <0:
            raise ValueError ("hp should be a non zero positive value")
        else:
            self.hp = hp

        self.classes = ["GRASS","FIRE","WATER"]
        
        if poke_class in self.classes:
            self.poke_class = poke_class
        else: 
            raise TypeError("Please enter a valid pokeman class to battle")

    def get_hp(self) -> int:
        return self.hp

    def get_level(self) -> int:
        return self.level

    def get_poke_class(self) -> str:
        return self.poke_class

    def is_fainted(self) -> bool:
        if self.hp <= 0:
            return True

    def level_up(self) -> None:
        self.level = self.level + 1
    
    @abstractclassmethod
    def get_speed(self) -> int:
        #returns the pokemons speed
        pass

    @abstractclassmethod
    def get_attack_damage(self) -> int:
        #returns the attack damage stat
        pass
    
    @abstractclassmethod
    def get_defence(self) -> int:
        #returns the defence stat of the pokemon
        pass

    def defend(self, damage: int) -> None:
        #Evaluates the damage after being attacked expression and then changes hp accordingly. By precondition, damage must be ≥ 0.
        """
        Evaluates the damage after being attacked 
        expression and then changes hp accordingly for each class. 
        By precondition, damage must be ≥ 0.

        :paramArg1 = damage to pokemon caused in battle 
        :raises ValueError: if the damage is negative
        """

        if damage >= 0:
            if self.poke_class == "FIRE":
                if damage > self.get_defence():
                    self.hp = self.hp - damage
                else: 
                    self.hp = self.hp - damage//2
            elif self.poke_class == "GRASS":
                if damage > self.get_defence() + 5:
                    self.hp = self.hp - damage
                else:
                    self.hp = self.hp - damage//2
            else: 
                if damage > self.get_defence()*2:
                    self.hp = self.hp - damage
                else:
                    self.hp = self.hp - damage//2
        else:
           raise ValueError ("Damage cannot be negative")

    def get_poke_name(self) -> str:

        return PokemonBase.__class__.__name__ 

    @abstractmethod
    def __str__(self):
        pass
