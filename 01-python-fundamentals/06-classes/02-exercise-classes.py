class Averages:
    def __init__(self, input_data):
        for nums in input_data:
            if type(nums) != (int or float):
                raise ValueError("This must be a list of numbers")
        self.input_list = sorted(input_data)
        self.length = len(self.input_list)
        self.sum = sum(self.input_list)
        self.is_even = self.length % 2 == 0
        
        
    def mean(self):
        return self.sum/self.length

    def median(self):
        if self.is_even == True:
            middle_2 = [self.input_list[int(self.length/2)],self.input_list[int(self.length/2)-1]]
        #return sum(middle_2)/len(middle_2)
            return sum(middle_2)/2
        else:
            median_entry = int(self.length/2)
            return self.input_list[median_entry]
    def mode(self):
        #mode is the most common element used in a list
        #Need error handling, should return all items if there are multiples that are tied for max
        #
        usage_counts = {}
        for item in self.input_list:
            #Check if item used before, add to count dictionary if not
            if item not in usage_counts:
                usage_counts[item] = 0
            #iterate usage count
            usage_counts[item] += 1
    
        #Find min/max in usage counts
        return max(usage_counts,key=usage_counts.get)
        

avgs = Averages([5,10,15,25,5])
print(avgs.mean()) # 12
print(avgs.median()) # 10
print(avgs.mode()) # 5
