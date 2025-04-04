import os
from datetime import datetime

def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print (f"File name {filename}:  Created Successfully!")
    except FileExistsError:
        print (f"File Name {filename} already exists!")    
    except Exception as E:
        print("An error occured !")


def view_all_files():
    files = os.listdir()
    if not files:
        print("No files exists.")
    else:
        print("Files in directory.")
        for file in files:
            print(file)


def delete_file(filename):
    try:
        os.remove(filename)
        print(f"File Name {filename} has been removed.")
    except FileNotFoundError:
        print("File Not Found!")
    except Exception as E:
        print("An error occured !")


def read_file(filename):
    try:
        with open(filename,'r') as f:
            content = f.read()
            print (f"Content of '{filename}': \n{content}")
    except FileNotFoundError:
        print ("File not found!")
    except Exception as E:
        print("An error occured!")


def edit_file(filename):
    try:
        with open(filename, 'a') as f:
            content = input('Enter data to add = ')
            f.write(content + "\n")
            print(f'Content added to {filename} Successfully!')
    
    except FileNotFoundError:
        print(f"{filename} doesn't exist!")
    
    except Exception as e:
        print('An error occurred!')

def search_in_file(filename, search_text):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            found = False
            print(f"\nSearching for '{search_text}' in {filename}:")
            for i, line in enumerate(lines, 1):
                if search_text in line:
                    print(f"Line {i}: {line.strip()}")
                    found = True
            if not found:
                print("Text not found in file.")
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_file_info(filename):
    try:
        stats = os.stat(filename)
        created = datetime.fromtimestamp(stats.st_ctime)
        modified = datetime.fromtimestamp(stats.st_mtime)
        size = stats.st_size

        print(f"\nFile Information for {filename}:")
        print(f"Size: {size} bytes")
        print(f"Created: {created}")
        print(f"Last Modified: {modified}")
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    while True:
        print('FILE MANAGEMENT APP')
        print('1: Create file')
        print('2: View all files')
        print('3: File information')
        print('4: Delete file')
        print('5: Read file')
        print('6: Edit file')
        print('7: Search in file')
        print('8: Exit')

        choice = input('Enter your choice (1-8) = ')

        if choice == '1':
            filename = input("Enter the file-name to create = ")
            create_file(filename)

        elif choice == '2':
            view_all_files()

        elif choice == '3':
            filename = input('Enter file name: ')
            get_file_info(filename)

        elif choice == '4':
            filename = input('Enter the name of file you want to delete = ')
            delete_file(filename)

        elif choice == '5':
            filename = input('Enter file name to read = ')
            read_file(filename)

        elif choice == '6':
            filename = input('Enter file name to edit = ')
            edit_file(filename)

        elif choice == '7':
            filename = input('Enter file name: ')
            search_text = input('Enter text to search: ')
            search_in_file(filename, search_text)

        elif choice == '8':
            print("Exiting File Management App.")
            exit()

        else:
            print("Invalid choice! Please enter a number between 1 and 8.")


if __name__=="__main__":
    main()



    
