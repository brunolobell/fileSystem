from .folderOperations import *
from .file import File

# Function to copy a file
def copyFile(originalFile, newFile, stackFolder):
  if newFile == originalFile:
    print("Two are the same file")
    return 
  index = originalFile.rfind("/") + 1
  current = stackFolder[-1]
  if '/' in originalFile:
    current = currentFolder(originalFile[:index], stackFolder)
  print(current.getName())
  items = current.getItemsDict()
  print(items)
  text = items[originalFile[index:]].getText()
  fileCP = createFile(newFile, stackFolder)
  if fileCP == None:
    return
  fileCP.writeFile(text)

# Function to create a file
def createFile(fileName, stackFolder):
  current = stackFolder[-1]
  index = 0
  for letter in range(len(fileName)-1, -1, -1):
    if fileName[letter] == '/':
      index = letter + 1
      break
  if index > 0:
    current = currentFolder(fileName[:index], stackFolder)
  if current != -1:
    inPath = current.getItemsDict().keys()
    if fileName[index:] in inPath:
      print("File/directory {} exists in {}!".format(fileName, current.getPath()))
      return
    if fileName[0] != '/':
      fullFileName = current.getPath() + '/' + fileName[:index]
    else:
      fullFileName = current.getPath() + fileName[index:]
    newFile = File(fileName[index:], fullFileName)
    current.insertItem(fileName[index:], newFile)
    return newFile
  return 

# Function to remove a file
def removeFile(fileName, stackFolder):
  current = stackFolder[-1]
  index = 0
  for letter in range(len(fileName)-1, -1, -1):
    if fileName[letter] == '/':
      index = letter + 1
      break
  if index > 0:
    current = currentFolder(fileName[:index], stackFolder)
  if current != -1:
    current.removeItem(fileName[index:])

# Function to insert text in a file
def newText(text, stackFolder):
  startIndex = text.find('"')
  endIndex = text.rfind('"')
  nameIndex = endIndex + 5
  current = stackFolder[-1]
  if '/' in text:
    nameIndex = text.rfind('/')
    current = currentFolder(text[endIndex + 5 : nameIndex], stackFolder)
    if current == -1:
      return
  items = current.getItemsDict()
  if text[-2:] != '-w':
    changeFile = items[text[nameIndex:]]
    changeFile.writeFile(text[startIndex + 1 : endIndex])
  else:
    changeFile = items[text[nameIndex:-3]]
    changeFile.writeFile(text[startIndex + 1 : endIndex], 'w')
  return changeFile