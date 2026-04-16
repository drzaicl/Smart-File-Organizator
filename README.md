# 📁 Smart File Organizer (GUI)

A simple Python desktop application that automatically organizes files in a selected folder based on file type.

##  Features

* Organize files with one click
* Automatically sorts files into folders:

  * Images (.jpg, .png)
  * Videos (.mp4)
  * Documents (.txt)
* Simple and clean GUI (Tkinter)
* Fast and easy to use

##  How It Works

1. User enters a folder path
2. Clicks the **Organize** button
3. The program scans all files in the folder
4. Files are automatically moved into categorized subfolders

##  GUI Preview (Concept)

* Input field → enter folder path
* Button → start organizing
* Status label → shows result

##  Usage

1. Run the program:

```bash
python main.py
```

2. Enter the folder path (example):

```text
C:/Users/YourName/Downloads
```

3. Click **Organize**

4. Done 

---

## 🛠 Tech Used

* Python
* Tkinter (GUI)
* os (file handling)
* shutil (file moving)

---

##  Example

Before:

```text
Downloads/
  file.jpg
  video.mp4
  notes.txt
```

After:

```text
Downloads/
  Images/file.jpg
  Videos/video.mp4
  Documents/notes.txt
```

---

##  Notes

* Only files (not folders) are processed
* Existing folders will not be affected
* File extensions are case-insensitive

---

## 💡 Future Improvements

* Add file browser (no manual path input)
* Support more file types
* Add "Others" category
* Create .exe version for easy sharing

---

## 👊 Author
      drzaicl

Built as part of learning Python automation and GUI development.
