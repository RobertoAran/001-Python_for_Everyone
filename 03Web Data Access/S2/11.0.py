import re

name = "regex_sum_1600098.txt"
handle = open(name)

tot = 0
for line in handle:
    finded = ""
    line = line.rstrip()
    if re.search('[0-9]+', line):
        finded = re.findall('[0-9]+', line)
        for find in finded:
            tot = tot + int(find)
print(tot)
