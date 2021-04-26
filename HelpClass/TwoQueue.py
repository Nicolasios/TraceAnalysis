from HelpClass.ListNode import *
import json


class TwoQueue():

    def __init__(self, slicetrace):
        self.slicetrace = slicetrace

    def getMissRate(self, cacheSize, blockSize):
        blockNums = int(len(self.slicetrace)/blockSize)+1
        # 遍历所有分块
        for i in range(blockNums):
            miss = 0
            hit = 0
            hashmapIn = {}
            hashmapOut = {}
            hashmapLRU = {}
            QueueIn = 0
            QueueOut = 0
            QueueLRU = 0
            FIFOQueueInHead = Node(0)  # 清零
            FIFOQueueOutHead = Node(0)
            LRUQueueHead = Node(0)
            # 遍历各个块
            FIFOQueueInTemp = FIFOQueueInHead          # 三个队列当前元素的尾指针
            FIFOQueueOutTemp = FIFOQueueOutHead
            LRUQueueTemp = LRUQueueHead
            for j in range(blockSize):
                if i*blockSize+j >= len(self.slicetrace):
                    break
                address = self.slicetrace[i*blockSize+j]
                flag1 = address in hashmapIn
                flag2 = address in hashmapOut
                flag3 = address in hashmapLRU
                # 在Am中
                if flag3:
                    hit += 1
                    # 获取要从LRU队列中删除且插到尾部的节点
                    pre = hashmapLRU[address]
                    temp = pre.next
                    pre.next = temp.next
                    if pre.next == None:
                        LRUQueueTemp = pre
                        hashmapLRU.pop(address)
                    else:
                        hashmapLRU[pre.next.data] = pre
                    # 插到尾部
                    LRUQueueTemp.next = temp
                    temp.next = None
                    hashmapLRU[address] = LRUQueueTemp
                    LRUQueueTemp = LRUQueueTemp.next
                # 在Aout中
                elif flag2:
                    hit += 1
                    # 在Out队列删除该节点
                    pre = hashmapOut[address]
                    temp = pre.next
                    pre.next = temp.next
                    hashmapOut.pop(address)
                    if pre.next == None:
                        FIFOQueueOutTemp = pre
                    else:
                        hashmapOut[pre.next.data] = pre
                    QueueOut -= 1
                    # 添加到LRU中
                    # 如果LRU已经满了则发生替换，否则添加到队尾
                    if QueueLRU < cacheSize/2:
                        LRUQueueTemp.next = Node(temp.data)
                        hashmapLRU[temp.data] = LRUQueueTemp
                        LRUQueueTemp = LRUQueueTemp.next
                        QueueLRU += 1  # 个数加一

                    else:
                        # 删除头结点的下一个节点
                        LRUQueueHead = LRUQueueHead.next
                        address_out = LRUQueueHead.data
                        hashmapLRU.pop(address_out)
                        LRUQueueHead.data = 0
                        # 插入到队尾，并移动队尾指针
                        LRUQueueTemp.next = Node(temp.data)
                        hashmapLRU[temp.data] = LRUQueueTemp
                        LRUQueueTemp = LRUQueueTemp.next

                elif flag1:
                    hit += 1
                    # do nothing
                    pass

                # 不在队列中
                else:
                    # 队列Ain未满
                    if QueueIn < cacheSize/4:
                        miss += 1
                        FIFOQueueInTemp.next = Node(address)
                        hashmapIn[address] = FIFOQueueInTemp
                        FIFOQueueInTemp = FIFOQueueInTemp.next
                        QueueIn += 1
                    # 队列已经满了则要替换，并且插入到Out队列
                    else:
                        miss += 1
                        FIFOQueueInHead = FIFOQueueInHead.next
                        address_in = FIFOQueueInHead.data
                        hashmapIn.pop(address_in)
                        FIFOQueueInHead.data = 0
                        FIFOQueueInTemp.next = Node(address)
                        hashmapIn[address] = FIFOQueueInTemp
                        FIFOQueueInTemp = FIFOQueueInTemp.next
                        # 插到Aout中
                        if QueueOut < cacheSize/4:
                            # Aout未满直接插入，计数器加一
                            FIFOQueueOutTemp.next = Node(address_in)
                            hashmapOut[address_in] = FIFOQueueOutTemp
                            FIFOQueueOutTemp = FIFOQueueOutTemp.next
                            QueueOut += 1
                        else:
                            # Aout已满,丢弃头结点，插入到尾节点
                            FIFOQueueOutHead = FIFOQueueOutHead.next
                            hashmapOut.pop(FIFOQueueOutHead.data)
                            FIFOQueueOutHead.data = 0
                            FIFOQueueOutTemp.next = Node(address_in)
                            hashmapOut[address_in] = FIFOQueueOutTemp
                            FIFOQueueOutTemp = FIFOQueueOutTemp.next
            return miss, hit
