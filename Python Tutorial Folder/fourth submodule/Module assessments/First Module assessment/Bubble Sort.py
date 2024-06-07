# Bubble Sort


# Requirements
# Bubble sort is a comparison-based algorithm in which each pair of adjacent elements is compared and swapped, 
# if they are not in order.
# Write a program that sorts an array ascendingly using bubble sort. 


# Create a random list of numbers.
# Start iterating over them and apply the sorting algorithm.
# Print the sorted list.

### Note: says ascendingly so least to greatest


def main():
    ls = [515, 151, 585, 412, 1265, 4, 11, 515, 15] # random numbers list
    #ls = [4,  11,  15,  151,  412,  515,  515,  585,  1265] #can uncomment this list and coment the other one to test already sorted list
    def Sort(ls):
        n = len(ls)
        
        for item in range(n):
            needsort = False # makes it so the default is as if the list was already sorted
            
            
            for x in range(0, n-item-1):
    
                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if ls[x] > ls[x + 1]: #determines if needs to be swapped
                    needsort = True
                    ls[x], ls[x + 1] = ls[x + 1], ls[x] #part that swaps it
    
            if needsort == False: #if list is already sorted, it just sends the list to print
                return
    
    
   
    
    
    Sort(ls)
    
    print("Sorted list is:")
    for i in range(len(ls)):
        print(ls[i], end=" ")
        
main()    