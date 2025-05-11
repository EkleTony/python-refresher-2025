# ============ Loops ====================

# 1. Whhile loop: executive if a certain condtion i true
x = 0
while x < 5:
    print(x, "Welcome to school! ")
    x += 1

print()
print("========== Stop conditions =============")

# ans = input("Should I stop? ").lower()
# while ans != "yes":
#     print(ans)
#     ans = input("should I stop? ").lower()


print()
print("====Multiplication Table ====")
# Nested While loop
i = 1
while i <= 12:
    # print(f"{i} times Table")
    j = 1
    while j <= 15:
        print(f"{i*j} ", end='\t')
        j += 1
    print()
    i += 1
