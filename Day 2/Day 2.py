# list
# key value = dictionary
# set = set(list) = unique list

#to open file
#f = open(r"C:\Users\kso\PycharmProjects\AdventOfCode2018\Day 2\Day2Input.txt", "r")
#
# #PART 1
#
# # counter
# twocount = 0
# threecount = 0
#
# for line in f:
#     #print(line.replace("\n", ""))
#     count = {}
#     for s in line:
#         count[s] = line.count(s)
#     if 2 in count.values():
#         twocount += 1
#     if 3 in count.values():
#         threecount +=1
#     else:
#         pass
#
# print ('two count:', twocount)
# print ('three count:', threecount)
# print (twocount*threecount)

#PART 2

file = open(r"C:\Users\kso\PycharmProjects\AdventOfCode2018\Day 2\Day2Input.txt", "r")
ids = file.readlines()

toggle = 0 #use this as toggle to get out of word one-loop

for wordone in ids:

    wordoneclean = wordone.replace("\n", "") #to take out the space at end of lines

    for wordtwo in ids: #for every word in list to compare to (p is word comparing to)

        wordtwoclean = wordtwo.replace("\n", "") #to take out the space at end of lines

        count = 0 #set count here before it loops through letters

        for k, c in enumerate(wordtwoclean):
            if wordoneclean[k] != wordtwoclean[k]:
                count += 1

        if count == 1:#set if statement outside of loop, because once end loop, then can check what total count is
            toggle = 1 #set toggle to 1 to break word one-loop
            print(wordoneclean, wordtwoclean) #the two words that only have 1 letter different
            break #to get out of word two-loop

    if toggle == 1:
        break

#need to have it read and produce all the letters that are the same