#! usr/bin/python

def booths_algorithm():
    #Gets Multiplicand
    multiplicand_dec = input('Please enter your multiplicand: ')
    while int(multiplicand_dec)>127 or int(multiplicand_dec)<-128:
        print("Absolute value too big, please try again")
        multiplicand_dec = input('Please enter your multiplicand: ')
    
    #Gets Multiplier
    multiplier_dec = input('Please enter your multiplier: ')
    while int(multiplier_dec)>127 or int(multiplier_dec)<-128:
        print("Absolute value too big, please try again")
        multiplier_dec = input('Please enter your multiplier: ')
    
    #Converts Multiplicand
    if int(multiplicand_dec)<0:
        multiplicand_bin = twos_complement(int(multiplicand_dec))
    else:
        multiplicand_bin = "{0:b}".format(int(multiplicand_dec))
    
    #Convertts Multiplier
    if int(multiplier_dec)<0:
        multiplier_bin = twos_complement(int(multiplier_dec))
    else:
        multiplier_bin = "{0:b}".format(int(multiplier_dec))


    print("Multiplicand: " + multiplicand_bin)
    print("Multiplier: " + multiplier_bin)
    return



#Converts negative numbers
def twos_complement(dec):
    #Convert to dec, adding 1, then removing negative
    adjusted = abs(int(dec) + 1)

    #Turns into binary number
    binint = "{0:b}".format(adjusted)

    #Flip bits
    flipped = flip(binint)
    
    # Iterates through and makes the binary value 4
    for i in range(4-len(flipped)):
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
