# Iniciating the list variable to be used in the functions
survey = []

# this function will validate all the inputs that the user will provide. will check if the data is a integer and if it is between 1 and 5
def valid_rate(a):
    try:
        rate = int(input(a))
        while rate < 1 or rate > 5:
            print("")
            print("ATENCION:\nplease provide a rate between 1 and 5.")
            rate = int(input(a))
    except ValueError as s:
        print("")
        print(f"ATENCION USER:\nYou provided a character or an empty value, which means that you need to provide a number between 1 and 5.\nPYTHON ERROR:\n{s}\n")
        rate = int(input(a))
        while rate < 1 or rate > 5:
            print("")
            print("please provide a rate between 1 and 5.")
            rate = int(input(a))
    survey.append(rate)
    # using the count variable to use in the file processing, to access the list index and write the data in the file.
    # the lens value will be added in each interation starting with 'one' that why i`m removeing 1, to start in 0
    count = len(survey) - 1
    survey_data = open('survey_data.txt', 'a')
    survey_data.write(str(survey[count]))
    # this conditional statement will check the index of the list and if it is the last index which is '3'  wont write the comma and also will jump one line, meaning that the next time that this function is called the new data will be in an another line.
    if count != 3:
        survey_data.write(',')
    else:
        # when reach the last item in the list it will jump one line and clear the list to start again the count in 0.
        survey_data.write('\n')
        survey.clear()
        survey_data.close()

def new_survey(a):
    # using for loop with range of 4 to get all the 4 options, each number in the range will be for one rating.
    # Each if will add the input in a list
    for i in range(a):
        print("For each aspects please provide a rating from 1 to 5.")
        for surv in range(4):
            if surv == 0:
                # this is the name for the aspect that the user are rating
                aspect = "Service Quality: "
                # calling function valid_rate to validate if the entries are integer or not.
                valid_rate(aspect)
            elif surv == 1:
                aspect = "Cleanliness: "
                valid_rate(aspect)
            elif surv == 2:
                aspect = "Value for Money: "
                valid_rate(aspect)
            elif surv == 3:
                aspect = "Overall Satisfaction: "
                valid_rate(aspect)
    print("\nThank you for answering our survey.")
    print("You rate was saved successfully.\n")
    print("")
    survey.clear()
    main()

def survey_summary():
    survey_data = open('survey_data.txt', 'r')
    survey_list = list(survey_data.readline())
    survey_list = survey_list.rstrip('\n')
    print(survey_list)

# Main module that will show the menu and call other functions.
def main():
    print("Welcome to my survey program\n")
    print("1. Conduct a new survey\n2. View survey summary\n3. Exit\n")
    # checking the entries that the user are providing. If the user provided a integer but diferente from 1, 2 or 3 it will continue to ask for a number between 1 and 3 if it is a string will show up a error and open the menu again. 
    try:
        option = int(input("Please choose one of the above option (1, 2 or 3): "))
        while option < 1 or option > 3:
            option = int(input("ATENCION:\nPlease choose one of the option from menu above, which can be number 1, 2 or 3 : "))
    except ValueError as o:
        print(f"\nATENCION USER:\nYou provided a character or an empty value, which means that you need to provide a number between 1 and 3.\nPYTHON ERROR:\n{o}\n")
        main()
    # This block of code will check which option the user choose. have an option for each number.
    if option == 1:
        try:
            respond = int(input("Please enter the number of respondents: "))
        except ValueError as r:
            print(f"\nATENCION USER:\nYou provided a character or an empty value, which means that you need to provide a number, correspondent to the number of respondents.\nPYTHON ERROR:\n{r}\n")
            main()
        new_survey(respond)
    elif option == 2:
        print("Survey Summary: ")
        survey_summary()

        main()
    else:
        print("\nThank you for using my survey program")
        exit(0)
main()
