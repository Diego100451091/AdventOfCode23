file = open("input.txt", "r")
outputFile = open("parsedInput.txt", "w")
lines = file.readlines()
# Write into output with " after and berofe each line but in the same line
for line in lines:
    outputFile.write("\"")
    outputFile.write(line.rstrip("\n"))
    outputFile.write("\"")
    outputFile.write(",")

file.close()
outputFile.close()