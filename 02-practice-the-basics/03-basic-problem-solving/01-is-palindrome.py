"""
Complete this function such that it returns True if and only if
the string passed into this function is a palindrome, that is if 
it is the same string of characters forwards and in reverse. 
Return False otherwise. 
"""
def is_palindrome(input_string):
    # Delete pass, and put your code here.
    return input_string == input_string[::-1]

    #pass


# Very Simple Tests:
assert is_palindrome('racecar') == True
assert is_palindrome('battle') == False
assert is_palindrome('wasitabatisaw') == True
assert is_palindrome('a') == True
assert is_palindrome('abca') == False
## ADD AT LEAST 3 MORE TESTS ##
assert is_palindrome('alphbeticallacitebhpla') == True
assert is_palindrome('123454321') == True
assert is_palindrome('do spaces work krow secaps od') == True
assert is_palindrome('nope, this isn\'t') == False

## Just helpful to see, if this prints your tests all passed!
print("All tests passed.")