import os

from app.disk import *
from app.fileOperations import *
from app.folder import Folder
from app.folderOperations import *
from app.externalFileOperations import *

# Commands to pass in terminal
def terminalCommands(command, disk, stackFolder):
  current = stackFolder[-1]
  # cat fileName  
  if command[:3] == 'cat':
    name = command[4:]
    if '/' in command:
      nameIndex = command.rfind('/') + 1
      name = command[nameIndex:]
      current = currentFolder(command[4:nameIndex], stackFolder)
    items = current.getItemsDict()
    changeFile = items[name]
    print(changeFile.getText())
    
  # cd folderName
  elif command[:2] == 'cd':
    openDirectory(command[3:], stackFolder)
  
  #cp file1 file2 
  elif command[:2] == 'cp':
    spCommand = command.split(' ')
    copyFile(spCommand[1], spCommand[2], stackFolder)
  
  #echo "<text here>" >> file
  elif command[:4] == 'echo':
    file = newText(command[5:], stackFolder)
    startText = command.find('"')
    finalText = command.rfind('"')
    nameFile = command[finalText + 5:]
    file.setSize(finalText - startText - 1)
    inode = file.getInode()
    block = disk.getBlocks()[inode.getBlocksAddr()[-1]]
    for elem in command[startText + 1: finalText]:
      disk.allocPosition()
      newSize = block.add(file.getSize(), file)
    if newSize > 0:
      newBlock = Block()
      newBlock.add(newSize, file)
      position = disk.insertBlock(newBlock)
      disk.allocPosition()
      inode.insertBlocks(position)       

  #mkdir folderName
  elif command[:5] == 'mkdir':
    newFolder = createFolder(command[6:], stackFolder)
  
  #mv folderOld folderNew
  elif command[:2] == 'mv':
    commands = command.split(' ')
    renameFolder(commands[2], commands[1], stackFolder)

  #ls
  elif command == 'ls':
    for el in current.getItemsDict():
      print(el, end=' ')
    print()

  #rm fileName 
  elif command[:3] == 'rm ':
    removeFile(command[3:], stackFolder)
  
  #rmdir fileName
  elif command[:5] == 'rmdir':
    removeFolder(command[6:], stackFolder)

  #touch fileName
  elif command[:5] == 'touch':
      newFile = createFile(command[6:], stackFolder)
      if newFile != None:
        disk.allocPosition()
        newBlock = Block()
        newBlock.add(0, newFile)
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
    newBlock.add(0, rootFolder)
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