# get_names.py

import os


def main():
    cwd = os.getcwd()
    print(f"Current directory: {cwd}\n")

    found_folders = 0

    for item in os.listdir(cwd):
        item_path = os.path.join(cwd, item)

        if os.path.isdir(item_path):
            found_folders += 1
            name_file = os.path.join(item_path, "name.txt")
            with open(name_file, "w") as f:
                f.write(item + "\n")
            print(f"✅ Created: {name_file}")

    if found_folders == 0:
        print("⚠️ No folders found in this directory!")


if __name__ == "__main__":
    main()
