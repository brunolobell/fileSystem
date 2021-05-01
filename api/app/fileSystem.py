import os
from .fileOperations import File
from .folderOperations import Folder
from .disk import Disk, Inode

# Function to create a file
def createFile(fileName, currentFolder):
  inPath = currentFolder.getItemsList()
  index = 0
  for letter in range(len(fileName)-1, -1, -1):
    if fileName[letter] == '/':
      index = letter + 1
  if index > 0:
    folder = createFolder(fileName[:index], currentFolder.getPath())
  if folder == None:
    return
  if fileName in inPath:
    print("File/directory {} exists in {}!".format(fileName, currentFolder.getPath()))
    return
  fullFileName = currentFolder.getPath() + fileName
  newFile = open(fullFileName, 'w')
  newFile.close()
  if index == 0:
    currentFolder.insertItem(fileName)
  return File(fileName[index:], fullFileName)

# Function to create a folder
def createFolder(folderName, currentFolder):
  inPath = currentFolder.getItemsList()
  if folderName in inPath:
    print("File/directory {} exists in {}!".format(folderName, currentFolder))
    return
  fullFolderName = currentFolder.getPath() + folderName
  if 'api/root' not in os.path.abspath(fullFolderName):
    print("The home directory must be '/'!")
    return
  try:
    os.makedirs(fullFolderName)
  except:
    print("File/directory {} exists in {}!".format(folderName, currentFolder))
    return
  return Folder(folderName, fullFolderName)
    