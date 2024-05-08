# crewai-apps

a list of apps that runs on crewai ,also for new concepts and researchs

## CrewAI Framework

CrewAI is designed to facilitate the collaboration of role-playing AI agents. In this example, these agents work together to choose between different of cities and put together a full itinerary for the trip based on your preferences.

## Running the Script

run docker compose to start the instance

```bash
docker-compose up
```

access the instance from web browser at `http://localhost:7681`

in the browser, run the script

```bash
./run.sh
```

## modules

### serper search crew

searches the web for the query and returns the results, using serper search api, summarize the result and write to a local file.

### websearch

searches the web for the query and returns the results, using duckduckgo api

### file ops

reads the file and returns the content, also writes the content to the file

### instagarm post crew (scrapt website using browserless, then serper search its competitors)

using browserless to scrap the website and then use serper search to find its competitors, return results and also summarize the contents.
it will also make a midjourney prompts for the instagram post.
verify the post as well as the prompts for quality and relevance control.

### rag search

search and store data in chromedb and summarize the data using rag model
