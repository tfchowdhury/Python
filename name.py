#name.py

#Declare main function
def main():

#Prompt the user to enter full name
    name = input("Enter your full name: ")
#Split the name into seperate words
    full_name = name.split(" ")
    
#Use for loop to get first character of each name as an initial
    for name in full_name:
        if name == full_name[0]:
            first_initial = name[0]
        elif name == full_name[-1]:
            last_initial = name[0]
        else:
            middle_initial = name[0]

#Convert the first character to upper case if it is already not in upper case
    if first_initial != first_initial.isupper():
        first_initial = first_initial.upper()     
    if middle_initial != middle_initial.isupper():
        middle_initial = middle_initial.upper()
    if last_initial != last_initial.isupper():
        last_initial = last_initial.upper()
    
#Print the desired outcome
    print(last_initial + "." + middle_initial + "." + first_initial)

#Call the main function
main()
