# ================= Condiatinals and loops =====================

# comparing two values
a = int(input("Enter a: "))
b = int(input("Enter b: "))

if a < b:
    print(f" {a} is less than {b}")
elif a == b:
    print(f"{a} is equal to {b}")
else:
    print(f"{a} is greater than {b}")


# Using the if-else Construct

result = "greater" if a > b else "less than"
print(result)

age = int(input("Enter you age: "))
# age filtering
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)


# Using the add and or operator
income = int(input("Anual income: "))
credit = int(input("Enter credit score: "))
student = str(input("Are you a student? yes or no").lower())
high_income = True if income > 50000 else False
good_credit = True if credit > 800 else False
student = True if student == "yes" else False

print("========= Loan Eligibility =============")
if high_income and good_credit and not student:
    print("Eligible for Loan")

if not student:
    print("Not Eligible")
else:
    print("Not Eligible")
