# Sequences: LIst and tuples

mylist = [0, 1, 2, "one", False]
print("my list is : ", mylist)
print("length of list: ", len(mylist))

# indexing
# print(mylist[2])  # value at i=3
# print(mylist[-1])  # last values
# mylist[0] = 100  # changing values at i=0
# print(mylist)

# adding list to another lsit
# mylist2 = [22, 44, 55, 66]
# mylist = mylist + mylist2
# print(mylist)

# Treating Springs as lists
mystr = "Hello I'm getting this Amazon Research Scientist position for Mum"
print(mystr)
print(mystr[2:10])


# list slicing
print("============== LIST SLICING =================")
print(mystr[1:15])
print(mystr[::-1]) # reversing a sequence




print("=========== Tuples: are immutable lists (can't be changed when created)")
mytuple = (0, 1, 2, "three")
print(mytuple)



# SEts
print("========= sets =====enforce uniqueness in values and set don't suppor indexing")
myset = {1,2,3,3,4,5}
print(myset)

