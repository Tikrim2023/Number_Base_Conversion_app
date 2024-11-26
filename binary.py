def binary_to_other_base(number,base):

    binary = int(number,base)

    octal = oct(binary)

    print("octal: "+ str(octal))

number = str(input("Enter number: "))

base =2

binary_to_other_base(number,base)