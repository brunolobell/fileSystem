import os

from app.disk import *
from app.fileOperations import *
from app.folder import Folder
from app.folderOperations import *
from app.externalFileOperations import *

# Commands to pass in terminal
def terminalCommands(command, disk, stackFolder):
  current = stackFolder[-1]
  # cat file 
  if command[:3] == 'cat':
    name = command[4:]
    if '/' in command:
      nameIndex = command.rfind('/') + 1
      name = command[nameIndex:]
      current = currentFolder(command[4:nameIndex], stackFolder)
    items = current.getItemsDict()
    changeFile = items[name]
    print(changeFile.getText())

  elif command[:2] == 'cd':
    openDirectory(command[3:], stackFolder)

  elif command[:2] == 'cp':
    spCommand = command.split(' ')
    copyFile(spCommand[1], spCommand[2], stackFolder)
  
  elif command[:4] == 'echo':
    file = newText(command[5:], stackFolder)
    startText = command.find('"')
    finalText = command.rfind('"')
    nameFile = command[finalText + 5:]
    for character in command[startText + 1, finalText]:
      disk.allocPosition()
    
  elif command[:5] == 'mkdir':
    newFolder = createFolder(command[6:], stackFolder)

  elif command[:2] == 'mv':
    commands = command.split(' ')
    renameFolder(commands[2], commands[1], stackFolder)

  elif command == 'ls':
    for el in current.getItemsDict():
      print(el, end=' ')
    print()

  elif command[:3] == 'rm ':
    removeFile(command[3:], stackFolder)

  elif command[:5] == 'rmdir':
    removeFolder(command[6:], stackFolder)

  elif command[:5] == 'touch':
      newFile = createFile(command[6:], stackFolder)
      if newFile != None:
        disk.allocPosition()
        newBlock = Block()
        newBlock.add(newFile)
        position = disk.insertBlock(newBlock)
        newInode = Inode(position, command[6:], current.getPath())
        newFile.setInode(newInode)

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