# Working with Exceptions

# e.g 10/0 ===??
# 10/0  # ZeroDivisionError: division by zero

try:
    x = 10/0
except:
    print("coding not working!")


# printing the exact error message!
try:
    ans = input("What should i divide 10 by? ")
    num = int(ans)
    print(10/num)
except ZeroDivisionError as e:
    print("You can't divide by zero")
except ValueError as e:
    print("You didn't give me a valid number")
    print(e)
finally:
    print(f"Finally always runs")
    
st = "Hello, welcome homoe, boy"
print(list(st.split(",")))
