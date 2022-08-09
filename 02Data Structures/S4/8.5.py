fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
splline = ""
for line in fh:
    if line.startswith("From "):
        splline = line.split();
        print(splline[1])
        count = count + 1;
        continue
print("There were", count, "lines in the file with From as the first word")