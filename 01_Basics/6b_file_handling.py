# ============ File handling in python =================
# 1. r =Read
# 2. a = Append
# 3. w = write
# 4. X = create


# 1. Reading a file
print("============== 1.  REading============")
# f = open("predictions.txt")
# # print(f.read(5))
# # print(f.readline())

# for line in f:
#     print(line)

# f.close()

try:
    f = open("name.txt")
    print(f.read())
except:
    print("The file you want to read doesn't exist")
finally:
    f.close()


# ============ Append-- create the file if it doesn't exist
print("========== Apend and writing ============")
# f = open("schools.txt", "a")
# f.write("Tennessee Tech University\n")
# f.write("Moscow Institute of Physics and Technology\n")
# f.close()

# # read the new file
# f = open("schools.txt")
# print(f.read())
# f.close()


# ======= Write (overwrite) =========
f = open("name.txt", "w")
f.write("i deleted all names in the names.txt")
f.write("======== newly added ======== \n")
f.write("1. Anthony\n2. John \n3.  Peter \n4. Luke \n5. Alex \n6. Aton ")
f.close()

f = open("name.txt")
print(f.read())
f.close()
