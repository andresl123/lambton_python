def main():
    print("Welcome to my survey program\n")
    print("1. Conduct a new survey\n2. View survey summary\n3. Exit\n")
    try:
        option = int(input("Please choose one of the above option: "))
        while option < 1 or option > 3:
            option = int(input("Please choose one of the option from menu above, which can be number 1, 2 or 3 : "))
    except ValueError as o:
        print(f"You provided a caracter diferent from integer, which means that you need to provide a number between 1 and 3 {o}")
        main()
main()
