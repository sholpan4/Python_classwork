# import router  #from router import Router  #import router as r
import sys
# from logger import Logger
from PyQt6.QtWidgets import QApplication
from router import Router
from udp_receiver import *
from udp_sender import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # log = Logger(Logger.DEBUG)

    route = Router()  #route = router.Router()
    route.start()
    
    app.exec()
    