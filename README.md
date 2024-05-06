Bin Effendi, Alif Muhammad 22106588

Kaung, Pwint 22207519

Title: ErasmusConnect+

MyGit Link : https://mygit.th-deg.de/ab15588/assistance-system

Wiki Repository MyGit Link : https://mygit.th-deg.de/ab15588/assistance-system/-/wikis/home

# Project Description
This project aims to enhance the Erasmus mobility program at TH Deggendorf by focusing on the optimization of the services provided by the International Office through **ErasmusConnect+**. 

This Project is about a bot that can help the student in THD to have an opportunity to study abroad for 1-2 semesters or asking about this program in general like what is the program about, what is the requirements to apply and also which countries are available in the program. To have more detailed about the overview of the project, please visit the [Wiki](https://mygit.th-deg.de/ab15588/assistance-system/-/wikis/home) for the project documentation.

Erasmus is a scholarship program for students which supports, promotes and funds student mobility around Europe.

## Prerequisites
We are using Windows and PyCharm

- rasa                         3.6.13
- Flask                        3.0.0
- python                       3.9

## Installation
- git clone https://mygit.th-deg.de/ab15588/assistance-system.git
- install the packages (from prerequisites)
	- pip install rasa Flask

transfer this folder into the directory path       
to test need to run from these 2 terminal first 
- Terminal 1:
	- rasa run actions
- Terminal 2:
	- cd actions
	- set FLASK_APP=app.py
	- set FLASK_ENV=development
	- flask run

Lastly, to use the chatbot use the third terminal
- Terminal 3:
	- rasa shell


## Basic Usage
To start the conversation with the chatbot:    
Start with "Hello" or Greetings with chatbot in Terminal 3  

One of the example conversation, can be check from the sample dialogs in the Wiki documentation.  


## Implementation of the Requests

Requests are

Check for right fit   
1 system persona and 3 user persona   
At least 5 use cases    
Find the technical prerequisites   
For every persona at least 2 example dialogs    
A dialog flow   
Implementation in rasa (yaml and Python files)   

## Work done
Who has implemented what part of the requests:

By **Alif Muhammad bin Effendi**
- 1 system persona and 3 user persona: By Alif Muhammad bin Effendi
- Find the technical prerequisites: By both of us
- For every persona at least 2 example dialogs: By Alif Muhammad bin Effendi
- Implementation in rasa (yaml and Python files)
	- domain
	- nlu
	- app.py
	- actions.py

By **Pwint Kaung**
- Check for right fit: By Pwint Kaung
- At least 5 use cases: By Pwint Kaung
- Find the technical prerequisites: By both of us
- A dialog flow: By Pwint Kaung
- Implementation in rasa (yaml and Python files)
	- stories
	- domain
	- nlu
