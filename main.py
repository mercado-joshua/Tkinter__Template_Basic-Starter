#===========================
# Imports
#===========================
import tkinter as tk
from tkinter import ttk, colorchooser as cc, Menu, Spinbox as sb, scrolledtext as st, messagebox as mb, filedialog as fd, simpledialog as sd

#===========================
# Main App
#===========================
class App(tk.Tk):
    """Main Application."""
    #------------------------------------------
    # Initializer
    #------------------------------------------
    def __init__(self):
        super().__init__()
        self.init_config()
        self.init_vars()
        self.init_widgets()
        self.init_events()

    #------------------------------------------
    # Instance Variables
    #------------------------------------------
    def init_vars(self):
        pass

    #-------------------------------------------
    # Window Settings
    #-------------------------------------------
    def init_config(self):
        self.resizable(True, True)
        self.title('template')
        self.iconbitmap('python.ico')
        self.style = ttk.Style(self)
        self.style.theme_use('clam')

    #-------------------------------------------
    # Window Events / Keyboard Shorcuts
    #-------------------------------------------
    def init_events(self):
        pass

    #-------------------------------------------
    # Widgets / Components
    #-------------------------------------------
    def init_widgets(self):
        pass

    # INSTANCE ---------------------------------
    def ins_func(self):
        pass

    # EVENTS -----------------------------------
    def evt_func(self):
        pass

    # PARAMETERS -------------------------------
    def arg_func(self):
        pass

#===========================
# Start GUI
#===========================
def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()