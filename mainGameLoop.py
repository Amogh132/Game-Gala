import time
import sys
from Mobs import enemy_template, Mob, enemy_encounter


# Typing animation function
def typing_animation(text, delay=0.05):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)
    print()


# Initialize variables
username = ""
health = 0
strength = 0
agility = 0
luck = 0
shield = 0
playerCheating = True
playerDead = False
gameMode = ""
mobDict = {mob.name: mob for mob in enemy_template}
currMob = mobDict.get("Alien")
enemy_encounter()

# Game start loop
while playerDead == False:
    print("Welcome to *game title*, we hope you enjoy!")
    time.sleep(0.5)
    username = input("Enter the Player's name: ")
    time.sleep(0.5)
    print(f"Welcome {username}! You may now choose your stats. Keep in mind that you only have 6 stat points; choose your stats wisely!")
    time.sleep(0.5)

    # Stat loop
    while playerCheating:
        health = int(input("How many points would you like to put into Health? Health increases in increments of 5: "))
        time.sleep(0.5)
        strength = int(input("How many points would you like to put into Strength? Strength increases in increments of 1: "))
        time.sleep(0.5)
        agility = int(input("How many points would you like to put into Agility? Agility increases in increments of 1: "))
        time.sleep(0.5)
        shield = int(input("How many points would you like to put into Shield? Shield increases in increments of 1: "))
        time.sleep(0.5)
        luck = int(input("How many points would you like to put into Luck? Luck increases in increments of 1: "))
        playerstats = [health, strength, agility, shield, luck]

        if sum(playerstats) != 6:
            print("The total of your stat points must equal 6. Please re-enter your stats.")
        else:
            playerstats[1] = playerstats[1] * 5  # Strength multiplies by 5
            playerCheating = False  # Exit the loop

    # Display stats (for debugging or future implementation)
    print(f"Stats confirmed: Health = {health}, Strength = {strength}, Agility = {agility}, Shield = {shield}, Luck = {luck}")

    # Class selection and mode choice
    print(f"Welcome {username}! You are now ready to begin your adventure.")
    time.sleep(0.5)

    userChoiceCorrect = False
    while not userChoiceCorrect:
        userchoice = input("What mode would you like to choose? Hard, Medium, Easy: ").strip().lower()
        if userchoice == "hard":
            gameMode = "hard"
            userChoiceCorrect = True
        elif userchoice == "medium":
            gameMode = "medium"
            userChoiceCorrect = True
        elif userchoice == "easy":
            gameMode = "easy"
            userChoiceCorrect = True
        else:
            print("Invalid choice. Please choose 'Hard', 'Medium', or 'Easy'.")

    # Game introduction
    print("The year is 2245. Humanity has spread across the stars, colonizing distant planets and building massive space stations, all connected by the vast web of interstellar trade and diplomacy.")
    time.sleep(2)
    print("However, not all is well in this bright future. The once harmonious relations between the human colonies are beginning to crack, and a mysterious force known only as The Void is slowly encroaching on the edges of the known universe.")
    time.sleep(2)
    print("As an elite member of a covert organization known as The Vanguard, you have been tasked with investigating strange occurrences across the galaxy—disappearances, destroyed ships, and mysterious messages that seem to come from the heart of The Void.")
    time.sleep(2)
    print("Some say it is an ancient alien force, others believe it is the result of humanity’s own arrogance in unlocking the secrets of deep space.")
    time.sleep(2)

    if gameMode == "easy":
        print("You begin in a bustling city on Mars, receiving a secretive message from an anonymous source urging you to investigate an abandoned research station on a forgotten moon.")
        time.sleep(2)
        typing_animation("Traveling....", delay=0.1)

        # Future game actions would go here, such as combat or investigation choices
        print("You arrive at the moon. It looks eerie, with ruins scattered across the surface. The research station seems abandoned, but something feels off...")
        time.sleep(2)