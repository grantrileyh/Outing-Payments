# Riley Grant
# January 8th, 2020
# ---------------
# This seeks to create a really easy way to calculate the minimum number of
# reimbursements between friends who went on a trip. Also to help my python.
#
# Run in python 2 through the terminal
# ---------------------------------------------------------------------------

# todo:
# - clean up code, comments, etc
# - make output list of how much each person paid
# - make output list of all debts of each person

# import library to be able to take input from user
from sys import argv

# ===== Define things =====

# a function to find the maximum value of the list
def myMax(valA, valB):
    if valA > valB:
        return valA
    else:
        return valB

# a function to find the minimum value of the list
def myMin(valA, valB):
    if valA < valB:
        return valA
    else:
        return valB

# a function to check if every single value in the list is close to 0
def allNonZeroHuh(listVal):
    for i in listVal:
        if i >= 0.05:
            return True
    return False

def myGive(indA, indB, listVal, listPlay):
    # while-loop until all equals out
    while allNonZeroHuh(listVal):
        valA = listVal[indA]
        valB = listVal[indB]
        personA = listPlay[indA]
        personB = listPlay[indB]
        # wooooo
        if indA > indB:
            print("broke immediately :(")
            break
        elif (valA + valB) == 0:
            print("\t* %r pays %r $%r" % (personB, personA, valB) )
            listVal[indA] = 0.00
            listVal[indB] = 0.00
            myGive(indA + 1, indB - 1, listVal, listPlay)
            # adjust values in list of moneys
        elif (valA + valB) > 0:
            valGive = -1 * valA
            print("\t* %r pays %r $%r" % (personB, personA, valGive) )
            listVal[indA] = 0.00
            listVal[indB] = round(valA + valB, 2)
            myGive(indA + 1, indB, listVal, listPlay)
        else: # (valA + valB) < 0:
            valGive = valB
            print("\t* %r pays %r $%r" % (personB, personA, valGive) )
            listVal[indA] = round(valA + valB, 2)
            listVal[indB] = 0.00
            myGive(indA, indB - 1, listVal, listPlay)

# ===== startup stuff =====
print("Type in the name of a person on the trip.")
print("Type 'done' if there are more people to add.")
# establish an two empty lists at the beginning
players = []
amt_player = []

# ===== get data from the user =====
while True:
    # set name to the input from the user
    name = raw_input("> ")
    # if user types done, break out of this loop
    if name == "done":
        break
    # otherwise, the user has inputted a name. Get how much money they owe
    else:
        print("and how much did %s pay" % (name) )
        paid = raw_input("> ")
        if paid == "done":
            break
        players.append(name)
        amt_player.append(float(paid))
        print("If there's another person, type their name, if not type 'done'.")

# ===== get the total number of people, and total cost =====
# get total number of goobers, and total sum
total_cost = sum(amt_player)
total_heads = len(amt_player)
# ez math for even split
even_split = round((total_cost / total_heads), 2)
total_heads_half = total_heads / 2

print("\n\nList of people and how much they spent:")
print(players)
print(amt_player)

# print out some text to user
print("\n$%r was the total cost of this trip." % total_cost)
print("%r people attended this outing of goobers." % total_heads)
print("Therefore, everyone should pay $%r to split the cost evenly." % even_split)
# calculate debts of each person, negative debt means you get money
i = 0
while i < total_heads:
    # print players.get(head)
        # something is fucky here
    amt_player[i] = round(even_split - amt_player[i], 2)
    i = i + 1

# sort both the lists concurrently, but sort based on values from amt_players[]
for i in range(1, total_heads):
    key = amt_player[i]
    keyA = players[i]
    j = i - 1
    while j >= 0 and key < amt_player[j] :
        amt_player[j+1] = amt_player[j]
        players[j+1] = players[j]
        j = j - 1
    amt_player[j+1] = key
    players[j+1] = keyA

# for me
print("\nList of people and their credit(-) / debt(+):")
print(players)
print(amt_player)

# ===== actually run function =====
# start function on both ends of list
i = 0
j = total_heads - 1
# print "i = %r, j = %r" % (i, j)
print("\nTo accomplish this in the least amount of transactions:\n")
myGive(i, j, amt_player, players)

print("\nThen everyone has paid %r total, and we all even!" % (even_split) )
print("\n   :))))))")
print("\n")
