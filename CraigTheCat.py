#Craig The Cat
import time

def main():

    print("Mow meow meow mow meow meow meow!")
    time.sleep(2)
    print ("what would you like to do?")
    userChoice = input("1. Play with Craig\n2. Feed Craig\n3. Sleep\n4. Quit\n")
    if userChoice == "1":
        print("Craig is excited to play with you!")
        time.sleep(2)
        print("Craig is playing with a ball of yarn!")
        time.sleep(2)
        print("Craig is chasing a laser pointer!")
        time.sleep(2)
        print("Craig is playing with a toy mouse!")
        time.sleep(2)
        print("Craig is tired from playing!")
        time.sleep(2)
        print("Craig is taking a nap!")
        time.sleep(2)
        main()
    elif userChoice == "2":
        print("Craig is hungry!")
        time.sleep(2)
        print("Craig is eating!")
        time.sleep(2)
        print("Craig is full!")
        time.sleep(2)
        print("Craig is taking a nap!")
        time.sleep(2)
        main()
    elif userChoice == "3":
        print("Craig is tired!")
        time.sleep(2)
        print("Craig is sleeping!")
        time.sleep(2)
        print("Craig is dreaming!")
        time.sleep(2)
        print("Craig is awake!")
        time.sleep(2)
        main()
    elif userChoice == "4":
        print("Goodbye!")
    else:
        print("Invalid choice. Please choose a valid option.")
        main()

print("Meow, meow meow mow meow mow meow!")
time.sleep(2)
print("Mow mow mow meow, meow mow meow mow meow mow mow!")
time.sleep(2)

main()