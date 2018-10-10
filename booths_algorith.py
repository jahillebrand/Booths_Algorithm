#! usr/bin/python

def booths_algorithm():
    multiplicand_dec = input('Please enter your multiplicand: ')
    multiplier_dec = input('Please enter your multiplier: ')
    twos_complement(multiplicand_dec)
    twos_complement(multiplier_dec)
    return

def twos_complement(dec):
    """ binint = "{0:b}".format(int(dec[1:])) #convert to binary
    print(binint)
    flipped = bin(~int(binint,2))
    print(flipped)
    twos_complement = bin(int(flipped[1:],2) + int('1',2))
    print(twos_complement)
    print(type(twos_complement))"""
    adjusted = abs(int(dec) + 1)
    print(adjusted)
    binint = "{0:b}".format(adjusted)
    print(binint)
    flipped = flip(binint)
    print(flipped)
    for i in range(8-len(flipped)):
        signed_value = "1" + flipped
    print(signed_value)
    return

def flip(string):
    flipped_string = ""

    for bit in string:
        if bit == "1":
            flipped_string += "0"
        else:
            flipped_string += "1"
    
    return flipped_string


booths_algorithm()
