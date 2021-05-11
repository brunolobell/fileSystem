import ast
import math
import os

from .externalFileOperations import *

# 1 MB = 10^3 KB = 10^6 B 
# Disk Size in MBs
diskSize = os.getenv('DISK_SIZE', 128)
# Block Size in Bs
blockSize = os.getenv('BLOCK_SIZE', 4 * 1024)


# Class to represent a virtual disk
class Disk:
  def __init__(self):
    self.sizeDisk = diskSize * 1024 * 1024
    self.disk = [0] * self.sizeDisk
    self.createDiskMemory()

  # Function to create a file that represent the disk 
  def createDiskMemory(self):
    serviceFiles = os.listdir('../service')
    if len(serviceFiles) <= 1:
      vm.write(str(self.disk))
    else:
      self.disk = createExtenalFile()

  # Alloc new position
  def allocPosition(self):
    for position in range(len(self.disk)):
      if self.disk[position] == 0:
        self.disk[position] = 1
        return position
    print("Don't have more positions to allocate new blocks!")
    return -1

  # Function to free a position in disk
  def free(self, position):
    if self.disk[position] == 1:
      self.disk[position] = 0
    else:
      print("The disk position {} is free!".format(position))

  # Function to free a disk
  def freeAll(self):
    self.disk = [0] * (self.sizeDisk / blockSize)


# Class to represent a block
class Block:
  def __init__(self, inode):
    self.full = False
    self.blockList = [None] * blockSize
    self.blockList[0] = inode

  # Add data in a block
  def add(self, data):
    if data.getSize() > (blockSize - 1):
      self.full = True
      finalPosition = blockSize - 2
      for index in range(1, finalPosition):
        self.blockList[index] = 1
    else:
      finalPosition = -1
      for index in range(1, data.getSize()):
        self.blockList[index] = 1
    return finalPosition
  
  # Free the block
  def free(self):
    self.blockList = [None] * blockSize

  # Remove a slice of block
  def removeSlice(self, position):
    self.blockList[position] = None


# Class to represent an inode
class Inode:
  def __init__(self, blockAddr, fileName, filePath, fileSize = 0):
    self.blocksAddr = blockAddr
    self.fileName = fileName
    self.filePath = filePath
    self.fileSize = fileSize

  # Function to take the blocks addr
  def getBlocksAddr(self):
    return self.blocksAddr

  # Function to take the blocks addr
  def getInode(self):
    return {'file': {'name': self.fileName, 'path': self.filePath, 'size': self.fileSize}, 'blocks': self.blocks}

  # Function to insert the blocks addr
  def insertBlocks(self, position):
    self.blocksAddr.append(position)

  # Function to change a block addr
  def setBlocks(self, position, newAddr):
    self.blocks[position] = newAddr

  # Change a data file
  def setFileData(self, dataType, data):
    if dataType == 'name':
      self.fileName = data
    elif dataType == 'path':
      self.filePath = data
    elif dataType == 'size':
      self.fileSize = data
    else:
      print("DataType {} not found!".format(dataType))