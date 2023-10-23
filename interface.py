import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import pandas as pd
import cv2
import os
import subprocess
# Tạo cửa sổ giao diện
interface = tk.Tk()
interface.title("Security System")


# Lấy kích thước cửa sổ
window_width = 512*2
window_height = 314*2
interface.geometry(f"{window_width}x{window_height}")

# Tải và thay đổi kích thước ảnh nền
background_image = Image.open("resource\\bg.png")  # Thay "background.png" bằng đường dẫn tới hình nền của bạn
background_image = background_image.resize((window_width, window_height), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)

# Đặt ảnh làm nền
background_label = tk.Label(interface, image=background_photo)
background_label.place(relwidth=1, relheight=1)

# # Hàm để mở cửa sổ thông tin
# def show_info_window():
#     interface2.interface2()
#     interface.withdraw()

def open_csv_file():
    # Lấy đường dẫn tới thư mục dự án Python hiện tại
    current_directory = os.path.dirname(os.path.abspath("C:\\Users\\Dell Vostro\\PycharmProjects\\project\\Security-System"))

    # Đường dẫn tới tệp CSV trong cùng thư mục với tệp mã nguồn
    csv_file_path = os.path.join(current_directory, "C:\\Users\\Dell Vostro\\PycharmProjects\\project\\Security-System\\resource\\Attendance.cvs")
    
    # Đọc dữ liệu từ tệp CSV (điều này giả sử rằng tệp CSV chứa dữ liệu cột và hàng)
    if os.path.exists(csv_file_path):
        df = pd.read_csv(csv_file_path)
        
        # Tạo cửa sổ hoặc hộp thoại để hiển thị dữ liệu
        top = tk.Toplevel()
        text = tk.Text(top)
        text.insert("1.0", df.to_string(index=False))
        text.pack()

def run_other_program():
    interface.destroy()
    subprocess.run(['python', 'Attendance.py'])


# Tạo văn bản 
text = tk.Label(interface, text="Attendance", font=("Inter", 18), bg = "#000019", fg = "white", cursor="hand2")
text.place(x = 735, y = 34)
text.bind("<Button-1>", lambda event: open_csv_file()) 

# Tạo văn bản 
text2 = tk.Label(interface, text="START", font=("Inter", 21), bg = "white", fg = "black", cursor="hand2" )
text2.place(x = 172, y = 421)
text2.bind("<Button-1>",lambda event: run_other_program())
# Chạy vòng lặp chính của ứng dụng
interface.mainloop()