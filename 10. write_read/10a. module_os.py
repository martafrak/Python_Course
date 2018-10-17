#module os, add

import os

list = os.listdir("C:/Windows") #add example path
print(list)

list2 = os.listdir(".") #file in current folder
print(list2)

list3 = os.listdir("..") #file in 1 folder up
print(list3)

list4 = os.listdir("../..") #file in 2 folders up etc.
print(list4)

#if we want to check: folder of file?

for item in os.listdir("."):
    if os.path.isfile(item):
        print(item," - It is file")
    else: #we also use: if os.path.isdir(item):
        print("{} - It is folder".format(item))

#create folders
os.mkdir("example")

#rename folders (or file)
os.rename("example","test")

#remove folder
os.rmdir("test")


#create folder and file - PATH


path = "files/new_examples/test.txt" #relative path
print(path)
path2 = os.path.abspath(path) #absolute path
print(path2)
dir_path = os.path.dirname(path) #only folder's path
print(dir_path)
file_path = os.path.basename(path) #only files path
print(file_path)

os.makedirs(dir_path)
open(path,"w").close()

#remove file
os.remove(test.txt)
