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
    try:
        survey_data = open('survey_data.txt', 'a')
        survey_data.write(str(survey[count]))
    except FileNotFoundError:
        print("ERROR\nFile survey_data.txt does not exist.\n")
        main()
    except PermissionError:
        print("ERROR\nFile survey_data.txt does not permission to be accessed")
        main()

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

# this function will calculate and show all the information about the summary.
def survey_summary():
    #iniciating varables to be used and store the respectives values for each aspects
    service_quality_total = 0
    service_cleanliness_total = 0
    service_value_for_money_total = 0
    service_overall_satisfaction_total = 0
    rating = 0
    rating2 = 0
    rating3 = 0
    rating4 = 0
    rating5 = 0
    total_quality = 0

    rating1 = 0
    rating22 = 0
    rating33 = 0
    rating44 = 0
    rating55 = 0

    rating11 = 0
    rating222 = 0
    rating333 = 0
    rating444 = 0
    rating555 = 0

    rating1111 = 0
    rating2222 = 0
    rating3333 = 0
    rating4444 = 0
    rating5555 = 0
    # This variable will check number of respondents
    count_survey = 0
    # opening the file to be able to use it, in read option
    try:
        survey_data = open('survey_data.txt', 'r')
    except FileNotFoundError:
        print("ERROR\nFile survey_data.txt does not exist.\n")
        main()
    except PermissionError:
        print("ERROR\nFile survey_data.txt does not permission to be accessed")
        main()
    # tranfor the data inside of the file in a list
    survey_list = list(survey_data)
    # this first loop will create a list with each element separated
    for s in range(len(survey_list)):
        survey_list2 = list(survey_list[s])
        cleaned_survey_list = []
        # this second loop will create a new list without ',' and '\n'
        for item in survey_list2:
            # if the item is not ',' or '\n' will add in the new list
            if item not in {',', '\n'}:
                cleaned_survey_list.append(item)
        # this loop will use the index of the list to specify each rate to a specific aspect also will do the sum of the rates
        for item in range(len(cleaned_survey_list)):
            if item == 0:
                service_quality = int(cleaned_survey_list[item])
                service_quality_total = service_quality_total + service_quality
                if service_quality == 1:
                    rating = rating + 1
                elif service_quality == 2:
                    rating2 = rating2 + 1
                elif service_quality == 3:
                    rating3 = rating3 + 1
                elif service_quality == 4:
                    rating4 = rating4 + 1
                elif service_quality == 5:
                    rating5 = rating5 + 1
            elif item == 1:
                service_cleanliness = int(cleaned_survey_list[item])
                service_cleanliness_total = service_cleanliness_total + service_cleanliness
                if service_cleanliness == 1:
                    rating1 = rating1 + 1
                elif service_cleanliness == 2:
                    rating22 = rating22 + 1
                elif service_cleanliness == 3:
                    rating33 = rating33 + 1
                elif service_cleanliness == 4:
                    rating44 = rating44 + 1
                elif service_cleanliness == 5:
                    rating55 = rating55 + 1
            elif item == 2:
                service_value_for_money = int(cleaned_survey_list[item])
                service_value_for_money_total = service_value_for_money_total + service_value_for_money
                if service_value_for_money == 1:
                    rating11 = rating11 + 1
                elif service_value_for_money == 2:
                    rating222 = rating222 + 1
                elif service_value_for_money == 3:
                    rating333 = rating333 + 1
                elif service_value_for_money == 4:
                    rating444 = rating444 + 1
                elif service_value_for_money == 5:
                    rating555 = rating555 + 1
            elif item == 3:
                service_overall_satisfaction = int(cleaned_survey_list[item])
                service_overall_satisfaction_total = service_overall_satisfaction_total + service_overall_satisfaction
                if service_overall_satisfaction == 1:
                    rating1111 = rating1111 + 1
                elif service_overall_satisfaction == 2:
                    rating2222 = rating2222 + 1
                elif service_overall_satisfaction == 3:
                    rating3333 = rating3333 + 1
                elif service_overall_satisfaction == 4:
                    rating4444 = rating4444 + 1
                elif service_overall_satisfaction == 5:
                    rating5555 = rating5555 + 1
        count_survey += + 1

    # will print the output to the user
    print("Survey Summary: ")
    print("Total number of responses: ", count_survey)
    print("")

    print("Service Quality: ")
    average_quality = service_quality_total / count_survey
    print(" Average rating: {:.1f}".format(average_quality))
    print(" Number of responses for each rating (1 to 5):")
    print("  Rating 1: ", rating)
    print("  Rating 2: ", rating2)
    print("  Rating 3: ", rating3)
    print("  Rating 4: ", rating4)
    print("  Rating 5: ", rating5)
    print("")

    average_cleanliness = service_cleanliness_total / count_survey
    print("Cleanliness: ")
    print(" Average rating: {:.1f}".format(average_cleanliness))
    print(" Number of responses for each rating (1 to 5):")
    print("  Rating 1: ", rating1)
    print("  Rating 2: ", rating22)
    print("  Rating 3: ", rating33)
    print("  Rating 4: ", rating44)
    print("  Rating 5: ", rating55)
    print("")

    average_value_for_money = service_value_for_money_total / count_survey
    print("Value for Money: ")
    print(" Average rating: {:.1f}".format(average_value_for_money))
    print(" Number of responses for each rating (1 to 5):")
    print("  Rating 1: ", rating11)
    print("  Rating 2: ", rating222)
    print("  Rating 3: ", rating333)
    print("  Rating 4: ", rating444)
    print("  Rating 5: ", rating555)
    print("")

    average_overall_satisfaction = service_overall_satisfaction_total / count_survey
    print("Overall Satisfaction: ")
    print(" Average rating: {:.1f}".format(average_overall_satisfaction))
    print(" Number of responses for each rating (1 to 5):")
    print("  Rating 1: ", rating1111)
    print("  Rating 2: ", rating2222)
    print("  Rating 3: ", rating3333)
    print("  Rating 4: ", rating4444)
    print("  Rating 5: ", rating5555)
    print("")

    survey_data.close()
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
        survey_summary()
        main()
    else:
        print("\nThank you for using my survey program")
        exit(0)
main()
