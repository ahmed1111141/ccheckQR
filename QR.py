import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
import qrcode
from PIL import Image, ImageTk

def generate_qr():
    text = entry.get()
    if not text.strip():
        qr_label.config(image="", text="Enter text or URL", font=("Arial", 12), fg="gray")
        return
    
    fg_color = foreground_color.get()
    bg_color = background_color.get()
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fg_color, back_color=bg_color)
    
    img.save("qrcode.png")
    qr_img = ImageTk.PhotoImage(Image.open("qrcode.png"))
    qr_label.config(image=qr_img, text="")
    qr_label.image = qr_img

def save_qr():
    try:
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
        if file_path:
            img = Image.open("qrcode.png")
            img.save(file_path)
            messagebox.showinfo("Success", "QR Code saved successfully!")
    except FileNotFoundError:
        messagebox.showerror("Error", "QR Code not saved!")

def choose_foreground_color():
    color_code = colorchooser.askcolor(title="Select Foreground Color")[1]
    if color_code:
        foreground_color.set(color_code)
        generate_qr()

def choose_background_color():
    color_code = colorchooser.askcolor(title="Select Background Color")[1]
    if color_code:
        background_color.set(color_code)
        generate_qr()

def clear_all():
    entry.delete(0, tk.END)
    qr_label.config(image="", text="QR Code Preview", font=("Arial", 12), fg="gray")

root = tk.Tk()
root.title("QR Code Generator")
root.geometry("450x600")
root.configure(bg="#f0f0f0")

title_label = tk.Label(root, text="QR Code Generator", font=("Arial", 20, "bold"), bg="#f0f0f0", fg="#333")
title_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), width=30, bd=2, relief="solid")
entry.pack(pady=10)
entry.bind("<KeyRelease>", lambda event: generate_qr())

color_frame = tk.Frame(root, bg="#f0f0f0")
color_frame.pack(pady=10)

foreground_color = tk.StringVar(value="black")
background_color = tk.StringVar(value="white")

fg_button = tk.Button(color_frame, text="Foreground Color", font=("Arial", 10), bg="#4CAF50", fg="white", command=choose_foreground_color)
fg_button.grid(row=0, column=0, padx=5)

bg_button = tk.Button(color_frame, text="Background Color", font=("Arial", 10), bg="#008CBA", fg="white", command=choose_background_color)
bg_button.grid(row=0, column=1, padx=5)

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

generate_button = tk.Button(button_frame, text="Generate QR", font=("Arial", 12), bg="#4CAF50", fg="white", command=generate_qr)
generate_button.grid(row=0, column=0, padx=5)

save_button = tk.Button(button_frame, text="Save", font=("Arial", 12), bg="#008CBA", fg="white", command=save_qr)
save_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(button_frame, text="Clear", font=("Arial", 12), bg="#f44336", fg="white", command=clear_all)
clear_button.grid(row=0, column=2, padx=5)

qr_label = tk.Label(root, text="QR Code Preview", font=("Arial", 12), fg="gray", bg="#f0f0f0")
qr_label.pack(pady=20)

root.mainloop()
