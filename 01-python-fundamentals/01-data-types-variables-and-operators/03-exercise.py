# * Create four variables.
#     * Assign numeric values to two of them.
#     * Assign string data to one of them.
#     * Assign a boolean value to one of them.
# * Add the two numbers together and store the result in a new variable.
# * Use string concatenation to add some text to the string variable and store the result back into the original variable.
#     * Hint `+=` works for strings too!
# * Use the "not" operator `not` on your boolean variable and see what it does.
#     * Hint: If your variable is named `the_truth` then try `print(not the_truth)`
# * Try to use the `+` operator with variables that don't have the same type. Specifically try all of these combinations:
#     * Combine the boolean and a number.
#     * Combine a string and a number.
#     * Combine a string and a boolean.
#     * What happens when you run the code?
#     * Is it the same for each combination?
#     * Can you explain the behavior you're witnessing?
#         * **Hone your research skills:** search the internet for more information...

a = 10
b = 10.5
c = "this is a " 
d = True

e = a + b
c += "string"
print(not d)

print(a+d)
    #we assume true/false = 1/0 when adding to integers 
#print(a+c)
    #addition is unsupported for string and integer
#print(c+d)
    #bool is unsupported for concat with string
#print(d+c)
    #additions is unsupported with bool variables

#https://stackoverflow.com/questions/38276843/true-true-2-elegantly-perform-boolean-arithmetic
    #true = 1, False = 0