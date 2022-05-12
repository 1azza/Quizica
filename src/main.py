from QuizletAPI import Quizlet
from pprint import pprint
import logging
import time
import seneca
import webbrowser
import os
from dotenv import load_dotenv
#Get password from enviroment variables
load_dotenv()
PASSWORD = os.getenv('PASSWORD')


#Login to Quizlet and Seneca
client = Quizlet('larryrennoldson', PASSWORD)
user = seneca.User('017437@brgsmail.org.uk', PASSWORD)

#Recieve course
url = input('Course URL:')

#Download seneca course
print('Downloading course...')
data = seneca.course.getCourseInfo(url, user)

#Initialise set
print('Initialising set...')
id = client.user.createSet()
MySet = client.Set(id)
print(f'Set ID: {id}\n')

FOLDERS = {
    'Biology': 104164961,
}

#Parse course data
print('Generating flashcards...')
NumberOfModules = 0
Cards = {}
title = data.get('title').replace(' HyperFlashcards', '')
contents = data.get('contents')
Question = 0
print('Generating flashcards...')
for i in contents:
    contentModules = i.get('contentModules')
    for i in contentModules:
        if i.get('moduleType') == "hyper-flashcard":
            content = i.get('content')
            Cards[content.get('question')] = content.get('answer')
            
#cards to set
MySet.addCards(Cards)
MySet.setTitle(title)

#Publsih set
print('Publishing set...')
link = MySet.publish()

#Save to folder
MySet.saveToFolder(FOLDERS['Biology'])
print(link)
x = input('Press 1 to open in browser...')
if x == '1':   
 webbrowser.open_new(link)   
input('Press ENTER to exit...')