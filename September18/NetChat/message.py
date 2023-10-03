import json

class Message():
    time = 0
    text = ''
    type = ''
    senderName = ''
    receiverName = ''

    def __init__(self, jsonstring):
        data = json.loads(jsonstring)
        self.time = data.get('time', 0)
        if 'time' in data:
            self.time = data['time']
        if 'senderName' in data:
            self.senderName = data['senderName']
        if 'text' in data:
            self.text = data['text']
        if 'receiverName' in data:
            self.receiverName = data['receiverName']
        if 'type' in data:
            self.type = data['type']

    def toJson(self):
        data = {}
        data['time'] = self.time
        data['text'] = self.text
        data['type'] = self.type
        data['senderName'] = self.senderName
        data['receiverName'] = self.receiverName

        return json.dumps(data)

if '__main__' == __name__:
    msg = Message('{"taxt": "lalala", "time": 50}')
    print(msg.toJson())
         