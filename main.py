from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
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

        '''configures layout + widgets'''

        self.timer = Label(self.window,
                              text = "Focus",
                              font = ("Arial", 32, "bold"),
                              background = "white",
                              foreground = "#333333"
                              )
        self.timer.pack(pady=20)

        Label(self.window,
                 text="Enter what you wanna block out:",
                 font = ("Arial"),
                 background = "#fff3ed"
                 ).pack()
        
        self.url_txt = ScrolledText(
            self.window,
            height = 3,
            width = 30,
            font = ("Consolas", 14),
            background = "white",
            relief = FLAT,
            highlightthickness = 2
        
        ) 

        self.url_txt.pack(pady= 5, padx = 5)

        duration = Frame(self.window, background = "white")
        duration.pack(pady=5)

        Label(  duration,
                text="Duration(Hours):",
                background = "white",
                font = ("Arial", 15)
                
            ).pack(side=LEFT, padx=5)
        
        self.enter_hours = Spinbox(
            duration,
            from_=0.1, to=24.0, increment=0.1,
            width=5,
            font=("Arial", 11),
            justify='center'
        )
        self.enter_hours.delete(0, END)
        self.enter_hours.insert(0, "1.0")

        self.enter_hours.pack(side=LEFT)

        self.action_btn = Button(self.window,
                                 text = "Start Focus session",
                                 font=("Arial", 14, "bold"),
                                 background="white",
                                 foreground="black",
                                 command = self.toggle_action,
                                 height =2,
                                 relief = FLAT,
                                 cursor="hand1"
                                )
        self.action_btn.pck(fill=X, padx=40,pady = 30)

        Label(self.window,
              text="You must run as admin",
              font=("Arial", 9),
              bg="white",
              fg="black"
        ).pack(side=BOTTOM, pady=10)

        def toggle_action(self):
            if not self.is_blocking:
                self.start_blocking()
            else:
                self.stop_blocking()
        
        def start_blocking(self):
            try:
                hrs= float(self.enter_hours.get())
                if hrs <= 0:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Invalid Input", "please enter valid hours")
                return
            
            urls = [line.strip() for line in self.url_txt.get("1.0", END).splitlines()
                    if line.strip()]
            
            if not urls:
                messagebox.showwarning("Missing URLs", "Type in at least one website")
                return
            
            if not messagebox.askyesno('Confirm', f"Block {len(urls)} sites for {hours} hours?"):
                return
            
            self.stop_event.clear()
            self.block_thread = threading.Thread(
                target=logic.block,
                args=(hrs,urls, self.stop_event ),
                daemon= True
            )
            self.block_thread.start()

            self.is_blocking = True
            self.timer_label.config(text=f"Blocking for {hrs}h...", fg="light pink")
            self.action_btn.config(text="Emergency Unblock", bg="white")
            self.url_txt.config(state=DISABLED)
            self.enter_hours.config(state=DISABLED)


        
        
        
                 

if __name__ == "__main__":
    window = Tk()
    app = App(window)
    window.mainloop() 

