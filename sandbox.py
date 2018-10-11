#! usr/bin/python
## Performs Subtraction operation
def subtraction(product,mcand):
    carry = 0;
    prime_product = product[:4]
    final_product = ""
    for i in range(len(prime_product)-1,-1,-1):
        print(i)
        if (mcand[i] == "0" and prime_product[i] == "0"):
            if (carry == 1):
                final_product = "1" + final_product
            else:
                final_product = "0" + final_product
        elif (mcand[i] == "1" and prime_product[i] == "0"):
            if (carry == 1):
                final_product = "0" + final_product
            else:
                final_product = "1" + final_product
                carry = 1
        elif (mcand[i] == "0" and prime_product[i] == "1"):
            if (carry == 1):
                final_product = "0" + final_product
                #Not really sure what happens to "carry" here
                carry = 0
            else:
                final_product = "0" + final_product
        elif (mcand[i] == "1" and prime_product[i] == "1"):
            if (carry == 1):
                final_product = "1" + final_product
                #Again, not sure if this is what really happens to carry
                carry = 0
            else:
                final_product = "0" + final_product
        else:
            print("An error has occurred when subtracting: Exiting program")
            return 0

    return final_product + product[5:]


input1 = input("Enter number 1: ")
input2 = input("Enter number 2: ")
output = subtraction(input1,input2)
print(output)
