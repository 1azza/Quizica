from QuizletAPI import Quizlet
from pprint import pprint
import logging
import time
import seneca

client = Quizlet('larryrennoldson', 'Larry1102')
user = seneca.User('017437@brgsmail.org.uk', 'Larry1102')




data = seneca.course.getCourseInfo('https://app.senecalearning.com/classroom/course/367190db-2ecc-4feb-8aae-0590155b127f/section/5c512f5e-3573-413d-be79-c5cc1623e93a/session', user)
NumberOfModules = 0
Cards = {}
contents = data.get('contents')
Question = 0
for i in contents:
    contentModules = i.get('contentModules')
    for i in contentModules:
        if i.get('moduleType') == "hyper-flashcard":
            content = i.get('content')
            Cards[content.get('question')] = content.get('answer')
MySet = client.Set(698456137)
MySet.addCards(Cards)
print(MySet.setTitle('Chemistry'))