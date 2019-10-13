
import win32clipboard
import subprocess

filePath = "V:\\ViJay\\CompetitiveCoding\\Hackerrank\\PythonBasics\\"
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
f.write("\n\n\n\n\n# --signature")
f.close()

p = subprocess.Popen(["code.exe", filePath + fileName])
ret = p.wait()