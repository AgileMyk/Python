
#Hide Assignment Information
#Instructions
#This week's assignment involves writing a Python program to compute the 
#cost of house cleaning. Your program should prompt the user for the number 
#of rooms in the house and the type of cleaning (e.g., floors, windows, 
#bathrooms, dusting). Your program must offer at least two types of cleaning 
#and the price is different for each type. You should decide on the choices 
#to offer and the different prices of each type of cleaning. The cost should 
#be based on whether the house has a small, medium, or a large number of rooms 
#and the type of cleaning. You should decide on the cutoffs for what constitutes 
#a small, medium, and large number of rooms. Your program should output the cost 
#of the house cleaning based on the number of rooms and the type of cleaning.

#Your program should include Header comments (what the program does) and in-line 
#comments (the major design steps). Document the values you chose as the cutoffs 
#for the three house sizes, the cost for each size and the prices for each cleaning 
#type in your comments as well.

#Submit your Python program as a text file (.py) file. In addition, submit a Design 
#outline and a Test plan/report (3 different test cases) in a Word document or a 
#PDF file, and include a screenshot of execution of your program for each test case. 

#Your submission must also adhere to the Submission Requirements 
#document (i.e., Filename and display your name, class, date in the output).

def main():
#

#prompt users for values needed to calculate cost
    print("""We have two approaches to cleaning. If you prefer, we can
      do a deep clean; we will require that all members are out of the
      house for an extended period of time (8 hours+) while we devote
      a large amount of effort to deep cleaning the house. This 'bulk'
      purchase will reduce certain costs. The other option, a general
      cleaning, typically lasts for no more than 4 hours, does not require
      anyone to be out of the house, and runs the standard rate.\n\n""")
    

#calculation process based on user decision
    cleanChoice()
    

#functions
def cleanChoice():
    choice = input("Please type 1 for standard cleaning and 2 for deepcleaning\n")
    if (choice == "1"):
        roomCount()
    elif (choice == "2"):
        deepCleanCalc()
    else:
        cleanChoice()
        

#regular constants
ENTRY_WAY_COST = 20
KITCHEN_COST = 25
LIVING_ROOM_COST = 30
DINING_ROOM_COST = 30
FULL_BATH_COST = 25
HALF_BATH_COST = 15
GARAGE_COST = 35
STUDY_COST = 20
SUN_ROOM_COST = 25
HALLWAY_COST = 10
STEPS_COST = 10

#regular calculations
def roomCount():
    total = 0;
    roomTotal = eval(input("How many rooms would you like cleaned?\n"))
    while roomTotal > 0:
        total += roomAsk()
        roomTotal -= 1
    print("\nThe total cost will be", total)


#inner function for querying room type
def roomAsk():
    #ask nunmber of times based on room number entered
    total = 0
    room = input("""Please enter the room type to be cleaned:
    entry way (1), kitchen (2), living room(3),
    dining room(4), full bath(5), half bath(6),
    garage(7), study(8), sun room(9), hallway(10), steps(11)
    """)

    
    #provide option/description based on verbal or numerical entry
    if (room == "entry way".lower()):
        total += ENTRY_WAY_COST
        print(room.lower + ":", ENTRY_WAY_COST)
    elif (room == "1"):
        total += ENTRY_WAY_COST
        print("entry way:", ENTRY_WAY_COST)
        #KITCHEN
    elif (room == "kitchen".lower()):
        total += KITCHEN_COST
        print(room.lower + ":", KITCHEN_COST)
    elif (room == "2"):
        total += KITCHEN_COST
        print("entry way:", KITCHEN_COST)
        #LIVING ROOM
    elif (room == "living room".lower()):
        total += LIVING_ROOM_COST
        print(room.lower + ":", LIVING_ROOM_COST)
    elif (room == "3"):
        total += LIVING_ROOM_COST
        print("living room:", LIVING_ROOM_COST)
        #DINING ROOM
    elif (room == "dining room".lower()):
        total += DINING_ROOM_COST
        print(room.lower + ":", DINING_ROOM_COST)
    elif (room == "4"):
        total += DINING_ROOM_COST
        print("dining room:", DINING_ROOM_COST)
        #FULL BATH
    elif (room == "full bath".lower()):
        total += DINING_ROOM_COST
        print(room.lower + ":", FULL_BATH_COST)
    elif (room == "5"):
        total += FULL_BATH_COST
        print("full bath:", FULL_BATH_COST)
        #HALF BATH
    elif (room == "half bath".lower()):
        total += HALF_BATH_COST
        print(room.lower + ":", HALF_BATH_COST)
    elif (room == "6"):
        total += HALF_BATH_COST
        print("half bath:", HALF_BATH_COST)
        #GARAGE
    elif (room == "garage".lower()):
        total += GARAGE_COST
        print(room.lower + ":", GARAGE_COST)
    elif (room == "7"):
        total += GARAGE_COST
        print("garage:", GARAGE_COST)
        #STUDY
    elif (room == "study".lower()):
        total += STUDY_COST
        print(room.lower + ":", STUDY_COST)
    elif (room == "8"):
        total += STUDY_COST
        print("entry way:", KITCHEN_COST)
        #SUN ROOM
    elif (room == "sun room".lower()):
        total += SUN_ROOM_COST
        print(room.lower + ":", SUN_ROOM_COST)
    elif (room == "9"):
        total += SUN_ROOM_COST
        print("run room:", SUN_ROOM_COST)
        #HALLWAY
    elif (room == "hallway".lower()):
        total += HALLWAY_COST
        print(room.lower + ":", HALLWAY_COST)
    elif (room == "10"):
        total += HALLWAY_COST
        print("hallway:", HALLWAY_COST)
        #STEPS

        #
    else:
        print("""Please choose a valid room type or enter the associated number:
                entry way: 1,
                kitchen: 2,
                living room: 3,
                dining room: 4,
                full bath: 5,
                half bath: 6,
                garage: 7,
                study: 8,
                sun room: 9,
                hallway: 10,
                steps: 11
              """)

    return total
    
    

#deep-clean constants
#small
LOW = 1500
MED = 2500
#large

#deep-clean calculations

def deepCleanCalc():
    sqFt = eval(input("What is the square footage of the house?\n"))
    #calc cost and account for minimum pay
    if sqFt < LOW and sqFt * .15 <= 200:
        print("The total cost will be $200")
    elif sqFt < LOW and sqFt * .15 > 200:
        print("The total cost will be $%2d" % (sqFt * .15))
    elif sqFt < MED:
        print("The total cost will be $%2d" % (sqFt * .35))
    else:
        print("The total cost will be $%2d" % (sqFt * .55))
    
    
main()
