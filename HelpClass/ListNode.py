# 节点类
class Node(object):
    # 初始化，需要传入节点的数据
    def __init__(self, data):
        self.data = data
        self.next = None

    # 返回节点的数据
    def get_data(self):
        return self.data

    # 更新节点的数据
    def set_data(self, new_data):
        self.data = new_data

    # 返回后继节点
    def get_next(self):
        return self.next

    # 变更后继节点
    def set_next(self, new_next):
        self.next = new_next
