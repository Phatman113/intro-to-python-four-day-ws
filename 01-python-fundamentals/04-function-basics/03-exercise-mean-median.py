def mean(list1):
    list1_length = len(list1)
    list1_sum = sum(list1)
    return list1_sum/list1_length

numbers = [5, 10, 15]
m = mean(numbers)
print(m) # 10

pass


def median(list2):
    list2_length = len(list2)
    list2_sorted = sorted(list2)
    list2_is_even = list2_length % 2 == 0
    if list2_is_even == True:
        middle_2 = [list2_sorted[int(list2_length/2)],list2_sorted[int(list2_length/2)-1]]
        #return sum(middle_2)/len(middle_2)
        return mean(middle_2)
    else:
        median_entry = int(list2_length/2)
        return list2_sorted[median_entry]


numbers = [5, 10, 15,20,18,32,4,8]
med = median(numbers)
print(med) # 10
