import qrcode
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox
import os
from pathlib import Path

# Function to generate QR code with optional logo
def generate_qr_with_logo(data, filename='qr_code.png', fill_color='black', back_color='white', logo_path=None):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color).convert('RGB')

    if logo_path:
        try:
            logo = Image.open(logo_path)
            logo_size = 60
            logo = logo.resize((logo_size, logo_size))
            img_w, img_h = img.size
            pos = ((img_w - logo_size) // 2, (img_h - logo_size) // 2)
            img.paste(logo, pos, mask=logo if logo.mode == 'RGBA' else None)
        except Exception as e:
            messagebox.showerror("Logo Error", f"Could not add logo: {e}")

    img.save(filename)
    messagebox.showinfo("Success", f"QR code saved as {filename}")

# Function to browse for a logo image file
def browse_logo():
    start_dir = str(Path.home() / "Pictures")
    if not os.path.exists(start_dir):
        start_dir = str(Path.home())

    path = filedialog.askopenfilename(
        initialdir=start_dir,
        title="Select Logo Image",
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")]
    )
    if path:
        logo_path_var.set(path)
        logo_status.config(text=f"Selected: {os.path.basename(path)}")
    else:
        logo_status.config(text="No logo selected")

# Function triggered by "Generate QR Code" button
def generate_qr():
    data = data_entry.get()
    fill = fill_color_entry.get() or "black"
    back = bg_color_entry.get() or "white"
    logo = logo_path_var.get() or None

    if not data.strip():
        messagebox.showerror("Input Error", "Please enter text or a URL.")
        return

    generate_qr_with_logo(data, fill_color=fill, back_color=back, logo_path=logo)

# ---------------- GUI Setup ------------------
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x360")
root.resizable(False, False)

tk.Label(root, text="Enter text or URL:").pack(pady=5)
data_entry = tk.Entry(root, width=50)
data_entry.pack()

tk.Label(root, text="QR Color:").pack(pady=5)
fill_color_entry = tk.Entry(root, width=20)
fill_color_entry.insert(0, "black")
fill_color_entry.pack()

tk.Label(root, text="Background Color:").pack(pady=5)
bg_color_entry = tk.Entry(root, width=20)
bg_color_entry.insert(0, "white")
bg_color_entry.pack()

logo_path_var = tk.StringVar()
tk.Label(root, text="Logo (optional):").pack(pady=5)
tk.Entry(root, textvariable=logo_path_var, width=40).pack()
tk.Button(root, text="Browse", command=browse_logo).pack(pady=2)
logo_status = tk.Label(root, text="No logo selected", fg="gray")
logo_status.pack()

tk.Button(root, text="Generate QR Code", command=generate_qr, bg="green", fg="white").pack(pady=20)

root.mainloop()
