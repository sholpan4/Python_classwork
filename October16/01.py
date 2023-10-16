import json

class Message():
    time = 0
    text = ''
    type = ''
    senderName = ''
    senderIp = ''
    receiverName = ''
    receiverIp = ''
    
    @staticmethod
    def fromText(text):
        msg = Message('{"text: "%s"}'  % text)
        return msg


    # def copy(msg: Message):
    #     pass

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
        if 'senderIp' in data:
            self.senderIp = data['senderIp']
        if 'receiverIp' in data:
            self.receiverIp = data['receiverIp']

    def toJson(self):
        data = {}
        data['time'] = self.time
        data['text'] = self.text
        data['type'] = self.type
        data['senderName'] = self.senderName
        data['senderIp'] = self.senderIp
        data['receiverName'] = self.receiverName
        data['receiverIp'] = self.receiverIp

        return json.dumps(data)

if '__main__' == __name__:
    # msg = Message('{"taxt": "lalala", "time": 50}')
    # print(msg.toJson())

    msg2 = Message.fromText("smth")
    print(msg2.toJson())