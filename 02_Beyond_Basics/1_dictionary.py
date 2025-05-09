# ================ Dictionary Data Type ================
# Dict: had a key and the value, using key-value pair to associate data with a particular pair.

mydict = {"one": 1,
          "two": 2,
          "three": 3,
          "four": 4,
          5: "five",
          4.5: ["four", "point", "five"]
          }

# print my dict
# print(mydict)
# print()
# print("============ dict values via keys============")
# print(mydict["one"])
# print(mydict["three"])

# # making new keys
# mydict["Anthony"] = "A PhD Candidate in CS and focusing on AI and Graph Machine learning"

# print(mydict)
# print(mydict["Anthony"])


# To avoid calling non-existing keys

print("two" in mydict)
print("ten" in mydict)
print(mydict.keys())
print(mydict.values())


# ============= Iterating over all the iterms =================
print()
print("================== Items =================")
print(mydict.items())

print()
for key, val in mydict.items():
    print(key, val)
