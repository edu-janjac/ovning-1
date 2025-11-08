import random

def get_name():
    name = input("Namn?: ")
    return name

def number_guess():
    i = random.randint(1,10)
    j = 1
    while j <= 4:
        guess = int(input("Gissa ett tal mellan 1-10: "))
        if i == guess:
            print(f"Försök {j}: Gissa talet: {guess}\nRät gissat!\nYippie! 🙌")
            break
        elif j <= 3:
            print(f"Försök {j}: Gissa talet: {guess}\nFel gissat")
            j += 1
        elif j > 3: 
            print(f"Du har slut på försök, talet var {i}")
            break

def main():
    name = get_name()
    print(f"Hej {name} och välkomenen till the squid games!")
    number_guess()

main()