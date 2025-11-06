import random

def get_name():
    name = input("Namn?: ")
    return name

def number_guess():
    guess = int(input("Gissa ett tal mellan 1 - 10: "))
    i = random.randint(1,10)
    if i == guess:
        print("Hippie hurra! 🙌")
    else:
        print(f"Tyvärr det var {i}")

def main():
    name = get_name()
    print(f"Hej {name} och välkomenen till the squid games!")
    guess = number_guess

main()