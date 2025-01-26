# Import the random library to use for dice rolls
import random

# Step 1: Create dice options using list() and range()
diceOptions = list(range(1, 7))  # [1, 2, 3, 4, 5, 6]

# Define weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

# Display available weapons
print("Available weapons:")
for i, weapon in enumerate(weapons, start=1):
    print(f"{i}. {weapon}")

# Step 3: Input validation for hero and monster combat strengths
while True:
    try:
        combatStrength = int(input("Enter your combat Strength (1-6): "))
        if 1 <= combatStrength <= 6:
            break
        else:
            print("Please enter a number between 1 and 6.")
    except ValueError:
        print("Invalid input! Please enter an integer.")

while True:
    try:
        mCombatStrength = int(input("Enter the monster's combat Strength (1-6): "))
        if 1 <= mCombatStrength <= 6:
            break
        else:
            print("Please enter a number between 1 and 6.")
    except ValueError:
        print("Invalid input! Please enter an integer.")

# Roll dice for initial health points
input("Roll the dice for your health points (Press enter)")
heroHealth = random.choice(diceOptions)
print(f"You rolled {heroHealth} health points.")

input("Roll the dice for the monster's health points (Press enter)")
monsterHealth = random.choice(diceOptions)
print(f"You rolled {monsterHealth} health points for the monster.")

# Check for a healing potion
input("Roll the dice to see if you find a healing potion (Press enter)")
healingPotion = random.choice([0, 1])
print(f"Have you found a healing potion? {bool(healingPotion)}")

# Step 4: Simulate 10 rounds of battle
for round_num in range(1, 21, 2):  # 10 rounds, stepping by 2
    print(f"\n--- Round {round_num} ---")

    # Roll dice for hero and monster
    heroRoll = random.choice(diceOptions)
    monsterRoll = random.choice(diceOptions)

    # Roll for weapon
    weaponRoll = random.choice(diceOptions)
    selectedWeapon = weapons[weaponRoll - 1]

    # Update combat strengths
    heroStrength = combatStrength + heroRoll
    monsterStrength = mCombatStrength + monsterRoll

    # Announce round details
    print(f"Hero rolled {heroRoll} (Strength: {heroStrength})")
    print(f"Monster rolled {monsterRoll} (Strength: {monsterStrength})")
    print(f"Hero's weapon: {selectedWeapon}")

    # Determine the winner of the round
    if heroStrength >= monsterStrength:
        monsterHealth -= heroStrength
        print(f"Hero wins the round! Monster's health is now {max(0, monsterHealth)}")
    else:
        heroHealth -= monsterStrength
        print(f"Monster wins the round! Hero's health is now {max(0, heroHealth)}")

    # Check if either hero or monster is dead
    if heroHealth <= 0:
        print("Hero has been defeated. Game Over!")
        break
    if monsterHealth <= 0:
        print("Monster has been defeated. You win!")
        break

    # Step 5: Break condition for "Battle Truce"
    if round_num == 11:
        print("Battle Truce! Both sides retreat.")
        break

# Final game status
if heroHealth > 0 and monsterHealth > 0:
    print("The battle ends inconclusively.")

