
"""I made this because I knew it was an important way to show off basic programming
knowledge. Atleast now if I go into an interview I can make this again."""
number = 0 ## Starting value for fizzBuzz
willcountto = 50 ## how long fizzbuzz will run

def fizz_buzz(number: int, willcountto: int):
    for x in range(willcountto):
        number += 1
        if number%3 == 0:
            if number%5 == 0:
                print("fizzbuzz")
            else:
                print("fizz")
        elif number%5 == 0:
            print("buzz")
        else:
            print(number)

if __name__ == "__main__":
    fizz_buzz(number, willcountto)
