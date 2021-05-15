import os

# Function to take currentFolder
def positionStackFolder(path, pathStack):
  normalPath = os.path.normpath(path)
  listPath = normalPath.split('/')
  if '..' not in normalPath:
    return 0
  
  pathPosition = 0
  for p in listPath:
    if p != '..' or pathPosition == len(pathStack) -1:
      break
    pathPosition += 1
  return pathPosition

# Function to create a folder
def createFolder(folderName, stackFolder, diskJSON):
  normalPath = os.path.normpath(folderName)
  position = positionStackFolder(normalPath, stackFolder)
  currentFolder = stackFolder[-(position + 1)] 
  listItems = currentFolder.getItemsDict()
  if normalPath == '.' or normalPath == '..' or normalPath in listItems.keys():
    print("File/directory {} exists in {}!".format(normalPath, currentFolder.getName()))
    return
  listFolders = normalPath.split('/')
  if listFolders[0] == '':
    currentFolder = stackFolder[0]
  
  for folder in listFolders:
    listItems = currentFolder.getItemsDict()
    if folder != '' and folder != '..':
      if folder in listItems.keys():
        currentFolder = listItems[folder]
      else:
        currentFolder.insertItem(folder, Folder(folder, currentFolder.getPath() + '/' + folder))
        currentFolder = currentFolder.getItemsDict[folder]


# Class to represent a folder
class Folder:
  def __init__(self, folderName, folderPath, folderSize = 0, folderDict = {}):
    self.folders = folderDict
    self.name = folderName
    self.path = folderPath
    self.size = folderSize

  # Function to take the items list in this folder
  def getItemsDict(self):
    return self.folders

  # Function to take the folder name
  def getName(self):
    return self.name
  
  # Function to take the folder path
  def getPath(self):
    return self.path

  # Function to take the folder size
  def getSize(self):
    return self.size

  # Function to insert a item in this folder
  def insertItem(self, name, newItem):
    self.folders[name] = newItem

  # Function to remove a fitem of this folder
  def removeFolder(self, itemPosition):
    del self.folders[itemPosition]

  # Function to change the folder name
  def setName(self, newFolderName):
    self.name = newFolderName
  
  # Function to change the folder path
  def setPath(self, newFolderPath):
    self.path = newFolderPath
  
  # Function to change the folder size
  def setSize(self, newFolderSize):
    self.size = newFolderSize