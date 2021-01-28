# This was developed for as an assignment for the course work on py4e.com.
# The goal was to develop some code to search through a text file for email
# address's then to add them to a dictionary to later count them up and print
# off the email that shows up the most.  Below this is the actual assignment details

# 9.4 Write a program to read through the mbox-short.txt and figure out who has
# sent the greatest number of mail messages. The program looks for 'From ' lines
# and takes the second word of those lines as the person who sent the mail. The
# program creates a Python dictionary that maps the sender's mail address to a count
# of the number of times they appear in the file. After the dictionary is produced,
# the program reads through the dictionary using a maximum loop to find the most prolific committer.

# the file mbox-short.txt is included in this repository.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

di = dict()
for lne in handle:
    lne = lne.strip()
    lne = lne.split()
    if len(lne) < 3 or lne[0] != 'From' :
    	continue
    wds = lne[1]
    di[wds] = di.get(wds,0) + 1
    largest = -1
    theword = None
    for k,v in di.items():
        if v > largest:
            largest = v
            theword = k
print(theword, largest)
