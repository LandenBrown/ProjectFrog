#this is the start of something great


###initial planning: 
#Frogs: 2
#Predators: 1
#
#
#
#
#

import time

versionNumber = "0.1"
sysQuit = "x"

print ("Welcome to the Prject Frog, Version", versionNumber)

print("Press X to randomize population and biome data...")


#Initial 
p_input = input()
if p_input == "X" or p_input == "x":
    print("Diving into the world of Project Frog")
    time.sleep(0.4)
    #####CREATE OBJECTS HERE
    #Biome Details here
    print("Biome Details:\n-Weather: X\n-Foliage: X\n-Foliage Density: X")
    #Initial Frog count and details here
    print("Frogs: X")
    print("-Frog 1: X\n-Frog 2: X")
    #Initial Predator count and details here
    print("Predators: X")
    print("-Predator 1: X\n-Predator 2: X")

else:
    print("That is not a valid command, you are not worthy.")



while sysQuit != "q":
    print("test")
    sysQuit = input()