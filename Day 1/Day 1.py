#to open file
f = open("C:\\Users\\kso\\PycharmProjects\\AdventOfCode\\Day1Input.txt", "r")

#create list to insert file into
freq = []

for line in f:
    line = line.split()
    if line:
        line = [int(i) for i in line]
        freq.append(line)

print(freq)

#PART 1

total = 0
for i in freq:
    total += sum(i)
print(total)


#PART 2

freqresult = []
total = 0
x = 0

while x == 0:
    for i in freq:
        total += sum(i)
        if total in freqresult:
            x = 1
            break
        else:
            freqresult.append(total)

print(total)