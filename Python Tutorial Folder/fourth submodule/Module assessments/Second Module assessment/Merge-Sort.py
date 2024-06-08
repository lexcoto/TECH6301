# Merge-Sort

# Requirements
# Merge-sort first divides the array into equal halves, then combines them in a sorted manner. 
# Write a program that sorts the array using merge-sort algorithm. 

### Note: doesnt say how to sort it so going to assume least to most

# Follow these instructions to complete the mini-project.

#     Create a random list of numbers.
#     Start iterating over them and apply the sorting algorithm.
#     Print the sorted list.

def main():
    ls = [84, 57, 112, 68, 93, 68, 74, 12, 3, 59, 87, 52] 
    print("Original Array:", ls)
    def sort(ls):
        
        if len(ls)>1: #So it stops splitting when it gets to singles
            middle = len(ls)//2 #So it splits the list by whole integers
            half1 = ls[:middle] #before the center
            half2 = ls[middle:] #after the center
    
            sort(half1)
            sort(half2)
            item1=item2=x=0       
            while item1 < len(half1) and item2 < len(half2): 
                if half1[item1] < half2[item2]:
                    ls[x]=half1[item1]
                    item1=item1+1
                else:
                    ls[x]=half2[item2]
                    item2=item2+1
                x=x+1
    
            while item1 < len(half1):
                ls[x]=half1[item1]
                item1=item1+1
                x=x+1
    
            while item2 < len(half2):
                ls[x]=half2[item2]
                item2=item2+1
                x=x+1
        
    
    
    sort(ls)
    print("Array after sorting", ls)
    
main()