import ast
import math
import os

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

  # Function to create 2 files that represent the disk
  # A binary disk and a content disk  
  def createDiskMemory(self):
    serviceFiles = os.listdir('../service')
    if len(serviceFiles) == 0:
      vm = open('../service/VirtualMemory', 'w')
      vm.write(str(self.disk))
      vm.close()
      vmc = open('../service/VirtualMemoryContest', 'w')
      vmc.close()
    else:
      vm = open('../service/VirtualMemory', 'r')
      self.disk = ast.literal_eval(vm.read())
      vm.close()

  # Function to alloc positions in the Byte Map
  def allocPositionsByteMap(self):
    for position in range(0, len(self.disk), blockSize):
      if self.disk[position] == 0:
        self.disk[position] = 1
        return position
    print("The file is larger than the available space!")
    return -1

  def allocPositions(self):
    for position in range(0, len(self.disk), blockSize):
      if self.disk[position] == 0:
        self.disk[position] = 1
        return position
    print("The file is larger than the available space!")
    return -1

  # Function to disk release
  def free(self, position):
    if self.disk[position] == 1:
      self.disk[position] = 0
    else:
      print("The disk position {} is free!".format(position))


class Block:
  def __init__(self, inode, fileSlice):
    self.full = False
    self.blockList = [None] * blockSize
    self.inode = inode
    self.file = fileSlice
    self.newBlock()

  # Create a new block
  def newData(self):
    self.blockList[0] = self.inode
    

# Class to represent an inode
class Inode:
  def __init__(self, blockAddr, file, disk):
    self.blocksAddr = blockAddr
    self.file = file
    self.disk = disk

  # Function to take the blocks addr
  def getBlocksAddr(self):
    return self.blocksAddr

  # Function to take the blocks addr
  def getInode(self):
    return {'file': {'name': self.fileName, 'path': self.filePath, 'size': self.fileSize, 'Type': self.fileType}, 'blocks': self.blocks}
  
  # Function to insert the blocks addr
  def insertBlocks(self):
    startPosition, numberBlocks = self.disk.allocPositions(self.file.size)
    self.blocksAddr.append(startPosition)

  # Function to change a block addr
  def setBlocks(self, position, newAddr):
    self.blocks[position] = newAddr