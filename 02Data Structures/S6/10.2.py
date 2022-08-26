name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

hours = dict()

for line in handle:
    if line.startswith("From "):
        splline = line.split()
        spllinespelled = splline[5]
        splldata = spllinespelled.split(':')
        if splldata[0] in hours.keys():
            hours[splldata[0]] = hours[splldata[0]] + 1
        else:
            hours[splldata[0]] = + 1
sortdic = dict()
sortdic.update(sorted(hours.items()))
for x, y in sortdic.items():
    print(x, y)
