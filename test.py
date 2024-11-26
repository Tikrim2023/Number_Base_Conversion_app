def number_to_decimal(number, base):

    decimal = int(number, base)

    binary = bin(decimal)
    octal = oct(decimal)
    hexadecimal = hex(decimal)

    print("decimal: " + str(decimal))
    print("Binary: " + str(binary[2:]))
    print("octal: " + str(octal[2:]))
    print("hexadecimal: " + str(hexadecimal[2:]))

number = str(input("Enter a number: "))
base = 2

number_to_decimal(number,base)
