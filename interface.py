import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import openpyxl
import pandas as pd
from customtkinter import CTkSegmentedButton
import csv
import subprocess
import os

def start_clicked():
    app.destroy()
    subprocess.run(['python', 'Attendance.py'])

def clicked1():   
    folder_path = "C:\\Users\\MSI GF63\\OneDrive - ptit.edu.vn\\CODE\\Security System\\resource\\Unknown"  
    os.system(f'explorer {folder_path}')

def clicked2():
    folder_path = "C:\\Users\\MSI GF63\\OneDrive - ptit.edu.vn\\CODE\\Security System\\resource\\attendance.xlsx"  
    os.system(f'start excel "{folder_path}"')

def clicked3():
    folder_path = "C:\\Users\\MSI GF63\\OneDrive - ptit.edu.vn\\CODE\\Security System\\img"  
    os.system(f'explorer {folder_path}')


# Tạo cửa sổ giao diện
app = tk.Tk()
app.title("Security System App")
app.geometry("1024x628")
app.resizable(False, False)

# Màn hình main
main_frame = tk.Frame(app, width=1024, height=628)
main_frame.pack()

# Mở hình ảnh bằng PIL và chuyển nó thành đối tượng PhotoImage
image = Image.open("resource\\bg.png")  
image = image.resize((1024, 628), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(image)

# Tạo một Label widget để hiển thị hình ảnh:
background_label = tk.Label(main_frame, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Tạo văn bản 
text = tk.Label(main_frame, text="Home", font=("Inter", 18), bg = "#02262c", fg = "white", cursor="hand2")
text.place(x = 512, y = 34)
text.bind("<Button-1>", lambda event: clicked3()) 

# Tạo văn bản 
text = tk.Label(main_frame, text="Unknown", font=("Inter", 18), bg = "#000f12", fg = "white", cursor="hand2")
text.place(x = 630, y = 34)
text.bind("<Button-1>", lambda event: clicked1()) 

# Tạo văn bản 
text = tk.Label(main_frame, text="Attendance", font=("Inter", 18), bg = "#000019", fg = "white", cursor="hand2")
text.place(x = 781, y = 34)
text.bind("<Button-1>", lambda event: clicked2()) 

# Tạo văn bản 
text2 = tk.Label(main_frame, text="START", font=("Inter", 21), bg = "white", fg = "black", cursor="hand2")
text2.place(x = 172, y = 421)
text2.bind("<Button-1>", lambda event: start_clicked()) 

# Chạy vòng lặp chính của ứng dụng
app.mainloop()