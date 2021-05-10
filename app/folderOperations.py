import os

# Function to create a folder
def createFolder(folderName, currentFolder):
  fullFolderName = currentFolder.getPath() + folderName
  if 'api/root' not in os.path.abspath(fullFolderName):
    print("The home directory must be '/'!")
    return
  try:
    os.makedirs(fullFolderName)
  except:
    print("File/directory {} exists in {}!".format(folderName, currentFolder.getName()))
    return
  return Folder(folderName, fullFolderName)

# Class to represent a folder
class Folder:
  def __init__(self, folderName, folderPath, folderSize = 0, folderList = []):
    self.folders = folderList
    self.name = folderName
    self.path = folderPath
    self.size = folderSize

  # Function to take the items list in this folder
  def getItemsList(self):
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
  def insertItem(self, newItem):
    self.folders.append(newItem)

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