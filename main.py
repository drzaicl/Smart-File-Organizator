import tkinter as tk
import os
import shutil

def organize():
    folder = entry.get()

    file_types = {
        "Images": [".jpg", ".png"],
        "Videos": [".mp4"],
        "Documents": [".txt"]
    }

    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)

        if os.path.isfile(file_path):
            for folder_name, extensions in file_types.items():
                if any(file.lower().endswith(ext) for ext in extensions):

                    destination_folder = os.path.join(folder, folder_name)
                    os.makedirs(destination_folder, exist_ok=True)

                    shutil.move(file_path, os.path.join(destination_folder, file))
                    break

    label_result.config(text="Done!")

# GUI
root = tk.Tk()
root.title("Smart File Organizer")

label = tk.Label(root, text="Enter folder path:")
label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

button = tk.Button(root, text="Organize", command=organize)
button.pack()

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()