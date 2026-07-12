from tkinter import *
import threading
import logic

class App:
    def __init__(self, window):
        self.window = window
        self.window.title("Website Blocker")
        self.window.geometry("720x400")
        self.window.config(background = "#ffd6e5")
        self.is_blocking = False
        self.stop_event = threading.Event()
        self.block_thread = None

        self._setup_ui()

    def _setup_ui(self):
        
        
                               
        











window.mainloop() 

