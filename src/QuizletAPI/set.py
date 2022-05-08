import requests
from pprint import pprint
class Set():
    def __init__(self, cookies):
        self.qtkn = cookies['qtkn']
        self.app_session_id = cookies['app_session_id']
        self.qlts = cookies['qlts']
    def create(self, title):
        pass
    def edit(self, id : int, term  = None, definition = None):
        pass