import socket
import sys
import keyboard
from time import sleep
import time
from Controller import PS4Controller
from GUI import App
import tkinter as tk
import threading
import os


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()

    #while True:
        # Wait for a connection
        #t1 = threading.Thread(target=connectClient, args=())
        #t1.start()
