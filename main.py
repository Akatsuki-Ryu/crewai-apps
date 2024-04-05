import os

os.environ["SERPER_API_KEY"] = 'c7a06bdaa06e509b2116cb12ddb60fb773c9693f'
os.environ["OPENAI_API_KEY"] = 'sk-111111111111111111111111111111111111111111111111'

import subprocess
import json

base_url = "http://llm:11434/v1"


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
    print("Choose the model you would like to run:")
    for i, model in enumerate(model_list):
        print(f"{i + 1}. {model}")
    print("=====================================")
    choice = input("Enter the number of the model you would like to run: ")
    if choice == "":
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
    print("Choose the model you would like to run:")
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
    print("Choose the base URL you would like to run:")
    print("1. docker host (default)")
    print("2. baremetal localhost")
    print("3. docker network")
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
    else:
        print("Invalid choice. will choose to run local")
        base_url = "http://host.docker.internal:11434"
        os.environ["OPENAI_API_BASE"] = 'http://host.docker.internal:11434/v1'


# create a menu for user to choose which file to run
def main():
    print("Welcome to the AI Crew!")
    print("1. Trip Planner")
    print("2. Law Consultant")
    print("3. Research Assistant")
    print("4. File Operations")
    print("5. Instagram Poster")
    print("e. Exit")
    print("=====================================")
    choice = input("Enter the number of the file you would like to run: ")
    if choice == "1":
        print("Running Trip Planner...(this is not working)")
        os.system('python3 trip_planner.py')
    elif choice == "2":
        print("Running Law Consultant...")
        os.system('python3 ./websearchtoolbox/websearchtoolbox.py')
    elif choice == "3":
        print("Running Research Assistant...")
        os.system('python3 ./websearch/websearch.py')
    elif choice == "4":
        print("Running File Operations...")
        os.system('python3 ./fileopts/fileopts.py')
    elif choice == "5":
        print("Running Instagram Poster...")
        os.system('python3 ./instagramposter/instagrampostermain.py')
    elif choice == "e":
        print("Exiting...")
        exit()
    else:
        print("Invalid choice. Please try again.")
        main()


if __name__ == "__main__":
    choose_base_url()
    # list_models()
    display_model_list()
    choose_model()

    main()
