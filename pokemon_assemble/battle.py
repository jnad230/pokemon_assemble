""" Battle class. 

This module consists of the Battle class that reads in and creates a team for each player.
It then executes combat battle as per the battle_mode specified.

"""

__author__ = "Javeriya Aanam Nadaf"

from poke_team import PokeTeam
from stack_adt import ArrayStack
from queue_adt import CircularQueue

class Battle:
    
    def rotating_mode_battle(self, player_one: str, player_two: str) -> int:
        """
            Creates a team for each player in queue formation and calls method __conduct_combat
             which then returns the winner.

             :paramArg1 = player one name
             :paramArg2 = player two name
        """
        
        t1 = PokeTeam()
        t2 = PokeTeam()

        battle_mode = 1
        t1.battle_mode = battle_mode
        t2.battle_mode = battle_mode
        t1._PokeTeam__assign_team(player_one, 3, 2, 1)
        t2._PokeTeam__assign_team(player_two, 3, 2, 1)
        # battle._Battle__conduct_combat(t1, t2, battle_mode) == 0
        self.__conduct_combat(t1, t2, battle_mode)

    def set_mode_battle(self, player_one: str, player_two: str) -> int:
        """
            Creates a team for each player in stack formation and calls method __conduct_combat
             which then returns the winner.

             :paramArg1 = player one name
             :paramArg2 = player two name
        """
        
        t1 = PokeTeam()
        t2 = PokeTeam()

        battle_mode = 0
        t1.battle_mode = battle_mode
        t2.battle_mode = battle_mode
        t1._PokeTeam__assign_team(player_two, 3, 2, 1)
        t2._PokeTeam__assign_team(player_two, 3, 2, 1)
        # battle._Battle__conduct_combat(t1, t2, battle_mode) == 0
        self.__conduct_combat(t1, t2, battle_mode)

    def __conduct_combat(self, team1: PokeTeam, team2: PokeTeam, battle_mode: int) -> int:
         """
            Creates a team for each player in stack or queue formation according to the battle mode
            and calls method __conduct_combat which then returns the winner.

             :paramArg1 = player one name
             :paramArg2 = player two name
             :Complexity = Best = O(1) when each team has only one pokemon  
                           Worst = O(n) where n is the number of battle rounds
        """

        if battle_mode == 0:
            u1 = team1._ArrayStack_.pop()
            u2 = team2._ArrayStack_.pop()
        elif battle_mode == 1:
            u1 = team1._CircularQueue_.serve()
            u2 = team2._CircularQueue_.serve()

        while not team1.is_empty() or not team2.is_empty():
            if u1.get_speed() > u2.get_speed():

                u1Attack = u1.get_attack_damage()  #retrieves the attack damage stat of both the pokemons with equal speed

                if u1.get_poke_name() == "Charmander" and u2.get_poke_name() == "Charmander":
                    effective_C = u1.pokeman.CLASS_EFFECTIVENESS["FIRE"]  #retrieves the damage multiplied with the type effectiveness
                    damage = u1Attack*effective_C
                    u2.defend(damage)

                elif u1.get_poke_name() == "Charmander" and u2.get_poke_name() == "Bulbasaur":
                    effective_B = u1.pokeman.CLASS_EFFECTIVENESS["GRASS"]
                    damage = u1Attack*effective_B
                    u2.defend(damage)

                elif u1.get_poke_name() == "Charmander" and u2.get_poke_name() == "Squirtle":
                    effective_S = u1.pokeman.CLASS_EFFECTIVENESS["WATER"]
                    damage = u1Attack*effective_S
                    u2.defend(damage)

                elif u1.get_poke_name() == "Bulbasaur" and u2.get_poke_name() == "Bulbasaur":
                    effective_B = u1.pokeman.CLASS_EFFECTIVENESS["GRASS"]
                    damage = u1Attack*effective_B
                    u2.defend(damage)

                elif u1.get_poke_name() == "Bulbasaur" and u2.get_poke_name() == "Squirtle":
                    effective_S = u1.pokeman.CLASS_EFFECTIVENESS["WATER"]
                    damage = u1Attack*effective_S
                    u2.defend(damage)

                elif u1.get_poke_name() == "Bulbasaur" and u2.get_poke_name() == "Charmander":
                    effective_C = u1.pokeman.CLASS_EFFECTIVENESS["FIRE"]
                    damage = u1Attack*effective_C
                    u2.defend(damage)

                elif u1.get_poke_name() == "Squirtle" and u2.get_poke_name() == "Squirtle":
                    effective_S = u1.pokeman.CLASS_EFFECTIVENESS["WATER"]
                    damage = u1Attack*effective_S
                    u2.defend(damage)

                elif u1.get_poke_name() == "Squirtle" and u2.get_poke_name() == "Bulbasaur":
                    effective_B = u1.pokeman.CLASS_EFFECTIVENESS["GRASS"]
                    damage = u1Attack*effective_B
                    u2.defend(damage)

                elif u1.get_poke_name() == "Squirtle" and u2.get_poke_name() == "Charmander":
                    effective_C = u1.pokeman.CLASS_EFFECTIVENESS["FIRE"]
                    damage = u1Attack*effective_C
                    u2.defend(damage)

            elif u2.get_speed() > u1.get_speed:

                u2Attack = u2.get_attack_damage()   #retrieves the attack damage stat of both the pokemons with equal speed
                
                if u2.get_poke_name() == "Charmander" and u2.get_poke_name() == "Charmander":
                    effective_C = u2.pokeman.CLASS_EFFECTIVENESS["FIRE"]   #retrieves the damage multiplied with the type effectiveness
                    damage = u2Attack*effective_C
                    u1.defend(damage)

                elif u2.get_poke_name() == "Charmander" and u2.get_poke_name() == "Bulbasaur":
                    effective_B = u2.pokeman.CLASS_EFFECTIVENESS["GRASS"]
                    damage = u2Attack*effective_B
                    u1.defend(damage)

                elif u2.get_poke_name() == "Charmander" and u2.get_poke_name() == "Squirtle":
                    effective_S = u2.pokeman.CLASS_EFFECTIVENESS["WATER"]
                    damage = u2Attack*effective_S
                    u1.defend(damage)

                elif u2.get_poke_name() == "Bulbasaur" and u2.get_poke_name() == "Bulbasaur":
                    effective_B = u2.pokeman.CLASS_EFFECTIVENESS["GRASS"]
                    damage = u2Attack*effective_B
                    u1.defend(damage)
                    
                elif u2.get_poke_name() == "Bulbasaur" and u2.get_poke_name() == "Squirtle":
                    effective_S = u2.pokeman.CLASS_EFFECTIVENESS["WATER"]
                    damage = u2Attack*effective_S
                    u1.defend(damage)

                elif u2.get_poke_name() == "Bulbasaur" and u2.get_poke_name() == "Charmander":
                    effective_C = u2.pokeman.CLASS_EFFECTIVENESS["FIRE"]
                    damage = u2Attack*effective_C
                    u1.defend(damage)

                elif u2.get_poke_name() == "Squirtle" and u2.get_poke_name() == "Squirtle":
                    effective_S = u2.pokeman.CLASS_EFFECTIVENESS["WATER"]
                    damage = u2Attack*effective_S
                    u1.defend(damage)

                elif u2.get_poke_name() == "Squirtle" and u2.get_poke_name() == "Bulbasaur":
                    effective_B = u2.pokeman.CLASS_EFFECTIVENESS["GRASS"]
                    damage = u2Attack*effective_B
                    u1.defend(damage)

                elif u2.get_poke_name() == "Squirtle" and u2.get_poke_name() == "Charmander":
                    effective_C = u2.pokeman.CLASS_EFFECTIVENESS["FIRE"]
                    damage = u2Attack*effective_C
                    u1.defend(damage)
            else:
                
                u1Attack = u1.get_attack_damage()   #retrieves the attack damage stat of both the pokemons with equal speed
                u2Attack = u2.get_attack_damage()

                if u1.get_poke_name() == "Charmander" and u2.get_poke_name() == "Charmander":
                    effective_C = u1.pokeman.CLASS_EFFECTIVENESS["FIRE"]   #retrieves the damage multiplied with the type effectiveness
                    damage = u1Attack*effective_C
                    u2.defend(damage)

                    effective_C = u2.pokeman.CLASS_EFFECTIVENESS["FIRE"]
                    damage = u2Attack*effective_C
                    u1.defend(damage)

                elif u1.get_poke_name() == "Charmander" and u2.get_poke_name() == "Bulbasaur":
                    effective_B = u1.pokeman.CLASS_EFFECTIVENESS["GRASS"]
                    damage = u1Attack*effective_B
                    u2.defend(damage)
                
                    effective_B = u2.pokeman.CLASS_EFFECTIVENESS["GRASS"]
                    damage = u2Attack*effective_B
                    u1.defend(damage)

                elif u1.get_poke_name() == "Charmander" and u2.get_poke_name() == "Squirtle":
                    effective_S = u1.pokeman.CLASS_EFFECTIVENESS["WATER"]
                    damage = u1Attack*effective_S
                    u2.defend(damage)

                    effective_S = u2.pokeman.CLASS_EFFECTIVENESS["WATER"]
                    damage = u2Attack*effective_S
                    u1.defend(damage)

                elif u1.get_poke_name() == "Bulbasaur" and u2.get_poke_name() == "Bulbasaur":
                    effective_B = u1.pokeman.CLASS_EFFECTIVENESS["GRASS"]
                    damage = u1Attack*effective_B
                    u2.defend(damage)

                    effective_B = u2.pokeman.CLASS_EFFECTIVENESS["GRASS"]
                    damage = u2Attack*effective_B
                    u1.defend(damage)

                elif u1.get_poke_name() == "Bulbasaur" and u2.get_poke_name() == "Squirtle":
                    effective_S = u1.pokeman.CLASS_EFFECTIVENESS["WATER"]
                    damage = u1Attack*effective_S
                    u2.defend(damage)

                    effective_S = u2.pokeman.CLASS_EFFECTIVENESS["WATER"]
                    damage = u2Attack*effective_S
                    u1.defend(damage)

                elif u1.get_poke_name() == "Bulbasaur" and u2.get_poke_name() == "Charmander":
                    effective_C = u1.pokeman.CLASS_EFFECTIVENESS["FIRE"]
                    damage = u1Attack*effective_C
                    u2.defend(damage)

                    effective_C = u2.pokeman.CLASS_EFFECTIVENESS["FIRE"]
                    damage = u2Attack*effective_C
                    u1.defend(damage)
                    
                elif u1.get_poke_name() == "Squirtle" and u2.get_poke_name() == "Squirtle":
                    effective_S = u1.pokeman.CLASS_EFFECTIVENESS["WATER"]
                    damage = u1Attack*effective_S
                    u2.defend(damage)

                    effective_S = u2.pokeman.CLASS_EFFECTIVENESS["WATER"]
                    damage = u2Attack*effective_S
                    u1.defend(damage)

                elif u1.get_poke_name() == "Squirtle" and u2.get_poke_name() == "Bulbasaur":
                    effective_B = u1.pokeman.CLASS_EFFECTIVENESS["GRASS"]
                    damage = u1Attack*effective_B
                    u2.defend(damage)

                    effective_B = u2.pokeman.CLASS_EFFECTIVENESS["GRASS"]
                    damage = u2Attack*effective_B
                    u1.defend(damage)

                elif u1.get_poke_name() == "Squirtle" and u2.get_poke_name() == "Charmander":
                    effective_C = u1.pokeman.CLASS_EFFECTIVENESS["FIRE"]
                    damage = u1Attack*effective_C
                    u2.defend(damage)

                    effective_C = u2.pokeman.CLASS_EFFECTIVENESS["FIRE"]
                    damage = u2Attack*effective_C
                    u1.defend(damage)

        if battle_mode == 0:     #if battlemode is 0 push pokemon back into stack
    
            if u1.PokemonBase.is_fainted:
                team1._ArrayStack_.push(u1)
            elif u2.PokemonBase.is_fainted:
                team2._ArrayStack_.pop(u2)

        elif battle_mode == 1:    #if battlemode is 1 push pokemon back into queue
        
            if u1.PokemonBase.is_fainted:
                team1._CircularQueue_.append(u1)
            elif u2.PokemonBase.is_fainted:
                team2._CircularQueue_.append(u2)

        if team1.is_empty:
            print(0)        #prints 0 if player_one wins
        elif team2.is_empty:
            print(1)        #prints 1 if player_two wins
        elif team1.is_empty and team2.is_empty:
            print(2)        #prints 2 if theres a tie 

if __name__=="__main__":
    my_team = Battle()
    my_team.rotating_mode_battle("Ash", "Gary")
    my_team.set_mode_battle("Ash", "Gary")
    print(my_team)

            
