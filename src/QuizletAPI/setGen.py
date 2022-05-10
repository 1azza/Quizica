from pprint import pprint
import json
class setGenerator:
    def __init__(self, setID) -> None:
        self.setID = setID
        self.content = []
       
    def addCard(self, Term, Defenition, number=None):
        if number == None:
            number = len(self.content)
        card ={    'DATA' :
                            {
                                "definition": Defenition,
                                "definitionRichText": {
                                    "content": [
                                        {
                                            "content": [
                                                {
                                                    "text": Defenition,
                                                    "type": "text"
                                                }
                                            ],
                                            "type": "paragraph"
                                        }
                                    ],
                                    "type": "doc"
                                },
                                "rank": number,
                                "setId": self.setID,
                                "word": Term,
                                "wordRichText": {
                                    "content": [
                                        {
                                            "content": [
                                                {
                                                    "text": Term,
                                                    "type": "text"
                                                }
                                            ],
                                            "type": "paragraph"
                                        }
                                    ],
                                    "type": "doc"
                                }
                            }
        }
        self.content.append(card["DATA"])   
         
    def build(self):
        payload = {"data" : self.content, "requestId" : "1652038877870:set:op-seq-0"}
        return json.dumps(payload)
    
    
def test():
    Myset = setGenerator(698453480)
    Myset.addCard("Term 1", "Defenition 1")
    Myset.addCard("Term 2", "Defenition 2")
    Myset.addCard("Term 3", "Defenition 4")
    print(Myset.build())
if __name__ == "__main__":
    test()