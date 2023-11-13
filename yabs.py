import configparser
import os
import json

config = configparser.ConfigParser()
config.read_file(open(r'tests/project.cfg'))

# project section
compiler = config.get("project", "compiler")
output = config.get("project", "output")

# arguments section
arguments = config.get("arguments", "arguments")
libs = config.get("arguments", "libs")

# source files
sourceDir = config.get("source", "directory")
sourceFiles = json.loads(config.get("source", "files"))
headers = config.get("source", "headers")

files = ""

for file in sourceFiles:
    files += f"{sourceDir}/{file} "

files.replace("[", "")
files.replace("]", "")
files.replace(",", "")

command = f"{compiler} {arguments} -o {output} {files} -I{headers} {libs}"

os.system(command)