Output_file = open("results.txt","w")
def binary_converter(number):
    binary = ""
    number = int(number)
    if int(number) == 0:
        binary = "0"
    elif int(number) > 0:
        while number != 0:
            reminder = number % 2
            binary = (str(reminder) + binary)
            number = number // 2
    return binary





def Binary_read():
    Binary_file = open("binary.txt","r")
    for line in Binary_file:
        print(line)
    Binary_file.close
def Decimal_read():
    Decimal_file = open("Decimal.txt","r")
    for l in Decimal_file:
        number = (binary_converter(l))
        
        Converted_Binary.append(number)
    Decimal_file.close
Converted_decimals = []
Converted_Binary = []
Decimal_read()
Output_file = open("results.txt","w")
for numbers in Converted_Binary:
    Output_file.write(str(numbers) + "\n")
Output_file.close()

Decimal_read()
print(Converted_Binary)