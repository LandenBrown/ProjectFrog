import random

from frog_species import Frog
from world_biome import Biome
from predator_species import Predator

####Initial Data Creation and Collection Sets

#First names

frog_first_names = ["Foro", "Litho", "Oro", "Morro", "Jerro", "Kiro"]
predator_first_names = ["Veres", "Treves", "Meres", "Heres", "Nores", "Maxes"]

#Middle names
frog_middle_names = ["te", "de", "le", "vur", "lor", "lex", "ret", "vet", "cret", "feg", "van", "vax", "cet"]
predator_middle_names = ["de", "ret", "rat", "raf", "fer", "dur", "lur", "bay", "tray", "tre", "jer"]

#Last names
frog_last_names = ["lithius", "birtius", "crethius", "ferelias", "trallium", "borallian"]
predator_last_names = ["relious", "celius", "tricillian", "gorian", "filthian", "vestian", "snichian"]

def create_a_frog_name(fnames, mnames, lnames):
    #getting length of arrays minus 1
    fnamelength = (len(fnames)-1)
    mnamelength = (len(mnames)-1)
    lnamelength = (len(lnames)-1)
    #Generating random number between 1 and length of array
    fnamerandom = random.randint(1, fnamelength)
    mnamerandom = random.randint(1, mnamelength)
    lnamerandom = random.randint(1, lnamelength)
    #Building the random name with random selection in each array
    randomName = fnames[fnamerandom]+mnames[mnamerandom]+lnames[lnamerandom]
    return randomName
def create_a_predator_name(fnames, mnames, lnames):
    #getting length of arrays minus 1
    fnamelength = (len(fnames)-1)
    mnamelength = (len(mnames)-1)
    lnamelength = (len(lnames)-1)
    #Generating random number between 1 and length of array
    fnamerandom = random.randint(1, fnamelength)
    mnamerandom = random.randint(1, mnamelength)
    lnamerandom = random.randint(1, lnamelength)
    #Building the random name with random selection in each array
    randomName = fnames[fnamerandom]+mnames[mnamerandom]+lnames[lnamerandom]
    return randomName


######## FROG DATA
#Internal Attributes
#List:
frog_int_atts = ["Cold Blooded", "Warm Blooded", "Scared", "Brave"]
#
#
#External Attributes
#List:
frog_ext_atts = ["Strong", "Weak", "Fast", "Slow", "Camoflauge", "Smelly"]
#
#
######## PREDATOR DATA
#Internal Attributes
#List:
predator_int_atts = ["Cold Blooded", "Warm Blooded"]
#
#
#External Attributes
#List:
predator_ext_atts = ["Strong", "Weak", "Fast", "Slow"]
#
#



################################################################################      FROGS
def create_an_initial_frog(int_atts, ext_atts):
    ###Calculate Internal Attribute
    #getting length of arrays minus 1
    int_atts_length = (len(int_atts)-1) 
    #Generating random number between 1 and length of array
    RandomIntAtt_spot = random.randint(0, int_atts_length)
    RandomIntAtt = int_atts[RandomIntAtt_spot]
    
    ###Calculate External Attribute
    #getting length of arrays minus 1
    ext_atts_length = (len(ext_atts)-1)
    #Generating random number between 1 and length of array
    RandomExtAtt_spot = random.randint(0, ext_atts_length)
    RandomExtAtt = ext_atts[RandomExtAtt_spot]

    ###Calculate Name
    randomName = create_a_frog_name(frog_first_names, frog_middle_names, frog_last_names)

    ###Calculate Lifespan
    #Set lifespan constraints
    min_lifespan_days = 20
    max_lifespan_days = 100
    #Generate random lifespan
    randomLifespan = random.randint(min_lifespan_days, max_lifespan_days)

    #Generate time to starve
    min_food_days = 2
    min_food_days = 5
    #Gerenate random starvation period
    randomStarvation = random.randint(min_food_days, max_lifespan_days)

    #Creat new frog and return it
    newFrog = Frog(randomName, RandomExtAtt, RandomIntAtt, 1, randomLifespan, 0, randomStarvation, False)
    return newFrog

#frog1 = create_an_initial_frog(frog_int_atts, frog_ext_atts)
#print(frog1.name,frog1.internal_attributes,frog1.external_attributes,str(frog1.lifespan_days))




    


################################################################################      PREDATORS
def create_an_initial_predator(int_atts, ext_atts):
    ###Calculate Internal Attribute
    #getting length of arrays minus 1
    int_atts_length = (len(int_atts)-1) 
    #Generating random number between 1 and length of array
    RandomIntAtt_spot = random.randint(0, int_atts_length)
    RandomIntAtt = int_atts[RandomIntAtt_spot]
    
    ###Calculate External Attribute
    #getting length of arrays minus 1
    ext_atts_length = (len(ext_atts)-1)
    #Generating random number between 1 and length of array
    RandomExtAtt_spot = random.randint(0, ext_atts_length)
    RandomExtAtt = ext_atts[RandomExtAtt_spot]

    ###Calculate Name
    randomName = create_a_predator_name(predator_first_names, predator_middle_names, predator_last_names)

    ###Calculate Lifespan
    #Set lifespan constraints
    min_lifespan_days = 20
    max_lifespan_days = 100
    #Generate random lifespan
    randomLifespan = random.randint(min_lifespan_days, max_lifespan_days)

    #Creat new frog and return it
    newPredator = Predator(randomName, "Walk", RandomExtAtt, RandomIntAtt, "Bite", randomLifespan)
    return newPredator
    
#predator1 = create_an_initial_predator(predator_int_atts, predator_ext_atts)
#print(predator1.name,predator1.internal_attributes,predator1.external_attributes,str(predator1.lifespan_days))

#Biomes

standardJungle = Biome("Standard", "Tropical", "Rainforest", "Normal", "Picked", "Consistent", "Standard")