import pathlib
import os
from string import ascii_uppercase

# Write a Python program to list only directories, files and all directories, files in a specified path.
def listDirs(p):
    print([x.name for x in os.scandir(path = p) if x.is_dir()])

def listFiles(p):
    print([x.name for x in os.scandir(path = p) if x.is_file()])

def listDirsAndFiles(p):
    print([x.name for x in os.scandir(path = p)])

# Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path

def checkPath(p):
    # check for existence
    exist_status = os.access(path = p, mode = os.F_OK)
    print(f"Existence: {exist_status}")
    # check for readibility 
    read_status = os.access(path = p, mode = os.R_OK)
    print(f"Readibility: {read_status}")
    # check for writability 
    write_status = os.access(path = p, mode = os.W_OK)
    print(f"Writability: {write_status}")
    # check for executability
    exec_status = os.access(path = p, mode = os.X_OK)
    print(f"Executability: {exec_status}")

# Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
def existAndRetrievePathInfo(p):
    exist_status = os.access(path = p, mode = os.F_OK)
    if exist_status:
        print(f"File: {os.path.basename(p)}")
        print(f"Directory: {os.path.dirname(p)}")
    else:
        print("Path is not executable")

# Write a Python program to count the number of lines in a text file.
def countLines(filename):
    file = open(filename, 'r')
    count = 0
    for line in file:
        count += 1
    return count


# Write a Python program to write a list to a file.
def writeToFile(filename, new_list):
    file = open(filename, 'a')
    file.write(str(new_list))
    file.close()

    file = open(filename, 'r')
    print(file.read())


# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
def generateFiles():
    for ch in ascii_uppercase:
        file = open(f"./files/{ch}.txt", 'x')
        file.close()

    print("All files have been successfully generated")


# Write a Python program to copy the contents of a file to another file
def copyContent(init_filename, target_filename):
    init_file = open(init_filename, 'r')
    file_content = init_file.read()
    init_file.close()

    target_file = open(target_filename, 'w')
    target_file.write(str(file_content))
    target_file.close()
    print("Successfully copied")

    target_file = open(target_filename, 'r')
    print(target_file.read())
    target_file.close()


# Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
def deleteFile(p):
    if os.path.exists(p):
        os.remove(p)
        print("Successfully deletede the file")
    else:
        print("File does not exist")

def main():
    path = '..'
    print("Task 1")
    listDirs(path)
    listFiles(path)
    listDirsAndFiles(path)

    print("Task 2")
    checkPath(path)

    print("Task 3")
    existAndRetrievePathInfo('../tsis5/regexp_tasks.py')

    print("Task 4")
    print(f"Number of lines in a file demofile.txt = {countLines('demofile.txt')}")

    print("Task 5")
    writeToFile("demofile2.txt", ["Hello", "World"])

    
    print("Task 6")
    #generateFiles()

    print("Task 7")
    copyContent('demofile.txt', 'demofile3.txt')
    
    print("Task 8")
    deleteFile("./demofile2.txt")

if __name__ == "__main__":
    main() 
