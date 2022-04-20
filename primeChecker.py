import random

def main():
    keepGoing = True
    while keepGoing == True:
        numToCheck = int(input("\n\nPlease enter the number you wish to check for Primality: "))
        if checkPrime(numToCheck) == False:
            print("\n"+str(numToCheck)+" Is not a Prime Number\n\n")
        else:
            print("\n"+str(numToCheck)+" Is a Prime Number\n\n")
        continueCheck = input("If you wish to Exit please enter 'EXIT' : ")
        if continueCheck.upper() == "EXIT":
            keepGoing = False
    return

def checkPrime(newNum):
    if newNum == 1:
        return False
    if newNum % 2 == 0:
        return False
    for i in range(newNum):
        if i == 1:
            continue
        if i % 2 == 0:
            continue
        elif newNum % i == 0:
            return False
    
    return True

main()