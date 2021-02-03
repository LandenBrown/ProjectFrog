import random
"""Outlining predators and how they will function"""
debugOn = False

def debugCode(x):
    if debugCode == True:
        print("DEBUG: " + x)

class Predator:
    """#Predator Class"""

    def __init__(self, name, transport_function, external_attributes, internal_attributes, attack_methods, lifespan_days, attack_chance, has_attacked, starvation_days, is_dead, days_alive, days_without_food):
        self.name = name
        self.transport_function = transport_function
        self.external_attributes = external_attributes
        self.internal_attributes = internal_attributes
        self.attack_methods = attack_methods
        self.lifespan_days = lifespan_days
        self.attack_chance = attack_chance
        self.has_attacked = has_attacked
        self.starvation_days = starvation_days
        self.is_dead = is_dead
        self.days_alive = days_alive
        self.days_without_food = days_without_food

    #This is when the predator will be checked to see if he has hit his max lifespan yet.
    def checkLifespan(self):
        self.days_alive+=1
        if self.days_alive >= self.lifespan_days:
            print("###################################   A PREDATOR HAS DIED OF OLD AGE")
            self.is_dead = True
            #####Kill predator

    #This is where we will check to see if the predator has died of starvation.
    def checkStarvation(self):
        #check to see if the predator has died of starvation.
        if self.days_without_food >= self.starvation_days:
            print("###################################   A PREDATOR HAS DIED OF STARVATION")
            ######Kill predator
            self.is_dead = True

    #This is when the predator will find food.
    def findPrey(self, frogList):
        #starting find prey function

        #Check lifespan first.
        self.checkLifespan()
        debugCode("Predator is now finding prey...")
        randomPreyFinder = random.randint(1,100)
        if randomPreyFinder > 50:
            debugCode("The predator found food...")
            #create a list of alive frogs
            frogsCurrentlyAlive = len([v for k,v in frogList.items() if v.is_dead == False])
            #get length of alive frogs list
            frogListLength = (len(frogsCurrentlyAlive)-1)
            #pick a random number between 1 and the total amount of alive frogs
            randomchoice = random.randint(1, frogListLength)
            #select the random resulting frog from previous efforts
            randomSelectedFrog = frogsCurrentlyAlive[randomchoice]

            debugCode("The gathered frog list length minus one is " + str(frogListLength))
            

        else:
            debugCode("The predator did not find food...")
            self.checkStarvation




