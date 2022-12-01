from glob import glob
from typing import get_origin
import tkinter as tk  
from tkinter import filedialog
import os


def upload_files(socket):
    print("[+] Upload file")
    path = filedialog.askopenfilename(initialdir = r"adress",title = "Hello",filetypes = (("all files","*.*"),("png files","*.png")))

    fileName = ""
    for i in range(len(path)-1,-1,-1):
        if path[i] != '/':
            fileName = fileName + str(path[i])
        else:
            fileName = fileName[::-1]
            break

    path = path.removesuffix(fileName)
    print("[+] Selected File: ", fileName)
    socket.SendData(fileName)
    socket.SendFile(fileName, path)
