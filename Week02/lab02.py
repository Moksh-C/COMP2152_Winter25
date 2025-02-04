import random

# Define weapons array
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]


def get_valid_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Please enter a valid integer!")


try:
    # Roll the dice to determine weaponRoll
    weaponRoll = random.randint(1, 6)
    print(f"Weapon roll: {weaponRoll}")

    # Access weapon based on weaponRoll (index starts from 0, so subtract 1)
    weapon = weapons[weaponRoll - 1]
    print(f"Hero's weapon: {weapon}")


    if weaponRoll <= 2:
        print("You rolled a weak weapon, friend.")
    elif weaponRoll <= 4:
        print("Your weapon is meh.")
    else:
        print("Nice weapon, friend!")

    # Special case for Fist
    if weapon != "Fist":
        print("Thank goodness you didn't roll the Fist...")
except IndexError:
    print("Error: Invalid weapon roll. Please try again.")
except Exception as e:
    print(f"Unexpected error: {e}")
