# Import the random library to use for the dice later
import random

# Will the line below print when you import function.py into main.py?
# print("Inside function.py")

# Hero's Attack Function
def hero_attacks(combat_strength, m_health_points):
    ascii_image = """
                                @@   @@ 
                                @    @  
                                @   @   
               @@@@@@          @@  @    
            @@       @@        @ @@     
           @%         @     @@@ @       
            @        @@     @@@@@     
               @@@@@        @@       
               @    @@@@                
          @@@ @@                        
       @@     @                         
   @@*       @                          
   @        @@                          
           @@                                                    
         @   @@@@@@@                    
        @            @                  
      @              @                  

  """
    print(ascii_image)
    print("    |    Player's weapon (" + str(combat_strength) + ") ---> Monster (" + str(m_health_points) + ")")
    if combat_strength >= m_health_points:
        # Player was strong enough to kill monster in one blow
        m_health_points = 0
        print("    |    You have killed the monster")
    else:
        # Player only damaged the monster
        m_health_points -= combat_strength

        print("    |    You have reduced the monster's health to: " + str(m_health_points))
    return m_health_points


# Monster's Attack Function
def monster_attacks(m_combat_strength, health_points):
    ascii_image2 = """                                                                 
           @@@@ @                           
      (     @*&@  ,                         
    @               %                       
     &#(@(@%@@@@@*   /                      
      @@@@@.                                
               @       /                    
                %         @                 
            ,(@(*/           %              
               @ (  .@#                 @   
                          @           .@@. @
                   @         ,              
                      @       @ .@          
                             @              
                          *(*  *      
             """
    print(ascii_image2)
    print("    |    Monster's Claw (" + str(m_combat_strength) + ") ---> Player (" + str(health_points) + ")")
    if m_combat_strength >= health_points:
        # Monster was strong enough to kill player in one blow
        health_points = 0
        print("    |    Player is dead")
    else:
        # Monster only damaged the player
        health_points -= m_combat_strength
        print("    |    The monster has reduced Player's health to: " + str(health_points))
    return health_points

#collect loot function
def collect_loot(loot_options, belt):
    print("!!You find a loot bag!! You look inside to find 2 items:")

    for _ in range(2): #collect 2 items
        input("Roll for first item (Press enter)")
        lootRoll = random.choice(range(1, len(loot_options) + 1))
        loot = loot_options.pop(lootRoll - 1)
        belt.append(loot)
        print("Your belt: ", belt)

    return belt,loot_options #return the updated belt and loot_options

#use loot function
def use_loot(belt, health_points, good_loot_options, bad_loot_options):
    print("!!You see a monster in the distance! so you quickly use your first item:")
    first_item = belt.pop(0)
    if first_item in good_loot_options:
        health_points = min(6, (health_points + 2))
        print(f"You used {first_item} to up your health to {health_points}")
    elif first_item in bad_loot_options:
        health_points = max(0, (health_points - 2))
        print(f"You used {first_item} to hurt your health to {health_points}")
    else:
    print(f"You used {first_item} but it's not helpful")
   return belt, health_points #return the updated belt and health_points

#Attack Roll Function
def determine_first_attacker():
    attack_roll = random.choice(range(1, 6))
    print(f"Rolling to see who attacks first... {attack_roll}")

    if attack_roll in [1,3,5]:
        print("Hero attacks first")
        return "Hero"
    else:
        print("Monster attacks first")
        return "Monster"
    
    #Recursion function 
    def inception_dream(layer-0):
        print(f"Entering Dream Layer {layer}...")

        if layer == 3:
            print(f"Deepest dream layer reached. Returning 2.")
            return 2
        else:
            print(f"Going deeper into the dream...")
            return 1 + inception_dream(layer + 1)

