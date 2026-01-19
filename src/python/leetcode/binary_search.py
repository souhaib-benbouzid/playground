class Solution:
    def binarySearch(self, list, value):
        first = 0
        last = len(list) - 1
        
        while first < last: 
            # find mid point 
            mid = (first + last) // 2
            if list[mid] == value:
                return mid
            # if value is greater take left side
            if list[mid] < value:
                first = mid + 1    
            # take right side
            else: 
                last = mid - 1
        return None
        