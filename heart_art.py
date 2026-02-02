# Valentines Day Heart Art
import time
import sys

def red(text: str) -> str:
    return f"\033[91m{text}\033[0m"

def green(text: str) -> str:
    return f"\033[92m{text}\033[0m"

def user_input():
    displayed_text = input("Yes or No?: ")
    if displayed_text.lower() == "yes":
        print(green("Yay! Happy Valentine's Day! <3"))
    elif displayed_text.lower() == "y":
        print(green("Yay! Happy Valentine's Day! <3"))
    elif displayed_text == "YES":
        print(green("Yay! Happy Valentine's Day! <3"))
    elif displayed_text == "Y":
        print(green("Yay! Happy Valentine's Day! <3"))
    elif displayed_text == "Yes":
        print(green("Yay! Happy Valentine's Day! <3"))
    else:
        print(red("Oh no! Maybe next time :("))

def love(height):
    stars = 1
    space1 = 3
    space2 = 5
    print(" ");
    for i in range(1, height-1):
        print((" " * space1) + (red("*") * stars) + (" " * space2) + (red("*") * stars) + (" " * space1))
        stars += 2
        space1 -= 1
        space2 -= 2
    stars = 11
    space1 = 1
    space2 = 1
    for j in range(1, height+2):
        print((" " * space1) + (red("*") * stars) + (" " * space2))
        stars -= 2
        space1 += 1
        space2 += 1
    print(" ");
    text = "Will you be my Valentine?"
    for char in text:
        sys.stdout.write(red(char))
        sys.stdout.flush()
        time.sleep(0.2)
    print();
    user_input();
    time.sleep(5);
love(5);
