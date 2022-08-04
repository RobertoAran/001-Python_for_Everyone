# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
pas = True
numPositionArrayCero = 0
numConfidenceTotal = 0
numSearch = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    if pas:
        numPositionArrayCero = line.find("0")
        print(numPositionArrayCero)
        pas = False
    numConfidenceTotal = numConfidenceTotal + int(line[numPositionArrayCero])
    print(numPositionArrayCero)
    print(numConfidenceTotal)
print("Done")
