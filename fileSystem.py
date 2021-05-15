import os
from .app.fileOperations import *
from .app.folderOperations import *
from .app.disk import Disk, Inode, Block

# Commands to pass in terminal
def terminalCommands(command, disk, currentFolder):
  if command[:5] == 'touch':
    newFile = createFile(command[6:], currentFolder)
    position = disk.allocPosition()
    newInode = Inode(position, command[6:], currentFolder.getPath())
    newBlock = Block(newInode)
    newBlock.add(File)
    disk.insertBlock(newBlock)
  elif command == 'rm':
    pass
  elif '"' in command or '"' in command:
    pass
  elif command == 'cat':
    pass
  elif command == 'cp':
    pass
  elif command == 'mv':
    pass
  elif command == 'mkdir':
    pass
  elif command == 'rmdir':
    pass
  elif command == 'cd':
    pass
  elif command == 'mv':
    pass
  else:
    print("Command {} not found!".format(command))

# Main
def fileSystemMain():
  memory = Disk()
  
  

fileSystemMain()