from subprocess import call as sb
import re

def Insert_to_file(path):
    file = open("TempData/filepaths.txt",'a')
    name = get_Name(path)
    file.write(path+"\n")
    file.close()

def clean_file():
    file = open("TempData/filepaths.txt",'w')
    file.write("")
    file.close()

def run_bashConverter():
    sb.call("./ConvertGIF", shell=True)

def get_Name(path):#get gif file name
    try: 
        target1 = path.rindex("/")+1
        target2 = path.rindex(".gif")
        
        return path[target1:target2]

    except AttributeError :
        return "Gif name was not found"
