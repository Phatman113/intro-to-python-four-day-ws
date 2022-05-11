# This function doesn't return anything, but it does print a
# lot of stuff. Before you run this function, predict what it
# will print.

def loops_in_loops():
    c = 0

    for i in range(10):
        for j in range(10):
            print(i, j, c)
            c += 1


loops_in_loops()

# If this result confuses you, simulate its execution by
# manually keeping track of the values in the variables 
# i, j and c as you step through the code line by line.

#I think i and j will count up, but i will count up one, then j for 9, then i for 1, then j for 9.  Should end up with c = 81? 
# I forgot it starts at 0, so it's 99


