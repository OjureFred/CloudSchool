import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        #accept connections
        self.accept()
    
    def disconnect(self, close_code):
        pass

    #recieve message from WebSocket
    def recieve(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        #send message to webSocket
        self.send(text_data=json.dumps({'message': message}))
        
