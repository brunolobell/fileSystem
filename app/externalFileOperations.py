import ast
from .disk import Block, Inode

# Load the disk file
def loadExternalFile():
  file = open('../service/VirtualMemory', 'r')
  fileRead = file.readline()
  file.close()
  return ast.literal_eval(fileRead)

# Create a file to use like a disk
def createExtenalFile(disk):
  file = open('../service/VirtualMemory', 'w')
  file.write(str(disk))