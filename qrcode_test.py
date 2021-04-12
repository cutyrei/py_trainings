import qrcode as qr
import tkinter as tk
import tkinter.filedialog as fd
from PIL import ImageTk

base = tk.Tk()
base.title('QR코드 만들기')
input_area = tk.Frame(base, relief=tk.RAISED, bd=2)
image_area = tk.Frame(base, relief=tk.SUNKEN, bd=2)
encode_text = tk.StringVar()
entry = tk.Entry(input_area, textvariable=encode_text).pack(side=tk.LEFT)
qr_label = tk.Label(image_area)

def generator():
    qr_label.qr_img = qr.make(encode_text.get())
    img_width, img_height = qr_label.qr_img.size
    qr_label.tk_img = ImageTk.PhotoImage(qr_label.qr_img)
    qr_label.config(image=qr_label.tk_img, width=img_width, height=img_height)
    qr_label.pack()

encode_button = tk.Button(input_area, text='코드생성', command=generator).pack(side=tk.LEFT)
input_area.pack(pady=5)
image_area.pack(padx=3, pady=1)

def save():
    filename = fd.asksaveasfilename(title='다른 이름으로 저장', initialfile='qrcode.png')
    if filename and hasattr(qr_label, 'qr_img'):
        qr_label.qr_img.save(filename)

def exit():
    base.destroy()

menubar = tk.Menu(base)
filename = tk.Menu(menubar)
menubar.add_cascade(label='File', menu=filename)
filename.add_command(label='save', command=save)
filename.add_separator()
filename.add_command(label='exit', command=exit)
base.config(menu=menubar)
base.mainloop()

