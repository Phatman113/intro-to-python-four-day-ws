"""
Complete this function such that it returns True if and only if
the two strings passed to the function are anagrams of each other,
that is if they contain the same letters the same number of times.
Return False otherwise.
"""
def is_anagram(string_a, string_b):
    return sorted(string_a) == sorted(string_b)
    pass


# Very Simple Tests
assert is_anagram('abba', 'aabb') == True
assert is_anagram('aab', 'bba') == False
assert is_anagram('the detectives', 'detect thieves') == True
assert is_anagram('abcde', 'abcdf') == False
## ADD AT LEAST 3 MORE TESTS ##
assert is_anagram('alphabet','phalbeta') == True
assert is_anagram('string_a','a_string') == True
assert is_anagram('123456987','987456321') == True
assert is_anagram('abcdefg','ABCDEFG') == False
assert is_anagram('AbCdEfG','aBcDeFg') == False
pass