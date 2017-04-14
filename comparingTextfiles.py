#
# Problem:
# Take two files and compare the lines that exist in the files.
# The two files provided are: old_file.txt and new_file.txt.
#
# The files have lines that look like this:
# TAG : field- list
#
# You should create as Python program that compares each tag and for tags that match, compares
# each space-separated field. The output should be a list of the tags that are in both files and a comparison
# of the fields that are common, only in the old or only in the new
#
# Suppress tags where there is an exact match
#
# For example, given the two lines:
# C_LINK_CMD: lnk2000 - q - c - w - x - -heap = 0x800 - -stack = 0x400 - m link.map
# C_LINK_CMD: cl2000 - g - z - w - x - -heap = 0x800 - -stack = 0x400 - m link.map
#
# Your output should look like this:
# Tag # Name: C_LINK_CMD

# Existing Values:  lnk2000 -q -c -w -x - -heap = 0x800 - -stack = 0x400 - m link.map
# New Values:  cl2000 -g -z -w -x - -heap = 0x800 - -stack = 0x400 - m link.map
# Fields Omitted: lnk2000 - q - c
# Fields Added: cl2000 - g - z
#
#Please sort the output by tag name

#                                   Antonios Tsamourtzis 3/17/2017
# The logic behind my solution is:
#
#   1. Pass the two text files separately into dictionaries with the "TAG" as the key and the field-list as the "VALUE"
#   2. Then the comparisons start:
#       i) I compared the tags between the two files
#       ii) When a TAG match is found I split the fields-lists when a space is encountered
#       iii) Then only in the case that the field-lists between the two files are different check the values
#            by turning the fields into set and comparing them. That's how I checked what has been added and what
#            has been omitted.
#   3. Finally I set timers at the beginning of my comparison function to check the efficiency of my solution.
#      My results where somewhere between 0.00059 and 0.00093 seconds, for the two files that contain
#      between 75 and 90 lines of data. The program is efficient for small data files, but for files with hundreds of
#      thousands of lines it would take between 8 and 10 seconds for the same process.


import time

oldFile = open("/Users/antonishg/Desktop/Old_File.txt", "r")
oldFile = oldFile.readlines()
newFile = open("/Users/antonishg/Desktop/New_File.txt", "r")
newFile = newFile.readlines()

oldDict = {}
newDict = {}


def oldFileListing():
    for i in oldFile:
        i.split("\n")
        oldTag, oldFieldList = i.strip("\n").split(":")
        oldDict[oldTag]= oldFieldList
    return oldDict


def newFileListing():
    for j in newFile:
        j.split("\n")
        newTag, newFieldList = j.strip("\n").split(":")
        newDict[newTag] = newFieldList
    return newDict


def comparisons():

    oldDictionary = oldFileListing()
    newDictionary = newFileListing()
    t0 = time.time()
    for key in oldDictionary:
        if key in newDictionary:
            oldFields = oldDictionary[key].split("\n")
            for j in oldFields:
                oldFieldsSplit = j.split(" ")

            newFields = newDictionary[key].split("\n")
            for i in newFields:
                newFieldsSplit = i.split(" ")

            if set(oldFieldsSplit) != set(newFieldsSplit):
                print("\nTAG:", key)
                print("Existing Values: ", oldFieldsSplit)
                print("New Values: ", newFieldsSplit)
                if oldFieldsSplit not in newFieldsSplit:
                    added = (set(newFieldsSplit) - set(oldFieldsSplit))
                    if added != set():
                        print("ADDED:", added)

                if newFieldsSplit not in oldFieldsSplit:
                    omitted = (set(oldFieldsSplit) - set(newFieldsSplit))
                    if omitted != set():
                        print("OMITTED:", omitted)
    t1 = time.time()
    totalTime = t1 - t0
    print('\n\n\nTotal Time Elapsed:', totalTime, "seconds")


comparisons()