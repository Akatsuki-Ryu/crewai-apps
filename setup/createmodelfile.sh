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
models=("llama2" "mistral" "openhermes")

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

# Run the script for the selected model
case "$selected_model" in
    llama2)
      #if there is a model file called Llama2Modelfile , run the script, otherwise go to setup folder and try again
        if [ -f "./Llama2Modelfile" ]; then
            run_model_script "llama2" "crewai-llama2" "./Llama2Modelfile"
        else
          cd setup
          if [ -f "./Llama2Modelfile" ]; then
            run_model_script "llama2" "crewai-llama2" "./Llama2Modelfile"
          else
            echo "Llama2Modelfile not found."
            exit 1
          fi
        fi
        run_model_script "llama2" "crewai-llama2" "./Llama2Modelfile"
        ;;
    mistral)
      if [ -f "./MistralModelfile" ]; then
        run_model_script "mistral" "crewai-mistral" "./MistralModelfile"
      else
        cd setup
        if [ -f "./MistralModelfile" ]; then
          run_model_script "mistral" "crewai-mistral" "./MistralModelfile"
        else
          echo "MistralModelfile not found."
          exit 1
        fi
      fi
        ;;
    openhermes)
      if [ -f "./OpenhermesModelfile" ]; then
        run_model_script "openhermes" "crewai-openhermes" "./OpenhermesModelfile"
      else
        cd setup
        if [ -f "./OpenhermesModelfile" ]; then
          run_model_script "openhermes" "crewai-openhermes" "./OpenhermesModelfile"
        else
          echo "OpenhermesModelfile not found."
          exit 1
        fi
      fi
        ;;
esac