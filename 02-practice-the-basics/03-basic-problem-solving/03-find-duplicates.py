"""
Complete this function such that it returns a new list
which contains all values that appear more than once in
the list passed into the function. Each duplicated value
should appear exactly once in the output list regardless
of how many times it is duplicated. 

If no items are duplicated, return an empty list. 
"""
import numbers


def duplicates(input_list):
    list_counts = {}
    duplicated_numbers = []
    for num in input_list:
        #check if number is already been used
        if num not in list_counts:
            list_counts[num] = 0
        #increase number usage count
        list_counts[num] += 1
    for nums, usage_count in list_counts.items():
        if usage_count > 1:
            duplicated_numbers.append(nums)
    return duplicated_numbers
    pass


# Very Simple Tests
# in Python == for two lists means "do the items in the list match exactly, order included"
assert duplicates([1, 2, 3, 1]) == [1]
assert duplicates([3, 3, 3, 3, 3]) == [3]

# Note the use of sorted here: your function can return the duplicates
# in any order, but calling sorted on them makes it easier to test the
# output. 
assert sorted(duplicates([1, 2, 3, 4, 1, 2, 3, 4])) == [1,2,3,4]
assert sorted(duplicates([1, 1, 2, 3, 3, 4])) == [1, 3]

## ADD AT LEAST 3 MORE TESTS ##
assert sorted(duplicates([10,44,32,22,19,16,15,15,44,10,32,16])) == [10, 15, 16, 32, 44]
assert duplicates(['a','b','c','d','a','c','b']) == ['a','b','c']
assert sorted(duplicates(['a','A','B','c','D','A','C','D','a'])) == ['A','D','a']
pass