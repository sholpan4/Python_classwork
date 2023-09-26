from PyQt6.QtCore import QObject, pyqtSignal
from logger import log

# state, signal, transition

# тут будет контроллер
class Controller(QObject):
    _state = "INIT"
    _transitions =(
        {'from': "INIT",        'to': "LOGIN",          'by': "DB_READY"}, #BY=SIGNAL
        {'from': "LOGIN",       'to': "AUTH",           'by': "GUI_LOGIN"},
        {'from': "AUTH",        'to': "MAIN_WINDOW",    'by': "DB_AUTH_OK"},
        {'from': "AUTH",        'to': "LOGIN",          'by': "DB_AUTH_BAD"},

        {'from': "MAIN_WINDOW", 'to': "ADD_FRIEND",     'by': "UR_HELLO"}, #UDP RECEIVER
        {'from': "ADD_FRIEND",  'to': "MAIN_WINDOW",    'by': "IMMEDIATELY"},

        {'from': "MAIN_WINDOW",   'to': "CHECK_MESSAGE",  'by': "UR_MESSAGE"},
        {'from': "CHECK_MESSAGE", 'to': "MAIN_WINDOW",    'by': "IMMEDIATELY"},

        {'from': "MAIN_WINDOW", 'to': "SEND_MSG",     'by': "GUI_SEND"},
        {'from': "GUI_SEND",    'to': "MAIN_WINDOW",  'by': "IMMEDIATELY"},

        {'from': "MAIN_WINDOW", 'to': "CHANGING_CHAT",     'by': "GUI_CHAT_CHANGE"},
        {'from': "CHANGING_CHAT",    'to': "MAIN_WINDOW",  'by': "IMMEDIATELY"},

    )

    def process_state(self):
        match self._state:
            case "INIT":
                pass
            case "LOGIN":
                pass
            case "AUTH":
                pass
            case "MAIN_WINDOW":
                pass #switch window
            case _:
                log.w("Unknown state!")
            

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

