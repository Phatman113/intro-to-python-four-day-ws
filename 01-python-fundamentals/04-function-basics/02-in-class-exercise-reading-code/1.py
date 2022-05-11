# What does this function do?
def mystery_function(things, specific_thing):
    for thing in things:
        if specific_thing == thing:
            return True

    return False

# What will this print when executed?
return_value = mystery_function([1,2,3,4,5], 4)
print(return_value)

#False,False,False,True,False
#I was wrong, I missed and thought it was outputting False each time

# What about this?
return_value = mystery_function([1,2,3,4,5], '4')
print(return_value)

# True
# I thought == could deal with string/int comparisons, that must be another operator I thinking of


# Run this code to check your answers.