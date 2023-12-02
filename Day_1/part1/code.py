''' ============= ADVENT OF CODE 2023 =============
| DAY 1 - Part 1
| By @Diego100451091
'''

def readFile (path):
    file = open(path, "r")
    lines = file.readlines()
    file.close()
    return lines

def getCalibrationValue(word):
    first_value, last_value = None, None
    for character in word:
        #Check if the character is not a number
        if not character.isdigit():
            continue
        #Check if first_value is None
        if first_value == None:
            first_value = character
        else:
            last_value = character

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
    print(calibration_value)

if __name__ == "__main__":
    main()
        