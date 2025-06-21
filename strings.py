#lets mess with file paths (this will also serve as an extra
# file for hangman.py)

#now we will make sure the filepath passed in contains:
#   dir
#   ext
# import strings_var #just to use other variables from different files.
from strings_var import ran_paths, TD_ran_paths
import os


def check_for_dir(path):
    #check for both / and \
    if (path.startswith("./") or path.startswith(".\\")):
        return "Current DIR"
    
    index = path.rfind("/")
    if (index < 0):
        index = path.rfind("\\")

    if (index < 0): #if it found either slash it should not be -1
        return "NO DIR"
    
    return path[:index+1]
    
def get_ext(path):
    index = path.rfind(".")
    if (index < 0 or index <= len(path)/ 2): #there are cases where someone may have ./dir/path/dir/prog, also assuming itll be within the last half of the section (have to change this) 
        return "NO EXT"
    return path[index:]

#filenames can be in current dir and some files may not have an extension
def get_filename(path):
    if (path.startswith("./") or path.startswith(".\\")):
        return path[2:]
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

# def write_to_file(filename):
#     with open(filename, "w") as file: # w overwrites the file and a appends to the end of the file
    
    #return
def check_exists(path):
   if (os.path.exists(path)):
    print(f"FILE EXISTS: {path} ")
   else:
    print(f"FILE DOES NOT EXIST!, Creating {path}")
    file = open(path, "x") # just creating the file 
    file.close()

filepath = input("give me filepath: ")

#do stuff with the filepath

print(f"Directory: ",check_for_dir(filepath))
print(f"Extension: ",get_ext(filepath))
print("File name: ", get_filename(filepath))


# ran_paths = strings_var.ran_paths # if we do not use use __ from file.py we have to do var.___
# TD_ran_path = strings_var.TD_ran_paths

# going to write to a file 
# os is being used to check if the file exists or not.
writable_file = "./test.txt" #itll be within the working the dir
check_exists(writable_file)

with open(writable_file, "w") as file: # do not want to continuely increase file size
    file.write("USING 1D List\n")
    for i in range(len(ran_paths)):
        file.write(f"Path: {ran_paths[i]}\n")
        file.write(f"\tDir: {check_for_dir(ran_paths[i])}\n")
        file.write(f"\tExt: {get_ext(ran_paths[i])}\n")
        file.write(f"\tFile: {get_filename(ran_paths[i])}\n")
    file.write("END\n")
    print("Wrote to file")

with open(writable_file, "a") as file: #using append, it should write to the end 
    file.write("USING 2D List\n")
    for sublist in TD_ran_paths: #diff waw to access stuff
        for item in sublist:
            file.write(f"Path: {item}\n")
            file.write(f"\tDir: {check_for_dir(item)}\n")
            file.write(f"\tExt: {get_ext(item)}\n")
            file.write(f"\tFile: {get_filename(item)}\n")
        file.write("END\n")
    print("Wrote to file")







