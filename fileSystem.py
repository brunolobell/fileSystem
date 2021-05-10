import os
from fileOperations import *
from folderOperations import *
from disk import Disk, Inode

def fileSystemMain():
  rootFolder = Folder('root', '../root/')
  currentFolder = rootFolder
  folder1 = createFolder('teste', currentFolder)
  print()
  folder2 = createFolder('teste/../teste1', currentFolder)
  print()
  file2 = createFile('aa', currentFolder)
  print('---------------')
  try:
    print('FOLDER1: ', folder1.getName())
    print('FOLDER2: ', folder2.getName())
    print('FILE1: ', file2.getName())
  except:
    pass

fileSystemMain()