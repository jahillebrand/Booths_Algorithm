#! usr/bin/python

def booths_algorithm():
    #Gets Multiplicand
    multiplicand_dec = getInput("Mutiplicand")
    print(multiplicand_dec)
    #Gets Multiplier
    multiplier_dec = getInput("Multiplier")
    print(multiplier_dec)

    #Converts Multiplicand
    if int(multiplicand_dec)<0:
        multiplicand_bin = twos_complement(int(multiplicand_dec))
    else:
        multiplicand_bin = "{0:b}".format(int(multiplicand_dec))
        # Iterates through and makes the binary value 8
        for i in range(8-len(multiplicand_dec)):
            multiplicand_bin = "0" + multiplicand_bin

    #Converts Multiplier
    if int(multiplier_dec)<0:
        multiplier_bin = twos_complement(int(multiplier_dec))
    else:
        multiplier_bin = "{0:b}".format(int(multiplier_dec))
        # Iterates through and makes the binary value 8
        for i in range(8-len(multiplier_bin)):
            multiplier_bin = "0" + multiplier_bin

    print("Multiplicand: " + multiplicand_bin)
    print("Multiplier: " + multiplier_bin)
    return

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
