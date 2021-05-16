from .folderOperations import *

# Class to represent a file
class File:
  def __init__(self, fileName, filePath, fileSize = 0):
    self.name = fileName
    self.path = filePath
    self.size = fileSize

  # Function to take the file name
  def getName(self):
    return self.name
  
  # Function to take the file path
  def getPath(self):
    return self.path

  # Function to take the file size
  def getSize(self):
    return self.size

  # Function to take the file text
  def readFile(self):
    try:
      file = open(self.path, "r")
      return file.read()
    except Exception as err:
      print("Error: {}".format(str(err)))
      return -1
    
  # Function to change the file name
  def setName(self, newfileName):
    self.name = newfileName
  
  # Function to change the file path
  def setPath(self, newfilePath):
    self.path = newfilePath

  # Function to change the file size
  def setSize(self, newfileSize):
    self.size = newfileSize

  # Function to write in the file
  def writeFile(self, text, option = "a"):
    try:
      file = open(self.path, option)
      file.write(text)
      file.close()
    except Exception as err:
      print("Error: {}".format(str(err)))
      return -1


# Function to create a file
def createFile(fileName, stackFolder):
  currentFolder = stackFolder[-1]
  index = 0
  for letter in range(len(fileName)-1, -1, -1):
    if fileName[letter] == '/':
      index = letter + 1
      break
  if index > 0:
    print('FILENAME: ', fileName[:index], '\n')
    currentFolder = createFolder(fileName[:index], stackFolder)
  inPath = currentFolder.getItemsDict()
  if fileName[:index] in inPath:
    print("File/directory {} exists in {}!".format(fileName, currentFolder.getPath()))
    return
  if fileName[0] != '/':
    fullFileName = currentFolder.getPath() + '/' + fileName[:index]
  else:
    fullFileName = currentFolder.getPath() + fileName[:index]
  newFile = File(fileName[index:], fullFileName)
  currentFolder.insertItem(fileName[:index], newFile)
  return newFile