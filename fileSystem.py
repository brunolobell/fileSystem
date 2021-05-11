import os
from fileOperations import *
from folderOperations import *
from disk import Disk

# Commands to pass in terminal
def terminalCommands(command):
  if command == 'touch':
    pass
  elif command == 'rm':
    pass
  elif command == 'echo':
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
  blocks = []

fileSystemMain()