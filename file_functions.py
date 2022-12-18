import subprocess as sb
import re

def Insert_to_file(path):
    file = open("TempData/filepaths.txt",'a')
    file.write(path+"\n")
    file.close()

def run_bashConverter():
    sb.run(["/bin/bash TempData/ConvertGIF.sh"],shell=True)
