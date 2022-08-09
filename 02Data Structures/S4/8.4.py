fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    splline = line.split()
    for spl in splline:
        if spl not in lst:
            lst.append(spl)
lst.sort()
print(lst)
