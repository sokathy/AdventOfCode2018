# list
# key value = dictionary
# set = set(list) = unique list

#to open file
f = open(r"C:\Users\kso\PycharmProjects\AdventOfCode2018\Day 2\Day2Input.txt", "r")

# counter
twocount = 0
threecount = 0

for line in f:
    #print(line.replace("\n", ""))
    count = {}
    for s in line:
        count[s] = line.count(s)
    if 2 in count.values():
        twocount += 1
    if 3 in count.values():
        threecount +=1
    else:
        pass

print ('two count:', twocount)
print ('three count:', threecount)
print (twocount*threecount)