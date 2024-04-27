# the conda environment name is called "crewai"
# deactivate the current conda environment
# conda init
# conda deactivate
# conda deactivate

#remove the curernt conda environment
# conda remove -y --name crewai --all

# create a new conda environment
# conda create -y -n crewai python=3.11

# activate the conda environment
# conda init
# conda activate crewai

# install poetry
curl -sSL https://install.python-poetry.org | python3 -

# install the required packages
pip install crewai==0.28.8
pip install crewai_tools
pip install 'crewai[tools]'
# pip install duckduckgo-search
pip install -U duckduckgo-search



#for rag search
pip install crewai langchain-community langchain-openai requests duckduckgo-search chromadb



pip install pipx # it is ok to install this globally
pipx install poetry