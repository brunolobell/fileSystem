import os
from app.folder import Folder

# Function to take number times to unstack
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

# Function to take the current folder
def currentFolder(pathBase, stackFolder):
  normalPath = os.path.normpath(pathBase)
  count = positionStackFolder(normalPath, stackFolder)
  currentFolder = stackFolder[-(count + 1)]
  listPath = normalPath.split('/')
  start = 0
  if listPath[0] == '':
    start = 1
  currentFolder = stackFolder[0]
  for item in listPath[start:]:
    listItems = currentFolder.getItemsDict()
    if item != '':
      if item in listItems.keys():
        currentFolder = listItems[item]
      else:
        print("{}: No such file or directory".format(item))
        return -1
  return currentFolder

# Function to create a folder
def createFolder(folderName, stackFolder, fromFile = False):
  normalPath = os.path.normpath(folderName)
  position = positionStackFolder(normalPath, stackFolder)
  currentFolder = stackFolder[-(position + 1)] 
  listItems = currentFolder.getItemsDict()
  if normalPath == '.' or normalPath in listItems.keys():
    print("File/directory {} exists in {}!".format(normalPath, currentFolder.getName()))
    return -1
  listFolders = normalPath.split('/')
  if listFolders[0] == '':
    currentFolder = stackFolder[0]
  # Separete directories and add in folder
  index = 0
  for folder in listFolders:
    listItems = currentFolder.getItemsDict()
    path = currentFolder.getPath() + '/' + folder
    if path[1] == '/':
      path = currentFolder.getPath() + folder
    if folder != '' and folder != '..':
      if folder in listItems.keys():
        index += 1
        currentFolder = listItems[folder]
      else:
        newFolder = Folder(folder, path)
        currentFolder.insertItem(folder, newFolder)
        currentFolder = newFolder
  if index >= len(listFolders) and not fromFile:
    print("File/directory {} exists in {}!".format(normalPath, currentFolder.getName()))
    return -1
  return currentFolder
  
# Function to open a directory
def openDirectory(directory, stackFolder):
  if directory == '.':
    return
  normalPath = os.path.normpath(directory)
  count = positionStackFolder(normalPath, stackFolder)
  # Unstack 'count' times the stack folder
  for p in range(count):
    stackFolder.pop()
  # Take the current folder
  currentFolder = stackFolder[-1]
  if directory[0] == '/':
    for path in range(1,stackFolder):
      stackFolder.pop()
    currentFolder = stackFolder[0]
  # Separete directories and stack
  listDirectorys = normalPath.split('/')
  for folder in listDirectorys:
    listItems = currentFolder.getItemsDict()
    if folder != '' and folder != '..':
      if folder in listItems.keys():
        currentFolder = listItems[folder]
        stackFolder.append(currentFolder)
      else: 
        print('{}: No such file or directory'.format(folder))
        return -1

# Function to remove a folder
def removeFolder(folderName, stackFolder):
  normalPath = os.path.normpath(folderName)
  current = stackFolder[-1]
  name = normalPath
  if '/' in normalPath:
    index = normalPath.rfind('/')
    current = currentFolder(normalPath[:index], stackFolder)
    name = normalPath[index + 1:]
  items = current.getItemsDict()
  if name in items.keys():
    if len(items[name].getItemsDict().keys()) == 0:
      current.removeItem(name)
    else:
      print(name, ': Directory not empty')
  else:
    print('{}: No such file or directory'.format(name))

# Function to rename a folder
def renameFolder(newName, directory, stackFolder):
  normalPath = os.path.normpath(directory)
  index = normalPath.rfind('/')
  current = stackFolder[-1]
  if index != -1:
    current = currentFolder(directory[:index], stackFolder)
  items = current.getItemsDict()
  items[directory[index + 1:]].setName(newName)
  current.setItemName(directory[index + 1:], newName)