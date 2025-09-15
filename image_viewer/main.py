import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")]
    )
    if file_path:
        img = Image.open(file_path)
        img_tk = ImageTk.PhotoImage(img)
        label.config(image=img_tk)
        label.image = img_tk
        # Placeholder for watermark detection
        print("Image opened! Watermark check goes here.")

def close_image():
    label.config(image=None)
    label.image = None

# Create main window
root = tk.Tk()
root.title("ViewLock Viewer")
root.configure(bg='darkgray')
root.geometry('800x600')

# Open Image button
btn_open = tk.Button(root, text="Open Image", command=open_image)
btn_open.pack(expand=True)

# Close Image button (X)
btn_close = tk.Button(root, text="X", command=close_image)
btn_close.place(x=770, y=10)  # adjust as needed

# Label to display image
label = tk.Label(root, bg='darkgray')
label.pack()

root.mainloop()
