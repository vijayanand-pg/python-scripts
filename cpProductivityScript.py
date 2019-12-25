# win32clipboard is part of a package called pywin32, install using
# pip install pywin32

import win32clipboard
import subprocess
from datetime import date

filePath = "C:\\"
win32clipboard.OpenClipboard()
clipboardData = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()
# print(clipboardData)

fileName = clipboardData + ".py"

# from Tkinter import Tk
# data = Tk().clipboard_get()
# print(data)

f = open(filePath + fileName, "w+")
f.write("# python file created using cpProductivityScript.py")
f.write("# https://github.com/vijayanand-pg/python-scripts/")
f.write("\n\n\n\n\n# --signature")
currentDate = date.today().strftime("%b-%d-%Y")
f.write("\n# --" + currentDate)
f.close()

p = subprocess.Popen(["code.exe", filePath + fileName])
ret = p.wait()
