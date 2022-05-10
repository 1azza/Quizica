from QuizletAPI import Quizlet
from pprint import pprint
import logging
import time
import seneca

client = Quizlet('larryrennoldson', 'Larry1102')
user = seneca.User('017437@brgsmail.org.uk', 'Larry1102')

FOLDERS = {
    'Biology': 104164961,
}
url = input('Course URL:')
data = seneca.course.getCourseInfo(url, user)
NumberOfModules = 0
Cards = {}
title = data.get('title').replace(' HyperFlashcards', '')
contents = data.get('contents')
Question = 0
for i in contents:
    contentModules = i.get('contentModules')
    for i in contentModules:
        if i.get('moduleType') == "hyper-flashcard":
            content = i.get('content')
            Cards[content.get('question')] = content.get('answer')
                 
MySet = client.Set(client.user.createSet())
MySet.addCards(Cards)
MySet.setTitle(title)
print(MySet.publish())
MySet.saveToFolder(FOLDERS['Biology'])