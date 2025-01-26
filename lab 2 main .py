# Import the random library to use for the dice later
import random

# Define Variables
numLives = 10           # number of player's lives remaining
mNumLives = 12          # number of monster's lives remaining
#Roll options for the dice
diceOptions = [1, 2, 3, 4, 5, 6]

# Define weapons and their strengths
weapons = ["Fist", "Sword", "Club", "Gun", "Bomb","Nuclear Bomb"]
# input combat strength with error handling
combatStrength = input("Enter your combat Strength (1-10): ")
if combatStrength.isdigit() and 1 <= int(combatStrength) <= 10:
    combatStrength = int(combatStrength)
else:
    print("Please enter a number between 1 and 10")
    
    while True:
        mCombatStrength = input("Enter the monster's combat Strength (1-10): ")
        if mCombatStrength.isdigit() and 1 <= int(mCombatStrength) <= 10:
            mCombatStrength = int(mCombatStrength)
            break
        else:
            print("Please enter a number between 1 and 10 for combat strength")

    # Roll for health points
input("Roll the dice for your health points (Press enter)")
healthPoints = random.choice(diceOptions)
print("You rolled " + str(healthPoints) + " health points")

input("Roll the dice for the monster's health points (Press enter)")
mHealthPoints = random.choice(diceOptions)
print("You rolled " + str(mHealthPoints) + " health points for the monster")

# Check if healing potion is found
input("Roll the dice to see if you find a healing potion (Press enter)")
healingPotion = random.choice([0, 1])
print("Have you found a healing potion?: " + str(bool(healingPotion)))

input("Analyze the roll (Press enter)")
# Equality operators
print("--- You are matched in strength: " + str(combatStrength == mCombatStrength))

# Relational operators
print("--- You have a strong player: " + str((combatStrength + healthPoints) >= 15))

# and keyword
print("--- Remember to take a healing potion!: " + str(healingPotion == 1 and healthPoints <= 6))

# not keyword
print("--- Phew, you have a healing potion: " + str(
    not (                               # monster will NOT kill hero in one blow
        healthPoints < mCombatStrength  # monster will kill hero in one blow
    )
    and
    healingPotion == 1                  # hero has a healing potion
))

# or keyword
print("--- Things are getting dangerous: " + str(healingPotion == 0 or healthPoints == 1))

# in keyword
print("--- Is it possible to roll 0 in the dice?: " + str(0 in diceOptions))

# --- Expanded if statement
if healthPoints >= 5:
    print("--- Your health is ok")
elif healingPotion == 1:
    healingPotion = 0
    healthPoints = 6
    print("--- Using your healing potion... Your Health Points is now full at " + str(healthPoints))
else:
    print("--- Your health is low at " + str(healthPoints) + " and you have no healing potions available!")

# --- Nested if statement
print("You meet the monster. FIGHT!!")
input("You strike first (Press enter)")

#Weapon dice roll logic
weaponRoll = random.choice(diceOptions)
combatStrength += weaponRoll
weapon = weapons[weaponRoll - 1]

#weapon feedback
print(f"your weapon: {weapon}")
if weaponRoll <=2:
    print("You rolled a weak weapon, friend.")
elif weaponRoll <= 4:
    print("Your weapoon is meh.")
else:
    print("Nice weapon, friend!")

    #Check fist weapon
    if weapon != "Fist":
        print("Thank goodness you didn't roll a fist!")

print("Your sword (" + str(combatStrength) + ") ---> Monster (" + str(mHealthPoints) + ")")
if combatStrength >= mHealthPoints:
    mHealthPoints = 0
    print("You've killed the monster")
else:
    mHealthPoints -= combatStrength

    print("You've reduced the monster's health to: " + str(mHealthPoints))

    print("The monster strikes!!!")
    print("Monster's Claw (" + str(mCombatStrength) + ") ---> You (" + str(healthPoints) + ")")
    if mCombatStrength >= healthPoints:
        healthPoints = 0
        print("You're dead")
    else:
        healthPoints -= mCombatStrength
        print("The monster has reduced your health to: " + str(healthPoints))

        #Final check 
        if healthPoints == 0:
           print("Game over, You lost")
        elif mHealthPoints == 0:
            print("You won the battle!")
        else:
            print("The battle continues...")

