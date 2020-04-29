
numbers = []

f = open('dane4.txt', 'r')
numbers = f.readlines()
ciag = ""
for n in numbers:
    ciag += str(int(n))

max = 0
start = None
end = None
test = None

for n in numbers:
    n = str(int(n))
    s2 = None
    count = 0
    for x in range(0, len(n)):
        if x != len(n)-1:
            s1 = abs(int(n[x])-int(n[x+1]))

            if s2 == s1 or s2 == None:
                end = n[x]
                count += 1
                if count > max:
                    max = count
                    start = n[0]
                    test = n
            else:
                count = 0


            s2 = s1

            # if s > max:
            #     max = s
            # if s < min:
            #     min = s

print("Maks: "+str(max+1)+", s: "+str(start)+", e: "+str(end))
print(test)