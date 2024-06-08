# Insertion-Sort
# Requirements
# The Insertion-sort function involves finding the correct place for a given element in a sorted list. 
# This process begins with comparing and sorting the first two elements. A third element is then compared 
# to the two previously sorted elements and found its proper position among them. This way, more elements 
# gradually added to a continuously sorted list by inserting them into their proper positions. 
# Write a program that sorts an array using the insertion-sort algorithm. 

# Follow these instructions to complete the mini-project.

#     Create a random list of numbers.
#     Start iterating over them and apply the sorting algorithm.
#     Print the sorted list.


def main():
    
    
    ls = [45, 2, 68, 7, 21, 9, 78, 3, 6, 26]
    print('Original Array:', ls)
    def sort(ls):
        n = len(ls)  
          
        if n <= 1: #Part that stops it when done
            return  
        
        else:
            for item in range(1, n):  
                temp = ls[item]  # Takes out the number being sorted
                x = item-1
                while x >= 0 and temp < ls[x]:  
                    ls[x+1] = ls[x]  
                    x -= 1
                ls[x+1] = temp  # Puts number back
      
    
    sort(ls)
    print('Array after sorting:', ls)

main()