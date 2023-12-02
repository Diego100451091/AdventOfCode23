''' ============= ADVENT OF CODE 2023 =============
| DAY 1 - Part 2
| By @Diego100451091
'''

codifiedValues = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

def readFile (path):
    file = open(path, "r")
    lines = file.readlines()
    file.close()
    return lines

def updateValues (first_value, last_value, value):
    if first_value == None:
        first_value = value
    else:
        last_value = value
    return first_value, last_value

def getValueCodified (codifiedValue):
    for code in codifiedValues.keys():
        if code in codifiedValue:
            return codifiedValues[code]
    return None

def getCalibrationValue(word):
    first_value, last_value = None, None
    currentCodifiedValue = ""

    for character in word:
        #Check if the character is not a number
        if not character.isdigit():
            currentCodifiedValue += character
            #Check if the currentCodifiedValue match with a codified value
            valueCodified = getValueCodified(currentCodifiedValue)
            if valueCodified:
                first_value, last_value = updateValues(first_value, last_value, valueCodified)
                #Preserve the last character in case of it could be in the next codified value
                currentCodifiedValue = currentCodifiedValue[-1]
        else:
            currentCodifiedValue = ""
            #Check if first_value is None
            first_value, last_value = updateValues(first_value, last_value, character)

    #Check if the currentCodifiedValue match with a codified value
    valueCodified = getValueCodified(currentCodifiedValue)
    if valueCodified:
        first_value, last_value = updateValues(first_value, last_value, valueCodified)

    #Check if last_value is None
    if last_value == None:
        last_value = first_value
    value = first_value + last_value
    return int(value)


def main():
    lines = readFile("../input.txt")
    calibration_value = 0
    for line in lines:
        calibration_value += getCalibrationValue(line)
    print("RESULT: ", calibration_value)

if __name__ == "__main__":
    main()
        