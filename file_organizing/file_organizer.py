import os
import shutil

def organize_files():
    # main and sub
    main_dir = "MyFiles"
    subdirs = {
        "Docs": [".txt", ".pdf", ".docx"],
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Videos": [".mp4", ".mov", ".avi"]
    }

    # create main
    if not os.path.exists(main_dir):
        os.mkdir(main_dir)
        print(f"Created directory: {main_dir}")

    # subdirectories
    for subdir in subdirs.keys():
        path = os.path.join(main_dir, subdir)
        if not os.path.exists(path):
            os.mkdir(path)
            print(f"Created subdirectory: {path}")

    # organize files
    current_dir = os.getcwd()
    for file in os.listdir(current_dir):
        # skip
        if os.path.isdir(file):
            continue

        # check and move
        file_ext = os.path.splitext(file)[1].lower()
        for subdir, extensions in subdirs.items():
            if file_ext in extensions:
                src = os.path.join(current_dir, file)
                dest = os.path.join(current_dir, main_dir, subdir, file)
                shutil.move(src, dest)
                print(f"Moved: {file} -> {dest}")

if __name__ == "__main__":
    organize_files()
