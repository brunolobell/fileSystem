import ast
import os
import pickle

# write an object in the binary file (VirtualMemory)
def writeExternalFile(obj):
  with open('service/VirtualMemory', 'wb') as output:
    fileDump = pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

# Load the memory file
def loadExternalFile():
  if len(os.listdir('service')) < 1:
    return -1 
  with open('service/VirtualMemory', 'rb') as memory:
    fileLoad = pickle.load(memory) 
  return fileLoad

# Create a file with bytemap
def createByteMap(disk):
  file = open('service/VirtualMemory.bmt', 'w')
  file.write(str(disk))
  file.close()