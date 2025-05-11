# ===== Code Challenge ======
# Count the number of even or odd numbers in a list


def count_numbers(which, numbers):
    # Your code goes here
    lst = []
    if which == "even":
        for i in numbers:
            if i % 2 == 0:
                lst.append(i)
        return len(lst)
    elif which == "odd":
        for i in numbers:
            if i % 2 == 1:
                lst.append(i)
        return len(lst)
    else:
        if which != "odd" or "even":
            return -1


numbers = [7, 17, 2, 13, 19, 20, 0, 5, 11, 1280, 105]
# print(f"even count: {count_numbers("even", numbers)}")
ans = count_numbers("even", numbers)
print(f"even count: ", ans)

ans2 = count_numbers("odd", numbers)
print(f"odd counts: ", ans2)

ans3 = count_numbers("which", numbers)
print("none: ", ans3)
