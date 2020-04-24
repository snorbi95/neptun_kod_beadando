
list = []

f = open("triples_5.txt","r")
idx = 1
for line in f:
    if line != "\n":
        list.append(idx)
    idx += 1

idx = 1
for num in list:
    if idx % 20== 0:
        print("")
    else:
        print("{} ".format(num),end=(""))
    idx += 1