# Determine if a string is a palindrome!

def is_palindrome(test):
    test = test.lower()  # convert to lower

    # strip al the spaces and punctuations
    strr = [""]
    for s in test:
        if s.isalnum():
            strr.append(s)

    newstr = ''.join(strr)
    # now calculate the reverse of the string

    return newstr, "  ==  ", newstr[::1] == newstr[::-1]


test_word1 = "MadAm, I'm Adam."
test_word2 = "RACE CAR!"
test_word3 = "Hello, world"
test_word4 = "Radar?"
test_word5 = "A man, a plan, a canal Panama!"

print(f"test word 1:  {is_palindrome(test_word1)}")
print(f"test word 2:  {is_palindrome(test_word2)}")
print(f"test word 3: {is_palindrome(test_word3)}")
print(f"test word 4: {is_palindrome(test_word4)}")
print(f"test word 5: {is_palindrome(test_word5)}")
