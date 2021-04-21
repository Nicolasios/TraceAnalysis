from ListNode import Node


class TwoQueue():

    def __init__(self, slicetrace):
        self.slicetrace = slicetrace
        self.QueueIn = 0
        self.QueueOut = 0
        self.QueueLRU = 0
        self.FIFOQueueInHead = Node(0)   # 三个队列的头指针
        self.FIFOQueueOutHead = Node(0)
        self.LRUQueueHead = Node(0)
        self.hashmapIn = {}
        self.hashmapOut = {}
        self.hashmapLRU = {}

    def getMissRate(self, cacheSize, blockSize):
        blockNums = int(self.slicetrace.size()/blockSize)+1
        miss = 0
        # 遍历所有分块
        for i in range(blockNums):
            # 遍历各个块
            FIFOQueueInTemp = self.FIFOQueueInHead          # 三个队列当前元素的尾指针
            FIFOQueueOuTemp = self.FIFOQueueOutHead
            LRUQueueTemp = self.LRUQueueHead
            for j in range(blockSize):
                address = self.slicetrace[i*blockNums+j]
                flag1 = adddress in hashmapIn
                flag2 = adddress in hashmapOut
                flag3 = adddress in hashmapLRU
                # 在Am中
                if flag3:
                    # 删除temp
                    temp = hashmapLRU[address]
                    hashmapLRU[address] = temp.next
                    # 插到尾部
                    LRUQueueTemp.next = temp
                    LRUQueueTemp = LRUQueueTemp.next
                # 在Aout中
                elif flag2:
                    # 删除temp
                    temp = hashmapOut[address]
                    hashmapOut[address] = temp.next
                    # 添加到LRU中
                    # 如果LRU已经满了则发生替换，否则添加到队尾
                    if self.QueueLRU <= cacheSize/2

                elif flag1:
                    # do nothing
                    pass

                # 不在队列中
                else:
                    # 队列Ain未满
                    if self.QueueIn <= cacheSize/4:
                        miss += 1
                        FIFOQueueInTemp.next = Node(adddress)
                        hashmapIn[address] = FIFOQueueInTemp.next
                        FIFOQueueInTemp = FIFOQueueInTemp.next
                        self.QueueIn += 1
                    # 队列已经满了则要替换，并且插入到Out队列
                    else:
                        miss += 1
                        self.FIFOQueueInHead = self.FIFOQueueInHead.next
                        self.FIFOQueueInHead.data = 0
                        FIFOQueueInTemp.next = Node(adddress)
                        hashmapIn[address] = FIFOQueueInTemp.next
                        FIFOQueueInTemp = FIFOQueueInTemp.next


if __name__ == "__main__":
    a = {1: Node(1)}
    print(a[1].data)
