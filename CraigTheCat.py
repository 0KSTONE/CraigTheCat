#Craig The Cat
import time
import random as r

class Craig:
    def __init__(self):
        self.hunger = 5
        self.tiredness = 8
        self.happiness = 0
      
    def play(self):
        self.hunger += 3
        self.tiredness += 3
        self.happiness += r.randint(3, 7)
        Craig.checkStatus()
    def feed(self):
        self.hunger -= 5
        self.tiredness += 1
        self.happiness += 1
        Craig.checkStatus()
    def sleep(self): 
        self.hunger += 2
        self.tiredness -= 5
        self.happiness += 2
        Craig.checkStatus()
    def checkStatus(self):
        self.hunger = max(0, min(self.hunger, 10))
        self.tiredness = max(0, min(self.tiredness, 10))
        self.happiness = max(0, min(self.happiness, 10))
        

    

def main():
    while True:
        print("Mow meow mow meow meow meow!") #Mow meow * 2
        time.sleep(2)
        print ("what would you like to do?")
        userChoice = input("1. Play with Craig\n2. Feed Craig\n3. Sleep\n4. Craig\nQuit(Q) \n")
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
            
            Craig.play()
            time.sleep(2)
        elif userChoice == "2":
            print("Craig is hungry!")
            time.sleep(2)
            print("Craig is eating!")
            time.sleep(2)
            print("Craig is full!")
            time.sleep(2)
            print("Craig is taking a nap!")

            Craig.feed()
            time.sleep(2)

        elif userChoice == "3":
            print("Craig is tired!")
            time.sleep(2)
            print("Craig is sleeping!")
            time.sleep(2)
            print("Craig is dreaming!")
            time.sleep(2)
            print("Craig is awake!")

            Craig.sleep()
            time.sleep(2)
        
        elif userChoice == "4":
            print("Craig's current status:")
            print(f"Hunger: {Craig.hunger}")
            print(f"Tiredness: {Craig.tiredness}")
            print(f"Happiness: {Craig.happiness}")
            time.sleep(2)

        elif userChoice == "Q" or userChoice == "q":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
            continue

#Craig
Craig = Craig() #This is Craig the cat
#That was Craig the cat

print("Meow, meow meow mow meow mow meow!")
time.sleep(2)
print("Mow mow mow meow, meow mow meow mow meow mow mow!")
time.sleep(2)

main()