from .folderOperations import *
from .file import File

# Function to create a file
def createFile(fileName, stackFolder):
  current = stackFolder[-1]
  index = len(fileName)
  for letter in range(len(fileName)-1, -1, -1):
    if fileName[letter] == '/':
      index = letter + 1
      break
  if index < len(fileName):
    current = currentFolder(fileName, stackFolder)
  if current != -1:
    inPath = current.getItemsDict().keys()
    if fileName[:index] in inPath:
      print("File/directory {} exists in {}!".format(fileName, current.getPath()))
      return
    if fileName[0] != '/':
      fullFileName = current.getPath() + '/' + fileName[:index]
    else:
      fullFileName = current.getPath() + fileName[:index]
    newFile = File(fileName[index:], fullFileName)
    current.insertItem(fileName[:index], newFile)
    return newFile
  return 

def removeFile(fileName, stackFolder):
  current = stackFolder[-1]
  index = len(fileName)
  for letter in range(len(fileName)-1, -1, -1):
    if fileName[letter] == '/':
      index = letter + 1
      break
  if index < len(fileName):
    current = currentFolder(fileName, stackFolder)
  if current != -1:
    items = current.getItemsDict().keys()
