import string
import random


def getLowerAlp():
    lowerAlp = random.choice(string.ascii_lowercase)
    return lowerAlp


def getHighAlp():
    highAlp = random.choice(string.ascii_uppercase)
    return highAlp


def getDigit():
    digit = random.randint(0, 9)
    return digit


def getSymbol():
    symbols = string.punctuation
    symbols = symbols.replace(" ", "")
    symbols = symbols.replace("=", "")
    sym = random.choice(symbols)
    return sym


def pinGen(size):
    if size < 8:  # fixing the size of pin
        size = 8
    hasDigit = hasLowerAlp = hasSym = hasHighAlp = False
    genPassword = []
    for i in range(size):
        if (i == (size/4)-1) or (i == (size/2) - 1) or (i == 3*(size/4) - 1) or (i == size - 1):
            if not hasSym:
                nextDigit = getSymbol()
                hasSym = True
            elif not hasDigit:
                nextDigit = getDigit()
                hasDigit = True
            elif not hasLowerAlp:
                nextDigit = getLowerAlp()
                hasLowerAlp = True
            elif not hasHighAlp:
                nextDigit = getHighAlp()
                hasHighAlp = True
        else:
            digitDecider = (random.randint(1, 100) % 2)
            nextDigit = ""
            if digitDecider:  # this will decide whether the next element will be a Digit or an alphabet/Symbol
                nextDigit = getDigit()
                hasDigit = True
            else:
                symDecider = (random.randint(1, 100) % 2)
                if symDecider:  # this will decide whether the next element will be a symbol or an alphabet
                    alpDecider = (random.randint(1, 100) % 2)
                    if alpDecider:  # this will decide whether the next element will be a uppercase or lowercase
                        nextDigit = getHighAlp()
                        hasHighAlp = True
                    else:
                        nextDigit = getLowerAlp()
                        hasLowerAlp = True
                else:
                    nextDigit = getSymbol()
                    hasSym = True
        genPassword.append(nextDigit)
    genPassword = ''.join([str(i) for i in genPassword])    # Converting list to string using comprehension
    return genPassword


pinSize = int(input("Enter the size of pin\n"))
print(pinGen(pinSize))
