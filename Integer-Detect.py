# How to make sure user input a number
def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Not an intiger! Try again")
            continue
        else:
            return userInput
        break

# Main program Start here

age = inputNumber("How old are you?")
if(age>=18):
    print("You are old enouph to vote")
else:
    print("You will be able to vote in" , str(18 - age) , "years.")