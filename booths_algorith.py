#! usr/bin/python

def booths_algorithm():
    #Gets Multiplicand
    multiplicand_dec = getInput("Mutiplicand")

    #Gets Multiplier
    multiplier_dec = getInput("Multiplier")

    #Converts Multiplicand
    multiplicand_bin = convertDec(multiplicand_dec)

    #Converts Multiplier
    multiplier_bin = convertDec(multiplier_dec)

    boothsTriumph(multiplicand_bin,multiplier_bin)
    return

#Parent function for logical process
def boothsTriumph(mcand, plier):
    product = "00000000" + plier + "0"
    print(buildLine(0,mcand,product))
    for i in range(0,8):
        leftOp(product)


#Shows step-by-step process
def buildLine(iteration, mcand, product, tail):
    line = "Step: " + str(iteration) + " | Multiplicand: " + mcand + " | Product: " \
    + product[0:17] + "|" + product[17]
    return line

#Formats numbers from decimal to binary
def convertDec(dec):
    if int(dec)<0:
        bin = twos_complement(int(dec))
    else:
        bin = "{0:b}".format(int(dec))
        # Iterates through and makes the binary value 8
        for i in range(8-len(dec)):
            bin = "0" + bin
    return bin

#Gets input for for algorithm
def getInput(varName):
    boothIn = input('Please enter your ' + varName + ": ")
    while int(boothIn)>127 or int(boothIn)<-128:
        print("Absolute value too big, please try again")
        boothIn = input('Please enter your ' + varName + ": ")
    return boothIn

#Converts negative numbers
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



#Flips the bits into a string
def flip(string):
    flipped_string = ""

    for bit in string:
        if bit == "1":
            flipped_string += "0"
        else:
            flipped_string += "1"

    return flipped_string


booths_algorithm()
