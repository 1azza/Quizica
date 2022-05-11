from QuizletAPI import Quizlet
from pprint import pprint
import logging
import time
import seneca
import webbrowser
client = Quizlet('larryrennoldson', 'Larry1102')
user = seneca.User('017437@brgsmail.org.uk', 'Larry1102')
MySet = client.Set(client.user.createSet())

FOLDERS = {
    'Biology': 104164961,
}
url = input('Course URL:')
print('Downloading course...')
data = seneca.course.getCourseInfo(url, user)
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
MySet.addCards(Cards)
print('Publishing set...')
MySet.setTitle(title)
link = MySet.publish()
MySet.saveToFolder(FOLDERS['Biology'])
print(link)
x = input('Press 1 to open in browser...')
if x == '1':   
 webbrowser.open_new(link)   
input('Press ENTER to exit...')