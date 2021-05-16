# Class to represent a file
class File:
  def __init__(self, fileName, filePath, fileSize = 0):
    self.inode = None
    self.name = fileName
    self.path = filePath
    self.size = fileSize
    self.text = ''

  # Function to take the inode file
  def getInode(self):
    return self.inode

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
  def getText(self):
    return self.text

  # Function to change the inode
  def setInode(self, inode):
    self.inode = inode

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
  def writeFile(self, text, option = 'a'):
    if option == 'a' and self.text != '':
      self.text = self.text + '\n' + text
    else:
      self.text = text