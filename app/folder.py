# Class to represent a folder
class Folder:
  def __init__(self, folderName, folderPath, folderSize = 0):
    self.folders = dict()
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
  def removeItem(self, item):
    del self.folders[item]

  # Function to change the folder name
  def setName(self, newFolderName):
    self.name = newFolderName

  # Function to change the item name
  def setItemName(self, oldFolderName, newFolderName):
    self.folders[newFolderName] = self.folders.pop(oldFolderName)
  
  # Function to change the folder path
  def setPath(self, newFolderPath):
    self.path = newFolderPath
  
  # Function to change the folder size
  def setSize(self, newFolderSize):
    self.size = newFolderSize