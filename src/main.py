from QuizletAPI import Quizlet
from pprint import pprint
import logging
import time
logging.basicConfig(level=logging.INFO)
client = Quizlet('larryrennoldson', 'Larry1102')
pprint(client.set.edit('test'))
