import tkinter as tk

root = tk.Tk()
root.title('Image Viewer')
root.configure(bg='#1e1e1e')

# --- Top frame ---
top_frame = tk.Frame(root, bg='#252526', height=50)
top_frame.pack(fill='x', side='top')
top_frame.pack_propagate(False)

# Label field
label = tk.Label(
    top_frame,
    text='Image Viewer',
    font=('Fira Sans', 11),
    bg='#252526',
    fg='#d4d4d4')
label.pack(expand=True)

# --- Bottom frame ---
bottom_frame = tk.Frame(root, bg='#252526', height=50)
bottom_frame.pack(fill='x', side='bottom')
bottom_frame.pack_propagate(False)

# Entry field
command_entry = tk.Entry(
    bottom_frame,
    font=('Fira Sans', 9),
    width=30,
    bg='#333333',
    fg='#d4d4d4',
    insertbackground='#aeafad')
command_entry.pack(side='right', padx=(0, 10), pady=10)
command_entry.focus()

# 'Command:'
command_label = tk.Label(
    bottom_frame,
    text='Command:',
    font=('Fira Sans', 9),
    bg='#252526',
    fg='#d4d4d4'
)
command_label.pack(side='right', padx=(0, 5))

root.mainloop()
