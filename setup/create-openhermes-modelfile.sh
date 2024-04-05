#!/bin/bash

# Variables
model_name="openhermes"
custom_model_name="crewai-openhermes"

# Get the base model
ollama pull $model_name

# Create the model file
ollama create $custom_model_name -f ./OpenhermesModelfile