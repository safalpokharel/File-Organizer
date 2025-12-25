import tkinter as tk
from tkinter import filedialog, messagebox

import os
import shutil

root = tk.Tk()
root.title("File Organizer")
root.geometry("400x250")

source_path = tk.StringVar()
destination_path = tk.StringVar()


def browse_source():
    path = filedialog.askdirectory()
    if path:
        source_path.set(path)


def browse_destination():
    path = filedialog.askdirectory()
    if path:
        destination_path.set(path)

def start_organizing():
    source = source_path.get()
    base_destination = destination_path.get()

    if not source or not base_destination:
        messagebox.showerror("Error", "Please select both source and destination folders.")
        return

    file_types = {
        "Images": ['.jpg', '.jpeg', '.png', '.gif'],
        "Videos": ['.mp4', '.mov', '.avi'],
        "Documents": ['.doc', '.docx', '.txt', '.pdf'],
        "Zips": ['.zip', '.rar'],
    }

    try:
        source_files = os.listdir(source)
    except Exception as e:
        messagebox.showerror("Error", f"Cannot read source folder:\n{e}")
        return

    moved_files_count = 0

    for file in source_files:
        file_name, ext = os.path.splitext(file)
        ext = ext.lower()
        for folder, extensions in file_types.items():
            if ext in extensions:
                final_destination = os.path.join(base_destination, folder)
                os.makedirs(final_destination, exist_ok=True)
                src_path = os.path.join(source, file)
                des_path = os.path.join(final_destination, file)
                try:
                    shutil.move(src_path, des_path)
                    moved_files_count += 1
                except Exception as e:
                    print(f"Failed to move {file}: {e}")
                break

    messagebox.showinfo("Done", f"Moved {moved_files_count} files successfully.")


tk.Label(root, text="Select Source Folder:").pack(pady=5)
tk.Entry(root, textvariable=source_path, width=50).pack()
tk.Button(root, text="Browse", command=browse_source).pack(pady=5)

tk.Label(root, text="Select Destination Folder:").pack(pady=5)
tk.Entry(root, textvariable=destination_path, width=50).pack()
tk.Button(root, text="Browse", command=browse_destination).pack(pady=5)

tk.Button(root, text="Start Organizing", command=start_organizing, bg="green", fg="white").pack(pady=20)

root.mainloop()
