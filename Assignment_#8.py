# Iniciating the list variable to be used in the functions
survey = []

def new_survey():
    # using for loop with range of 4 to get all the 4 options, each number in the range will be for one rating.
    # Each if will add the input in a list
    for surv in range(4):
        if surv == 0:
            sqa = int(input("Service Quality: "))
            survey.append(sqa)
        elif surv == 1:
            clean = int(input("Cleanliness: "))
            survey.append(clean)
        elif surv == 2:
            vmoney = int(input("Value for Money: "))
            survey.append(vmoney)
        elif surv == 3:
            sat = int(input("Overall Satisfaction: "))
            survey.append(sat)
    print(survey)
    survey.clear()
    main()
        

# Main module that will show the menu and call other functions.
def main():
    print("Welcome to my survey program\n")
    print("1. Conduct a new survey\n2. View survey summary\n3. Exit\n")
    # checking the entries that the user are providing. If the user provided a integer but diferente from 1, 2 or 3 it will continue to ask for a number between 1 and 3 if it is a string will show up a error and open the menu again. 
    try:
        option = int(input("Please choose one of the above option (1, 2 or 3): "))
        while option < 1 or option > 3:
            option = int(input("Please choose one of the option from menu above, which can be number 1, 2 or 3 : "))
    except ValueError as o:
        print(f"You provided a character or an empty value, which means that you need to provide a number between 1 and 3.\n{o}\n")
        main()
    # This block of code will check which option the user choose. have an option for each number.
    if option == 1:
        try:
            respond = int(input("Please enter the number of respondents: "))
        except ValueError as r:
            print(f"You provided a character or an empty value, which means that you need to provide a number, correspondent to the number of respondets.\n{r}\n")
            main()
        new_survey()
    elif option == 2:
        print("view survey summary")
        main()
    else:
        print("\nThank you for using my survey program")
        exit(0)
main()
