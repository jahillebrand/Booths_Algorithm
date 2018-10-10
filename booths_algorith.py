#! usr/bin/python

def booths_algorithm():
    multiplicand_dec = input('Please enter your multiplicand: ')
    multiplier_dec = input('Please enter your multiplier: ')
    multiplicand_bin = twos_complement(multiplicand_dec)
    multiplier_bin = twos_complement(multiplier_dec)
    print(multiplicand_bin)
    print(multiplier_bin)
    return

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
#AHAHHAHAHAHAAHAH
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
