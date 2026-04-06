File Sorter Automation Script

Overview
This Python script automates file organization by sorting files into folders based on their extensions. It helps keep directories clean, saves time, and demonstrates practical Python automation.

Features
1) Automatically creates folders for different file types if they don’t exist.
2) Supports multiple file types out of the box:
- Text files, Python scripts, CSV, JSON
- Images: JPG, PNG, GIF, BMP
- Audio: MP3, WAV
- Video: MP4, MOV, AVI
- Documents: PDF, Word, Excel, Presentations
- Web files: HTML, CSS, JS
- Archives: ZIP, RAR, 7z
- Others automatically go into other_files
3) Scalable: works with any number of files.
4) Fully automated: just run the script in your folder and it sorts everything.

Usage
1) Clone the repository:
 - Bash
 - git clone <your-repo-url>
 - cd <repo-folder>

2) Place the files you want to sort in the same folder as the script.

3) Run the script:
 - Bash
 - python3 file_sorter.py

4) Watch as your files are automatically moved into the correct folders.

Demo
- Before running the script: mixed files in one folder
- After running the script: files neatly organized into subfolders
screenshot of the terminal output to showcase automation of .txt files being moved into a 'text_files' folder

Requirements
- Python 3.x
- Standard library only (os, shutil) — no external dependencies

Future Improvements
- Add logging for each move operation
- Handle conflicting file names automatically
- Extend support for more file types or custom mappings