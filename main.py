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

        self.timer = tk.Label(self.window,
                              text = "Focus",
                              font = ("Arial", 32, "bold"),
                              background = "white",
                              foreground = "#333333"
                              )
        self.timer.pack(pady=20)

if __name__ == "__main__":
    window = Tk()
    app = App(window)
    window.mainloop() 

