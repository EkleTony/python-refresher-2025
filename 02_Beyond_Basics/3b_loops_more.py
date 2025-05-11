# More on loops ====

days = ["Mon", "Tue", "Wed", "Thurs", "Fri", "Sat", "Sun"]
print("====== print all iterations ====")
for d in days:
    print(d)


print("===== break and continued keywords=====")

for d in days:
    if (d == "Fri"):
        break
    print(d)

print("print Continued: it skips the rest of that part of code====")
for d in days:
    if d == "Fri":
        continue
    print(d)


print(" ========= Enumerate Fnction to get an index and an item===")
for i, d in enumerate(days):
    print(i, d)

print()
print("               ====== multiplcation table with For Loop====           ")
print()
# Print headers for each table
for k in range(1, 9):
    print(f" Table {k} ", end="\t")
pri