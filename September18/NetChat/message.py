import json

class Message():
    time = 0
    senderName = ""
    text = ''
    receiverName = ""
    type = ''

    def __init__(self, jsonstring):
        data = json.loads(jsonstring)
        self.time = data['time']
        self.senderName = data['senderName']
        self.text = data['text']
        self.receiverName = data['receiverName']
        self.type = data['type']

    def toJson(self):
               