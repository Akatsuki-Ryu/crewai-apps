import os

os.environ["SERPER_API_KEY"] = 'c7a06bdaa06e509b2116cb12ddb60fb773c9693f'
os.environ["OPENAI_API_KEY"] = 'sk-111111111111111111111111111111111111111111111111'

# let user choose which model to run
def choose_model():
    print("Choose the model you would like to run:")
    print("1. Openhermes (default)")
    print("2. mistral")
    choice = input("Enter the number of the model you would like to run: ")
    if choice == "1":
        # model_name = "openhermes"
        os.environ["OPENAI_MODEL_NAME"] = 'openhermes'
    elif choice == "2":
        # model_name = "mistral"
        os.environ["OPENAI_MODEL_NAME"] = 'mistral'
    else:
        print("Invalid choice. will choose the default model openhermes.")
        os.environ["OPENAI_MODEL_NAME"] = 'openhermes'


# let user choose if running from docker or running from local
def choose_base_url():
    print("Choose the base URL you would like to run:")
    print("1. Docker")
    print("2. Local (default)")
    choice = input("Enter the number of the base URL you would like to run: ")
    if choice == "1":
        # base_url = "http://host.docker.internal:11434"
        os.environ["OPENAI_API_BASE"] = 'http://host.docker.internal:11434'
    elif choice == "2":
        # base_url = "http://localhost:11434"
        os.environ["OPENAI_API_BASE"] = 'http://localhost:11434'
    else:
        print("Invalid choice. will choose to run local")
        os.environ["OPENAI_API_BASE"] = 'http://host.docker.internal:11434'


# create a menu for user to choose which file to run
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
    choose_model()
    choose_base_url()
    main()
