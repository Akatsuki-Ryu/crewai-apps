#!/bin/bash

# Function to run the script for the specified model
run_model_script() {
    model_name=$1
    custom_model_name=$2
    model_file=$3

    # Get the base model
    ollama pull $model_name

    # Create the model file
    ollama create $custom_model_name -f $model_file
}

# List of available models
models=("llama2" "mistral" "openhermes" "llama3" "wizardlm2" "openhermes2.5-mistral")

# Display available models for the user to choose
echo "Available models:"
for ((i=0; i<${#models[@]}; i++)); do
    echo "$((i+1)). ${models[i]}"
done

# Prompt the user to choose a model
read -p "Enter the number corresponding to the model you want to run: " choice

# Check if the user input is a valid choice
if ! [[ "$choice" =~ ^[0-9]+$ ]]; then
    echo "Invalid input. Please enter a number."
    exit 1
fi

# Check if the choice is within the range of available models
if (( choice < 1 || choice > ${#models[@]} )); then
    echo "Invalid choice. Please select a number within the range."
    exit 1
fi

# Get the selected model name based on the user's choice
selected_model=${models[choice-1]}

# Function to check the existence of a model file and run the model script
check_and_run() {
    model_name=$1
    file_name=$2
    if [ -f "./$file_name" ]; then
        run_model_script "$model_name" "crewai-$model_name" "./$file_name"
    else
        cd setup
        if [ -f "./$file_name" ]; then
            run_model_script "$model_name" "crewai-$model_name" "./$file_name"
        else
            echo "$file_name not found."
            exit 1
        fi
    fi
}

case "$selected_model" in
    llama2)
        check_and_run "llama2" "Llama2Modelfile"
        ;;
    mistral)
        check_and_run "mistral" "MistralModelfile"
        ;;
    openhermes)
        check_and_run "openhermes" "OpenhermesModelfile"
        ;;
    llama3)
        check_and_run "llama3" "Llama3Modelfile"
        ;;
    wizardlm2)
        check_and_run "wizardlm2" "WizardLM2Modelfile"
        ;;
    openhermes2.5-mistral)
        check_and_run "openhermes2.5-mistral" "Openhermes2.5-mistralModelfile"
        ;;
esac