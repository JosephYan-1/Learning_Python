#lets mess with file paths (this will also serve as an extra
# file for hangman.py)

#now we will make sure the filepath passed in contains:
#   dir
#   ext
import os

def check_for_dir(path):
    #check for both / and \
    index = path.rfind("/")
    if (index < 0):
        index = path.rfind("\\")

    if (index < 0): #if it found either slash it should not be -1
        return "NO DIR"
    
    return path[:index]
    
def get_ext(path):
    index = path.rfind(".")
    if (index < 0 or index <= len(path)/ 2): #there are cases where someone may have ./dir/path/dir/prog, also assuming itll be within the last half of the section (have to change this) 
        return "NO EXT"
    return path[index:]

#filenames can be in current dir and some files may not have an extension
def get_filename(path):
    index_ext = path.rfind(".")
    if (index_ext < 0):
        index_ext = len(path)
    
    index_dir = path.rfind("/")
    if (index_dir < 0):
        index_dir = path.rfind("\\")
    
    if (index_dir < 0):
        #just incase only a file name is passed in, we dont want to cut off the first letter
        index_dir = 0 #we want to remove the /, also making it zero because it should -1 and we would add one
    else :
        index_dir += 1 
    return path[index_dir:index_ext]

def write_to_file(filename, exists)
filepath = input("give me filepath: ")

#do stuff with the filepath

print(f"Directory: ", check_for_dir(filepath))
print(f"Extension: ",get_ext(filepath))
print("File name: ", get_filename(filepath))

# going to write to a file 
# os is being used to check if the file exists or not.

writable_file = "./test.txt" #itll be within the working the dir
if (os.path.exists(writable_file)):
    print("FILE EXISTS, WRITING TO FILE")
else:
    print(f"FILE DOES NOT EXIST!, Creating {writable_file}")


