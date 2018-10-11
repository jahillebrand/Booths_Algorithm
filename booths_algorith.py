#! usr/bin/python

## MAIN
def booths_algorithm():
    #Gets Multiplicand
    multiplicand_dec = getInput("Mutiplicand")

    #Gets Multiplier
    multiplier_dec = getInput("Multiplier")

    #Converts Multiplicand
    multiplicand_bin = convertDec(multiplicand_dec)

    #Converts Multiplier
    multiplier_bin = convertDec(multiplier_dec)

    #Perform Booth's algorithm
    boothsTriumph(multiplicand_bin,multiplier_bin)
    return


## Parent function for logical process
def boothsTriumph(mcand, plier):
    #Create full product line for Booth's Algorithm
    product = "00000000" + plier + "0"

    #Display product line to user
    print(buildLine(0,mcand,product))

    #Iterate through Booth's Algorithm
    for i in range(0,8):
        ######MiliensOriginalIdea->leftOp(product)
        operation = product[len(product)-2:]
        product = perform_operation(product,mcand,operation)

    ##TODO
    #Print out final value in binary and decimal

    return

######TODO
## Perform the necessary algorithmic operation
def perform_operation(product,mcand,operation):
    if (operation == "00"):
        ##Do Nothing
    else if (operation == "01"):
        ##Product = Product + mcand

    else if (operation == "10"):
        ##Product = Product - mcand
    else if (operation == "11"):
        ##Do Nothing
    else:
        print("An error has occured when choosing operation: Exiting program")
        return 0
    ##Shift right!

##Adds the two binary strings
def binAdd(num, num2):
    product = ""
    for i in range(-1,-len(num)):
        if num[i] == "0" and num2[i] == "0":
            product = "0" + product
        elif num[i] #case 1 and 1
        else #case 0 and 1


## Shows step-by-step process
def buildLine(iteration, mcand, product, tail):
    line = "Step: " + str(iteration) + " | Multiplicand: " + mcand + " | Product: " \
    + product[0:17] + "|" + product[17]
    return line


## Formats numbers from decimal to binary
def convertDec(dec):
    # If the value is negative, calls twos_complement
    if int(dec)<0:
        bin = twos_complement(int(dec))
    # Else simply converts to binary
    else:
        bin = "{0:b}".format(int(dec))
        # Iterates through and makes the binary value 8
        for i in range(8-len(dec)):
            bin = "0" + bin
    return bin


## Gets input for for algorithm
def getInput(varName):
    #Request input
    boothIn = input('Please enter your ' + varName + ": ")

    #Parse input
    while int(boothIn)>127 or int(boothIn)<-128:
        print("Absolute value too big, please try again")
        boothIn = input('Please enter your ' + varName + ": ")
    return boothIn


## Converts negative numbers
def twos_complement(dec):
    #Convert to dec, adding 1, then removing negative
    adjusted = abs(int(dec) + 1)

    #Turns into binary number
    binint = "{0:b}".format(adjusted)

    #Flip bits
    flipped = flip(binint)

    # Iterates through and makes the binary value 8
    for i in range(8-len(flipped)):
        flipped = "1" + flipped
    return flipped



## Flips the bits into a string
def flip(string):
    flipped_string = ""

    for bit in string:
        if bit == "1":
            flipped_string += "0"
        else:
            flipped_string += "1"

    return flipped_string


## CALL MAIN
booths_algorithm()
