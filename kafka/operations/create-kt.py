import os
import glob

PATH=""

def get_latest_file(directory):
    # Get list of all files in the directory
    files = glob.glob(os.path.join(directory, '*'))

    # Check if the directory is empty
    if not files:
        return None

    # Get the latest file by comparing the last modified time
    latest_file = max(files, key=os.path.getmtime)
    return latest_file

if __name__ == "__main__":
    # directory = input("Enter the directory path: ")
    directory = PATH
    
    # Get the latest file in the directory
    latest_file = get_latest_file(directory)

    if latest_file:
        print(f"The latest file is: {latest_file}")
    else:
        print("The directory is empty or does not exist.")
