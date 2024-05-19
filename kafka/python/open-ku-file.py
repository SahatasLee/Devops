import subprocess
import os
import argparse

DEV_PATH=r"D:\T Kafka Configuration\DEV\Kafka-User"
UAT_PATH=r"D:\T Kafka Configuration\UAT\Kafka-User"
PRD_PATH=r"D:\T Kafka Configuration\PRD\Kafka-User"

def open_with_vscode(path, filename):

    # file_path=f"{path}\{filename}"
    # Construct the full file path using os.path.join
    file_path = os.path.join(path, filename)

    try:
        # Check if file exists
        if not os.path.isfile(file_path):
            # print(f"The file does not exist.")
            file_path = os.path.join(path, f"phase1\{filename}")
            if not os.path.isfile(file_path):
                print(f"The file {file_path} does not exist.")
                return

        # Use subprocess to call the code command
        subprocess.run(["code", file_path], shell=True)
        print(f"Opened {file_path} with VS Code.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to open the file. Command failed with error: {e}")
    except FileNotFoundError:
        print("The 'code' command is not found. Make sure VS Code is installed and the 'code' command is in your PATH.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Open a file with Visual Studio Code.")
    parser.add_argument("username", help="The path to the file to open")

    # Parse the arguments
    args = parser.parse_args()

    # Get the filename from the arguments
    username = args.username.upper()

    # Call the function to open the file with VS Code
    open_with_vscode(DEV_PATH, f"T-KAFKAUSER-{username}.yml")
    # open_with_vscode(f"{UAT_PATH}\T-KAFKAUSER-{username}.yml")
    # open_with_vscode(f"{PRD_PATH}\T-KAFKAUSER-{username}.yml")