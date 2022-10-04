"""EX06--A simulated quest and story of revenge with use of functions and global variables (CYOA)."""

__author__ = "730510525"

from random import randint

points: int = 0
player: str = ""
UNAMUSED_FACE: str = "\U0001F612"
HEART_EYES: str = "\U0001F60D"


def greet() -> None:
    """Greets the player and gives some context to the game."""
    global player
    player = input("What is your name? ")
    print(f"\nBinario: Hello {player}, I hope you're looking forward to another boring day in the virtual realm...\nBinario: On a sudden and unrelated note, have you heard about the monster going around--")
    print("(you hear distant screams in the background as your best friend, Binario, is slaughtered by a hideous monster)")
    print("Unknown Monster: muahahaha...bow down to me, puny 32-bit beings...I am the most powerful creature in existence,\nthe most unethical algorithm, and the most merciless foe--I am...THE AUTOGRADER")


def fight() -> str:
    """Simulates the fight between the player and autograder."""
    global player
    print(f"\nAutograder: Well {player}, you're pretty brave if you choose to fight me, but you will be crushed nonetheless...")
    print("(For each attack launched by the autograder, you will have a choice between 2 attacks...TYPE 1 or 2 to choose a counterattack)")
    global points
    valid: bool = True
    while valid:
        print("\nThe autograder attacks with LintError: Missing space on line 16")
        attack1: str = input("\n1. Add a space on line 16\n2. Remove the docstring from your main function\n")
        if attack1 == "1":
            print("\nThe counterattack was super effective! You only lost 5HP!")
            points -= 5
            valid = False
        elif attack1 == "2":
            print("\nOh no! Your main function doesn't work and the autograder's attack was very damaging...You lost 45HP")
            points -= 45
            valid = False
        else:
            print("\nYour input is invalid. Try again.\n")
    print(f"HP: {points}")
    while not valid:
        print("\nThe autograder attacks with IndexError on your line \"variable[len(variable)]\"")
        attack2: str = input("\n1. Change the name of the variable to a valid string\n2. Change the line to read \"variable[len(variable) - 1]\"\n")
        if attack2 == "1":
            print("\nThis didn't get rid of the error! The autograder's attack was super effective! You lose 60HP")
            points -= 60
            valid = True
        elif attack2 == "2":
            print("\nYou completely blocked his attack! You don't lose any HP!")
            valid = True
        else:
            print("\nYour input is invalid. Try again.\n")
    print(f"HP: {points}")
    while valid:
        print("\nThe autograder attacks with TypeError on your function definition")
        attack3: str = input("\n1. Examine the body of the function for the error\n2. Look at the function signature line to see if the parameter data types match up with the arguments\nand if the return value matches what is specified after the arrow\n")
        if attack3 == "1":
            print("\nThe autograder lands a deadly blow after that miscalculation...You lose 55HP")
            points -= 55
            if points <= 0:
                outcome: str = "L"
                return outcome
            valid = False
        elif attack3 == "2":
            print("\nNice counter! You only lost 20HP")
            points -= 20
            valid = False
        else:
            print("\nYour input is invalid. Try again.\n")
    print(f"HP: {points}")
    while not valid:
        print("\nThe autograder attacks with SyntaxError on your while loop conditional")
        attack4: str = input("\n1. Add a colon...it's always a missing colon error\n2. Just throw a for loop in there instead\n")
        if attack4 == "1":
            print("\nFor such an elegant solution, you receive a bonus 5HP")
            points += 5
            valid = True
        elif attack4 == "2":
            print("\nThe autograder deals a strong attack, and you lose 80HP")
            points -= 80
            valid = True
        else:
            print("\nYour input is invalid. Try again.\n")
    print(f"HP: {points}")
    if points > 0:
        outcome = "W"
    else:
        outcome = "L"
    return outcome


