""" PokeTeam class. 

This module consists of the PokeTeam class that checks for
valid team selection input and allows the assignment of team in stack formation 
in the order Charmander -> Bulbasaur -> Squirtle.

Variables: limit """

__author__ = "Javeriya Aanam Nadaf"

from pokemon import Charmander, Bulbasaur, Squirtle
from stack_adt import ArrayStack

class PokeTeam():
    
    limit = 6

    def __init__(self) -> None:
        self.name = None
        self.team = None
        self.battle_mode = None
    
    def __correct_team_given(self, charmanders: int, bulbasaurs: int, squirtles: int) -> bool:
        """ Returns true if the total number of Pokemon is equal to or under the limit given to the
         team and returns False if any of the arguments are negative integers.

         :paramArg1 = number of Charmanders
         :paramArg2 = number of Bulbasaurs
         :paramArg3 = number of Squirtles
         """
        
        total = charmanders + bulbasaurs + squirtles
        if total <= self.limit and total > 0
            return True
        elif charmanders < 0 or bulbasaurs < 0 or squirtles < 0:
            return False

    def __assign_team(self, name:str, charmanders: int, bulbasaurs: int, squirtles:int) -> None:
        """ private method - Adds pokemon objects to stack in the order such that Charmander is on the top 
        of the stack with Squirtle at the bottom.

        :paramArg1 = name of player
        :paramArg2 = number of Charmanders
        :paramArg3 = number of Bulbasaurs
        :paramArg4 = number of Squirtles
        Complexity: best = worst; O(squirtles + bulbasaurs + charmanders)
        """

        self.team = ArrayStack(PokeTeam.limit)

        if self.battle_mode == 0:
            #Initializing the StackArray
            self.team = ArrayStack(PokeTeam.limit)

            if squirtles != 0:
                for _ in range(squirtles):
                    self.team.push(Squirtle())
            
            if bulbasaurs != 0:
                for _ in range(bulbasaurs):
                    self.team.push(Bulbasaur())
            
            if charmanders != 0:
                for _ in range(charmanders):
                    self.team.push(Charmander()) #only one self
                    
        elif self.battle_mode == 1:
            #Initializing the StackArray
            self.team = CircularQueue(PokeTeam.limit)

            if charmanders != 0:
                for _ in range(charmanders):
                    self.team.append(Squirtle())
            
            if bulbasaurs != 0:
                for _ in range(bulbasaurs):
                    self.team.append(Bulbasaur())
            
            if charmanders != 0:
                for _ in range(charmanders):
                    self.team.append(Charmander()) #only one self

    def choose_team(self, name: str, battle_mode: int) -> None:
        """Prompts user to input pokemon selection. Calls __assign_team function 
        if __correct_team_given function returns true.

        :paramArg1 = name of player
        :paramArg2 = battle mode (either 0 or 1)
        
        :raises ValueError = if player chooses more than 6 or any negative values
        """
        self.name = input("Enter Player's name: ")
        
        while True:
            try:
                C_B_S = input("""Trainer {}! Choose your team as C B S 
                              where C is the number of Charmanders
                                    B is the number of Bulbasaurs
                                    S is the number of Squirtles \n""" .format(self.name))
                
                c = int(C_B_S[slice(1)])
                b = int(C_B_S[slice(2,3)])
                s = int(C_B_S[slice(4,5)])
                #Asigning the team with the given input values if values are valid
                if PokeTeam.__correct_team_given(self, c, b, s):
                    PokeTeam.__assign_team(self, name, c, b, s)
                    print("Team assigned -> {}"  .format(self.name))
                    break;
                else:
                    raise ValueError
            except ValueError:
                print("Player can only choose six non - negative pokemons")
                continue
    
    def __str__(self):
        return self.team.__str__()


if __name__=="__main__":
    my_team = PokeTeam()
    my_team.choose_team("FIT2085", 0)
    my_team.choose_team("FIT2085", 1)
    print(my_team)


