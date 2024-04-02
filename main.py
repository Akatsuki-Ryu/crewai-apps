import os

#create a menu for user to choose which file to run
def main():
    print("Welcome to the AI Crew!")
    print("1. Trip Planner")
    print("2. Law Consultant")
    print("3. Research Assistant")
    print("4. Exit")
    choice = input("Enter the number of the file you would like to run: ")
    if choice == "1":
        print("Running Trip Planner...(this is not working)")
        os.system('python3 trip_planner.py')
    elif choice == "2":
        print("Running Law Consultant...")
        os.system('python3 lawconsult.py')
    elif choice == "3":
        print("Running Research Assistant...")
        os.system('python3 websearch.py')
    elif choice == "4":
        print("Exiting...")
        exit()
    else:
        print("Invalid choice. Please try again.")
        main()

if __name__ == "__main__":
    main()