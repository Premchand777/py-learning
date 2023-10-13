mobileNumber = "9948123266"
numWords = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
repetitions = { 2: "Double", 3: "Tripple", 4: "Quadruple" }
output = ""
uniqueSet = set()

for index, digit in enumerate(mobileNumber):
    # 9
    if mobileNumber[index - 1] == digit:
        # "Nine" --> "DoubleNine"
        replaced = output.replace(numWords[int(digit)], repetitions[2] + numWords[int(digit)])
        output = replaced
    else:
        output += numWords[int(digit)]
        
print(output)