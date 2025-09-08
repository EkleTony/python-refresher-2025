# ========== Valid Parenthenses ==============
"""Given a string s containing just the characters "(, ), { , } ] determine if the input strings is valid """

st = "[{()}]"
# Output: true ==================Explanation:  All the brackets are well-formed.


# def validParanthesis(Str):
#     # create a stack
#     st = []

#     # loop through each char in str and add to stack, if closing matches the existing pop esle continue
#     for s in Str:
#         if s == '(' or s == "{" or s == "[":
#             st.append(s)

#         else:
#             if st and ((st[-1]) == "(" and s == ")" or
#                        (st[-1]) == "{" and s == "}" or
#                        (st[-1]) == "[" and s == "]"):

#                 st.pop()
#             else:
#                 return False
#     return not st

# # time complexity is O(n) and space is O(n)


def validParanthesis2(st):
    # create a hashmap of para
    pairs = {")": "(",
             "]": "[",
             "}": "{"}
    stk = []
    for c in st:
        if c in pairs:  # i.e closing bracket
            stk.append(c)
        else:
            if not stk:
                return False
            else:
                popped = stk.pop()
                if popped != pairs[c]:
                    return False
    return not stk  # time: O(n)


# examples samples
print(validParanthesis2(st))