def choc_arc(score: int) -> int:
    """Simulates the player's career working with chocolate."""
    global player
    print(f"\nWelcome {player}, this was a questionable decision you've made, but welcome to the world of chocolatetiering!\nSince chocolate generally makes everyone happy, you already have an approval rating of {score}CP (choccy points)")
    print("Your goal is to make the best chocolate recipe possible by adding or leaving out ingredients presented to you\nGood luck!")
    baking: bool = True
    while baking:
        cacao: str = input("\nWould you like to add cacao powder to the mix? (Y or N)\n")
        if cacao == "Y":
            print(f"Good choice! {HEART_EYES}\n")
            score += randint(10, 20)
            baking = False
        elif cacao == "N":
            print(f"...No words...{UNAMUSED_FACE}\n")
            score -= randint(5, 35)
            baking = False
        else:
            print("You typed an invalid input. Try again. ")
    print(f"Total CP: {score}")
    while not baking:
        milk: str = input("\nWould you like to add milk to the mix? (Y or N)\n")
        if milk == "Y":
            print("Good choice again, you have a few working brain cells at least\n")
            score += randint(20, 40)
            baking = True
        elif milk == "N":
            print("Yikes...\n")
            score -= randint(10, 30)
            baking = True
        else:
            print("You typed an invalid input. Try again. ")
    print(f"Total CP: {score}")
    while baking:
        baking_soda: str = input("\nWould you like to add baking soda to the mix? (Y or N)\n")
        if baking_soda == "Y":
            print(f"Please change professions {UNAMUSED_FACE}\n")
            score -= randint(10, 20)
            baking = False
        elif baking_soda == "N":
            print("Well done, well done\n")
            score += randint(15, 45)
            baking = False
        else:
            print("You typed an invalid input. Try again. ")
    print(f"Total CP: {score}")
    while not baking:
        salt: str = input("\nWould you like to add a pinch of salt to the mix? (Y or N)\n")
        if salt == "Y":
            print(f"Mmmmmmm...{HEART_EYES}\n")
            score += randint(30, 50)
            baking = True
        elif salt == "N":
            print(f"Bland chocolate, but it's fine {UNAMUSED_FACE}\n")
            score -= randint(0, 5)
            baking = True
        else:
            print("You typed an invalid input. Try again. ")
    print(f"Total CP: {score}")
    while baking:
        sugar: str = input("\nWould you like to add sugar to the mix? (Y or N)\n")
        if sugar == "Y":
            print(f"Yummmmmm {HEART_EYES}\n")
            score += randint(15, 60)
            baking = False
        elif sugar == "N":
            print(f"Is this supposed to be dark chocolate? {UNAMUSED_FACE}\n")
            score -= randint(5, 40)
            baking = False
        else:
            print("You typed an invalid input. Try again. ")
    print(f"Total CP: {score}")
    return score
    

def main() -> None:
    """Entrypoint for the program."""
    global player
    global points
    playing: bool = True
    greet()
    while playing:
        points = 150
        print(f"\n{player}, you have a full {points} points to start the game")
        choice: str = input("\nIn your head, you know the autograder must be defeated; he has been destoying programs and their creators for weeks now. Do you:\n1. Fight the autograder in mortal combat\n2. Flee and never return, disregarding the death of your best friend and other programs, to become a chocolatetier\n3. Beg for mercy (end the game, as the autograder is cruel and will not grant you your life and freedom)\n(TYPE 1, 2, or 3)\n")
        if choice == "1":
            outcome: str = fight()
            if outcome == "W":
                mercy: str = input("\nYou win the fight, but at what cost? The autograder is crying on the ground, for he is only a computer\nprogram created to fix useful functions, but he has accidentially caused so much harm...\nWill you give him mercy?(TYPE Y or N) ")
                if mercy == "Y":
                    print("\nAutograder: muahahahaha...you fool...")
                    print("(A digitalized UNC basketball team is spawned into the realm and you get dunked on so hard, you simply stop breathing,\nmeanwhile your friends and family are also destroyed by a sequence of impending slam dunks)")
                else:
                    print(f"\nYou win!!! Congratulations {player}")
            else:
                print("\nYou lost the battle against the autograder, and he destoys the virtual realm,\nputting a firm end to the career of becoming a computer programmer...")
        if choice == "3":
            print("\nThe autograder immediately vaporizes you, and you turn into a fine dust of pixels and bytes (and, of course, you have 0HP)")
        if choice == "2":
            points = choc_arc(points)
            if points > 200:
                print(f"Wow {player}, you're an amazing maker of chocolate!\nYou have an approval rating of {points}CP!")
            else:
                print(f"\n{player}, you somehow managed to mess up chocolate...that's some accomplishment...\nYou have an approval rating of {points} CP")
        retry: str = input("\nDo you want to play again? (Y or N)")
        if retry == "N":
            playing = False


if __name__ == "__main__":
    main()