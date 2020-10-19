# RasaCore_RasaNlu_Flask
Chatbot based on Rasa Core, Rasa NLU, and Flask.  

# About
This is a Chatbot build using Rasa NLU and Rasa Core, as they allow for better control over the NLU and NLG tensorflow models, and flexiblity of the overall pipeline.  
The backend of the bot is deployed as a Flask Rest API and communicates with a simple widget, as a frontend, via fetch http requests. Furthermore, Nginx is utilized as Load Balancer.  
The following illustrates the overall architecture of the chatbot:  
![alt text](https://github.com/ahnineamine/RasaCore_RasaNlu_Flask/blob/master/architecture.png?raw=true)  
  
The current satuts of the chatbot as it is, allow for a FAQ or Q&A with the user, which brings me to my next point ->  
As customizing the chatbot requires a knowledge of how RASA works.  
the following features are modifiable/customizable/adjustable:  
## NLU  
* the language and the data processing pipeline (the language in this specific bot is specified as 'french').  
* the nlu training data, nlu.md, which contains the list of questions or variations of question linked to every intent.  
## CORE  
* Fallback policy of the chatbot  
* Policies' parameters:  
  * Memoization Policy (max_history)  
  * Keras Policy (parameters related to the tensorflow model, such as, epochs, batch_size, validation_split, dropout, ..ect)  
* the core training data, stories.md and domain.yml, containing how the dialogue shoule be managed depending on the intents/intent prediction and the list of responses, intents and actions of the chatbot, respectively.  

# How to:  
the chatbot is deployed through a docker compose  
``` docker-compose up --build ```  
It's accessible via port 80. The latter is modifiable through the Nginx service configuration in the the docker compose.  
The Flask API is reachable via the following endpoint  
``` http://0.0.0.0:5005/response/default/conversations ```  
by sending a json file of the following format  
``` {"text": "salut"} ```

