# Calculate the Average
# Requirements
# Write a function to calculate the average of the numbers in a list of items using the built-in sum function 

### Note: it doesnt specify so I assume it's just a list of random numbers and the result can be a float
### Note: Since it mentions "write a function" I'm interpreting this to mean they want the taking the average part to be its own function


# Follow these instructions to complete the mini-project.

#     Define your function.
#     Get the sum of the list.
#     Divide it by its length.

def main():
    ls= [5, 15, 27, 48, 56, 91]
    def average(x):
        s = sum(x) # Sum of list numbers
        n = len(x) # Length of list
        
        result= s/n # you ccould totally use result= sum(ls)/len(ls), but since theyre in different steps, I assume they want it seperately
        return result
        
    print('Average of', ls, 'is:')
    print(average(ls))
main()