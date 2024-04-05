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

# Check the number of arguments provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 [llama2|mistral|openhermes]"
    exit 1
fi

# Check the argument provided and run the corresponding model script
case "$1" in
    llama2)
        run_model_script "llama2" "crewai-llama2" "./Llama2Modelfile"
        ;;
    mistral)
        run_model_script "mistral" "crewai-mistral" "./MistralModelfile"
        ;;
    openhermes)
        run_model_script "openhermes" "crewai-openhermes" "./OpenhermesModelfile"
        ;;
    *)
        echo "Invalid model name. Please choose from: llama2, mistral, openhermes"
        exit 1
        ;;
esac