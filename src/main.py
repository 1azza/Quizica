from QuizletAPI import Quizlet
from pprint import pprint
import logging
import time
logging.basicConfig(level=logging.INFO)
client = Quizlet('larryrennoldson', 'Larry1102')



cards = {
    'What is a fsdf?': 'A mouse is a small rodent.',
    'What is a keybofasdfard?': 'A keyboard is a small device that allows you to type.',
    'What is a asdf?': 'A computer is a small device that can be used to do things.',
}
MySet = client.Set(698453480)
pprint(MySet.addCards(cards))
