import os

from app.disk import *
from app.fileOperations import *
from app.folderOperations import *
from app.externalFileOperations import *

# Commands to pass in terminal
def terminalCommands(command, disk, stackFolder):
  currentFolder = stackFolder[-1]
  if command[:5] == 'touch':
    newFile = createFile(command[6:], stackFolder)
    position = disk.allocPosition()
    newInode = Inode(position, command[6:], currentFolder.getPath())
    newBlock = Block(newInode)
    newBlock.add(newFile)
    disk.insertBlock(newBlock)
  elif command[:2] == 'rm':
    pass
  elif command[:4] == 'echo':
    pass
  elif command[:3] == 'cat':
    pass
  elif command[:2] == 'cp':
    pass
  elif command[:2] == 'mv':
    pass
  elif command[:5] == 'mkdir':
    newFolder = createFolder(command[6:], stackFolder)
    disk.getBlocks()[0].add(newFolder)
  elif command[:5] == 'rmdir':
    pass
  elif command[:2] == 'cd':
    openDirectory(command[3:], stackFolder)
  elif command[:5] == 'touch':
    pass
  elif command == 'ls':
    for el in currentFolder.getItemsDict().keys():
      print(el, end=' ')
    print()
  else:
    print("Command {} not found!".format(command))

# Main
def fileSystemMain():
  memory = loadExternalFile()
  if memory == -1:
    rootFolder = Folder('root', '/')
    memory = Disk()
    writeExternalFile(memory)
    newBlock = Block()
    newBlock.add(rootFolder)
    memory.insertBlock(newBlock)
    #createByteMap(memory.getDiskMap())
  # Take root in Disk -> Block -> Folder[0]
  rootFolder = memory.getBlocks()[0].getItems()[0]
  stackDirectory = [rootFolder] 
  while(1):
    writeExternalFile(memory)
    command = input('USER@PC:{}$ '.format(stackDirectory[-1].getPath()))
    terminalCommands(command, memory, stackDirectory)

fileSystemMain()