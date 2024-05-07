import os

os.environ["NEWSAPI_KEY"] = 'e916ad44033a4aa0b37b10d2c144529f'
os.environ["SERPER_API_KEY"] = 'c7a06bdaa06e509b2116cb12ddb60fb773c9693f'
os.environ["OPENAI_API_KEY"] = 'sk-111111111111111111111111111111111111111111111111'
os.environ["OPENAI_API_BASE"] = 'http://llm:11434/v1'
os.environ["OPENAI_MODEL_NAME"] = 'openhermes'



import subprocess
import json

base_url = "http://llm:11434/v1"


# check if this script is running in docker or not
def is_running_in_docker():
    return os.path.exists('/.dockerenv')

def list_models():
    global base_url
    command = f"curl {base_url}/api/tags"
    print(f"Running command: {command}")
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()

    if error:
        print(f"Error: {error}")
        return []

    # Parse the output as JSON
    data = json.loads(output.decode('utf-8'))

    # Extract the model names
    model_names = [model['name'] for model in data['models']]
    return model_names


def display_model_list():
    model_list = list_models()
    print("Available models:")
    for i, model in enumerate(model_list):
        print(f"{i + 1}. {model}")
    print("=====================================")


def choose_model():
    model_list = list_models()
    print("\nChoose the model you would like to run:")
    for i, model in enumerate(model_list):
        print(f"{i + 1}. {model}")
    print("=====================================")
    choice = input("Enter the number of the model you would like to run: ")
    if choice == "":
        # if there is a model called "crewai-openhermes" in the model list, choose that, otherwise choose "openhermes"
        if "crewai-openhermes:latest" in model_list:
            print("No choice made. will choose the default model crewai-openhermes.")
            os.environ["OPENAI_MODEL_NAME"] = 'crewai-openhermes'
            return 0
        else:
            print("No choice made and crewai model is not initiated. will choose the default model openhermes.")
            #ask user if they want to run the "createmodelfile.sh" script
            print("Would you like to run the createmodelfile.sh script to create the crewai-openhermes model?")
            print("1. Yes")
            print("2. No")
            print("=====================================")
            choice = input("Enter the number of the choice you would like to make: ")
            if choice == "1":
                print("Running createmodelfile.sh...")
                os.system('bash ./setup/createmodelfile.sh')
                print("Model created. Please restart the program.")
                exit()
            elif choice == "2":
                print("No choice made. will choose the default model openhermes.")
                os.environ["OPENAI_MODEL_NAME"] = 'openhermes'
                return 0

        print("No choice made. will choose the default model openhermes.")
        os.environ["OPENAI_MODEL_NAME"] = 'openhermes'
        return 0
    if int(choice) in range(1, len(model_list) + 1) and choice != "":
        # only pass through the part before ":"
        selected_model = model_list[int(choice) - 1].split(":")[0]
        os.environ["OPENAI_MODEL_NAME"] = selected_model
        print(f"Running model: {selected_model}")
        return 0
    else:
        print("Invalid choice. will choose the default model openhermes.")
        os.environ["OPENAI_MODEL_NAME"] = 'openhermes'
        return 0


# let user choose which model to run
def choose_model_hardcode():
    print("\nChoose the model you would like to run:")
    print("1. Openhermes (default)")
    print("2. mistral")
    print("=====================================")
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
    print("\nChoose the base URL you would like to run:")
    print("1. docker host llm (default when running in docker)")
    print("2. baremetal localhost (default when running locally)")
    print("3. docker network llm")
    print("4. baremetal lm studio")
    print("=====================================")
    choice = input("Enter the number of the base URL you would like to run: ")
    global base_url
    if choice == "1":
        base_url = "http://host.docker.internal:11434"
        os.environ["OPENAI_API_BASE"] = 'http://host.docker.internal:11434/v1'
    elif choice == "2":
        base_url = "http://localhost:11434"
        os.environ["OPENAI_API_BASE"] = 'http://localhost:11434/v1'
    elif choice == "3":
        base_url = "http://llm:11434"
        os.environ["OPENAI_API_BASE"] = 'http://llm:11434/v1'
    elif choice == "4":
        base_url = "http://localhost:1234"
        os.environ["OPENAI_API_BASE"] = 'http://localhost:1234/v1'
    else:
        print("Invalid choice. will choose the default according to the environment.")
        if is_running_in_docker():
            base_url = "http://host.docker.internal:11434"
            os.environ["OPENAI_API_BASE"] = 'http://host.docker.internal:11434/v1'
            print("Running in docker. base url" + base_url)
        else:
            base_url = "http://localhost:11434"
            os.environ["OPENAI_API_BASE"] = 'http://localhost:11434/v1'
            print("Running locally. base url" + base_url)
    if choice == "1" or choice == "2" or choice == "3":
         choose_model()


# create a menu for user to choose which file to run
def main():
    print("\nWelcome to the AI Crew!")
    print("1. Trip Planner")
    print("2. Serper search")
    print("3. Research Assistant")
    print("4. File Operations")
    print("5. Instagram Poster")
    print("6. RAG search")
    print("e. Exit")
    print("=====================================")
    choice = input("Enter the number of the file you would like to run: ")
    if choice == "1":
        print("Running Trip Planner...(this is not working)")
        os.system('python3 trip_planner.py')
    elif choice == "2":
        print("Running serper search crew...")
        os.system('python3 ./websearchtoolbox/serpersearchtoolbox.py')
    elif choice == "3":
        print("Running Research Assistant...")
        os.system('python3 ./websearch/websearch.py')
    elif choice == "4":
        print("Running File Operations...")
        os.system('python3 ./fileopts/fileopts.py')
    elif choice == "5":
        print("Running Instagram Poster...")
        os.system('python3 ./instagramposter/instagrampostermain.py')
    elif choice == "6":
        print("Running RAG search...")
        os.system('python3 ./webragsearch/ragsearch.py')
    elif choice == "e":
        print("Exiting...")
        exit()
    else:
        print("Invalid choice. Please try again.")
        main()


if __name__ == "__main__":
    # print(is_running_in_docker())
    choose_base_url()
    # list_models()
    # display_model_list()
    # choose_model()

    main()
