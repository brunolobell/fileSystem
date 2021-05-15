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
    self.diskMap = [0] * self.sizeDisk
    self.blocks = []
    self.createDiskMemory()

  # Function to create a file that represent the disk 
  def createDiskMemory(self):
    serviceFiles = os.listdir('../service')
    if len(serviceFiles) <= 1:
      self.diskMap = loadExternalFile()
    else:
      createExtenalFile(self.diskMap)

  # Alloc new position
  def allocPosition(self):
    for position in range(len(self.disk)):
      if self.diskMap[position] == 0:
        self.diskMap[position] = 1
        return position
    print("Don't have more positions to allocate new blocks!")
    return -1

  # Function to free a position in disk
  def free(self, position):
    if self.diskMap[position] == 1:
      self.diskMap[position] = 0
    else:
      print("The disk position {} is free!".format(position))

  # Function to free a disk
  def freeAll(self):
    self.diskMap = [0] * (self.sizeDisk / blockSize)
    self.blocks = []

  # Function to insert a block in disk
  def insertBlock(self, block):
    self.blocks.append(block)

# Class to represent a block
class Block:
  def __init__(self, inode):
    self.full = False
    self.blockList = [None, None]
    self.blockList[0] = inode

  # Add data in a block
  def add(self, data, lastSize = 0):
    if (data.getSize() - lastSize) > (blockSize - 1):
      self.full = True
      newSize = data.getSize() - blockSize + 1
      self.blockList[1] = data
    else:
      newSize = -1
      self.blockList[1] = data
    return newSize


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