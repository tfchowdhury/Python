#numanalysis.py
#(A) Write a program that asks user to enter a series of 8 different numbers.
#create an empty list after defining main function

def main():
    numbers = []
#using for loop for the function to iterate 8 times.
    
    for i in range(8):
        num = int(input("Enter a number " + str(i+1) + " of 8: "))
        numbers.append(num)


#Printing the outputs
    print("\nList:", numbers)

    print("\nLow:", min(numbers))
    print("High:", max(numbers))
    print("Total:", sum(numbers))

    average = sum(numbers) / len(numbers)
    print("Average:", average)

#(B) Use tuple() function on the list to covert it to a tuple.

    numbers_tuple = tuple(numbers)
    print("\nTuple:", numbers_tuple)

# Use slicing expression on the tuple with a step value of -1
#to read the contents in reverse order in a 'for' loop and print each item.

    print("\nTuple contents printed in reverse order: ")
    for i in numbers_tuple[::-1]:
        print(i)

main()

