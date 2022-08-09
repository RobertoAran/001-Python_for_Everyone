# Use the file name   as the file name
fname = input("Enter file name: ")
fh = open(fname)
pas = True
numPositionArrayCero = 0
numConfidenceTotal = 0
numSearch = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        pas = True
        continue
    if pas:
        numSearch = numSearch + 1
        numPositionArrayCero = line.find("0")
        numPositionArrayCero = numPositionArrayCero - 1
        pas = False
        numConfidenceTotal = numConfidenceTotal + float(line[numPositionArrayCero:])
numConfidenceTotal = numConfidenceTotal / numSearch
print("Average spam confidence: " + str(numConfidenceTotal))
