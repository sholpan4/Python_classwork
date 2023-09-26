from PyQt6.QtCore import QObject, pyqtSignal
from logger import log

# state, signal, transition

# тут будет контроллер
class Controller(QObject):
    _transitions =(
        {'from': "INIT",        'to': "LOGIN",          'by': "DB_READY"}, #BY=SIGNAL
        {'from': "LOGIN",       'to': "AUTH",           'by': "GUI_LOGIN"},
        {'from': "AUTH",        'to': "MAIN_WINDOW",    'by': "DB_AUTH_OK"},
        {'from': "AUTH",        'to': "LOGIN",          'by': "DB_AUTH_BAD"},
        {'from': "MAIN_WINDOW", 'to': "ADD_FRIEND",     'by': "UR_HELLO"}, #UDP RECEIVER
        {'from': "ADD_FRIEND",  'to': "MAIN_WINDOW",    'by': "IMMEDIATELY"},
    )





    switchWindow = pyqtSignal(str, str)
    def login(self, username):
        if username:
            self.switchWindow.emit('MainWindow', username)  

    def message_received(self, message_text, message_type):
        log.d(f'mess poluchen: {message_text} tip: {message_type}')

# state machine
#process_signal(signal)
#process_state()
#itteratory  generatory logger read

