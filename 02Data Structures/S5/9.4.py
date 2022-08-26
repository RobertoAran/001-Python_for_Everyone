# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they
# appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a
# maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

senders = dict()

for line in handle:
    if line.startswith("From "):
        splline = line.split()
        spllineSender = splline[1]
        if spllineSender in senders.keys():
            senders[spllineSender] = senders[spllineSender] + 1
        else:
            senders[spllineSender] = 1

countBest = None
senderBest = None
for sender,count in senders.items():
    if countBest is None or count > countBest:
        senderBest = sender
        countBest = count
print(senderBest, countBest)