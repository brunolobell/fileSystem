import math
import os

# 1 MB = 10^3 KB = 10^6 B 
# Disk Size in MBs
diskSize = os.getenv('DISK_SIZE', 128)
# Block Size in Bs
blockSize = os.getenv('BLOCK_SIZE', 4000)

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


# Class to represent a virtual disk
class Disk:
  def __init__(self):
    self.size = diskSize * (10**6)
    self.disk = [0] * self.size
  
  # Function to alloc positions in the disk
  def allocPositions(self, fileSize = 0):
    numberBlocks = math.ceil(fileSize / blockSize)
    if numberBlocks > 0:
      for position in range(len(self.disk)):
        if self.disk[position] == 0:
          if (position + numberBlocks) <= self.size:
            self.size -= numberBlocks
            self.disk[position : position + numberBlocks] = [1] * numberBlocks
            return position, numberBlocks
    print("The file is larger than the available space!")
    return -1

  # Function to disk release
  def free(self, position):
    if self.disk[position] == 1:
      self.disk[position] = 0
    else:
      print("The disk position {} is free!".format(position))

  