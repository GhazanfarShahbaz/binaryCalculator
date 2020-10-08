def decimalToBase(decimal: int or str or float, base = 2) -> str:
    """Cobverts decimal numbers to a specific base
    Parameters: Base and decimal should both be integers"""
    bitConversion = ""
    KEY = 55                                          # For ASCII conversion

    print(decimal)
    if '.' in str(decimal) and base == 2:             # Only for base 2 atm
        bitConversion += "." + decimalPart(str(decimal))
        decimal = str(decimal)
        decimal = decimal[:decimal.find(".")]
    if type(decimal) is not int:
        decimal = int(decimal)

    while decimal >= base:
        bitConversion = f"{bitToBase(decimal % base)}{bitConversion}"
        decimal = int(decimal/base)

    if decimal > 0:
        bitConversion = f"{bitToBase(decimal)}{bitConversion}"

    return bitConversion


def bitToBase(value: int):
    KEY = 55
    if(value <= 9):
        return str(value)
    return str(chr(KEY + value))


def decimalPart(decimal: str) -> str:
    decimalPart = float(decimal) - float(decimal[:decimal.find('.')])
    conversion = ""

    for x in range(8):
        decimalPart *= 2
        if decimalPart >= 1:
            conversion += "1"
            decimalPart = decimalPart - int(decimalPart)
        else:
            conversion += "0"

    return conversion


def bitToDecimal(bit: str or int, base=2) -> int:
    """Converts bit to its coressponding decimal value
    Paramters: bit, a string value and base an integer value"""
    KEY = 55 
    conversion = 0
    negative = False
    bitLength = len(bit)

    if type(bit) is not str:
        bit = str(bit)
    
    if bit and bit[0] == "-":
        negative = True
        bit = bit[1:]
 
    if(not validityCheck(bit, base)):
        print("This is not a valid value for the specified base")
        while(not validityCheck(bit, base)):
            base = int(input(f"Please enter a base that corresponds to the bit {bit} : "))

    for x in range(0, bitLength):
        if(int(ord(bit[x])-KEY) <= 9):
            conversion += int(bit[x])*pow(base, bitLength-x-1)
        else:
            conversion += int(ord(bit[x])-KEY)*pow(base, bitLength-x-1)

    if negative:
        conversion = convertBase*-1

    return conversion


def validityCheck(bit: str, base: int) -> bool:
    """Checks if the bit value coressponds to the base"""
    KEY = 55

    for x in bit:
        currNumber = 0
        if(int(ord(x)-KEY) > 9):
            currNumber = int(ord(x)-KEY)
        else:
            currNumber = int(x)

        if(currNumber >= base):
            return False

    return True


def binary_addition(binaryOne: int or str, binaryTwo, base=2) -> str:
    return decimalToBase(bitToDecimal(binaryOne, base) + bitToDecimal(binaryTwo, base), base)


def binary_subtraction(binaryOne: int or str, binaryTwo: int or str, base = 2) -> str:
    output = decimalToBase(bitToDecimal(binaryOne, base) - bitToDecimal(binaryTwo, base), base)
    if not output:
        return "0"
    return output

def binary_multiplication(binaryOne: int or str, binaryTwo: int or str, base = 2):
    return decimalToBase(bitToDecimal(binaryOne, base) * bitToDecimal(binaryTwo, base), base)

def binary_division(binaryOne: int or str, binaryTwo: int or str, base = 2):
    output = decimalToBase(bitToDecimal(binaryOne, base)/bitToDecimal(binaryTwo, base), base)
    if not output:
        return "0"
    return output

def operation_gate(binaryOne: int or str, binaryTwo: int or str, operation, baseOne=2, baseTwo=2):
    baseOne = int(baseOne)
    baseTwo = int(baseTwo)
    if baseOne != baseTwo:
        binaryTwo = convertBase(binaryTwo, baseTwo, baseOne)
    
    if operation == "+":
        return binary_addition(binaryOne, binaryTwo, baseOne)
    elif operation == "-":
        return binary_subtraction(binaryOne, binaryTwo, baseOne)
    else:
        return binary_multiplication(binaryOne, binaryTwo, baseOne)




def greater_bit(bitOne: int or str, bitTwo: int or str, base=2) -> int or str:
    if(int(bitToDecimal(bitOne, base)) > int(bitToDecimal(bitTwo, base))):
        return bitOne
    return bitTwo

def format(bit: int or str)-> str:
    val = str(bit)
    ph = ""
    for x in range(len(val)):
        ph += str(val[len(val)-1-x])
        if (x+1)%4 == 0:
            ph += " "
    
    return ph[::-1].strip()


def complement(binary: str or int, base = 2, complement = 1) -> str:
    if type(binary) != str:
        binary = str(binary)

    maxBin = ""
    KEY = 55

    for x in range(len(binary)):
        if(binary[x] == "."):
            maxBin += "."
            continue
        if base <= 9:
            maxBin += f"{base-1}"
        else:
            maxBin += chr(KEY + base-1)

    onesComplement = binary_subtraction(maxBin, binary, base)

    while len(onesComplement) < len(binary):
        onesComplement = f"0{onesComplement}"
    
    if complement == 2:
        return binary_addition(onesComplement, "1", base)
    return onesComplement


def convertBase(binary: str or int, base: int, newBase) -> str:
    return decimalToBase(bitToDecimal(binary, base), newBase)



if __name__ == "__main__":
    for x in range(100000):
        if x%10000 == 0:
            print(f"On test {x}")
        for y in range(2, 30):
            if x != bitToDecimal(decimalToBase(x,y), y):
                print("TEST FAILED")
        # print(x, bitToDecimal(decimalToBase(x)), bitToDecimal(decimalToBase(x, 3),3), bitToDecimal(decimalToBase(x, 4),4), bitToDecimal(decimalToBase(x, 8),8), bitToDecimal(decimalToBase(x, 16),16))
    # INPUTS
    # print(format(binary_addition(input(), "FF34", 16)))
    # print(binary_subtraction(2214, 6674, 8))
    # print(bitToDecimal("FFFFFA",16))
    # print(complement(binary_addition(complement("2214", base = 8), 2020, 8),8))
    # print(validityCheck("FFFFFFF", base =17))
    # print(convertBase("0111111111111111111111010",2,16))