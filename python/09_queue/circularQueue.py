# 1.实现循环链式队列的入队、出队操作
#
# Author:Lee

class Node():
    '''循环链式队列的Node节点'''

    def __init__(self, data=None, next=None):
        '''Node节点的初始化.
        参数:
            data:Node节点存储的数据
            next:Node节点指向的下一个节点的引用地址
        '''
        self.__data = data
        self.__next = next

    @property
    def data(self):
        '''获取Node节点存储的数据.
        返回:
            data:Node节点存储的数据
        '''
        return self.__data

    @data.setter
    def data(self, data):
        '''Node节点存储数据的设置方法.
        参数:
            data:Node节点存储的数据
        '''
        self.__data = data

    @property
    def next(self):
        '''获取Node节点指向下一个节点的引用地址.
        返回:
            next:Node节点指向一下一个节点的引用地址
        '''
        return self.__next

    @next.setter
    def next(self, next):
        '''Node节点指向下一个节点的引用地址的设置方法.
        参数:
            next:下一个Node节点的引用地址
        '''
        self.__next = next


class CircularQueue():
    '''循环链式队列'''

    def __init__(self, n):
        '''循环链式队列的初始化方法.
        参数:
            n:循环链式队列的长度
        '''
        self.__size = n  # 循环链式队列长度
        self.__num = 0  # 村换链式队列实际存储数据个数
        node = Node()
        self.__head = self.__tail = node
        for i in range(1, n):
            node = Node()
            self.__tail.next = node
            self.__tail = node
        self.__tail.next = self.__head
        self.__tail = self.__head

    def enqueue(self, data):
        '''循环链式队列入队.
        参数:
            data:入队数据值
        返回:
            True:入队成功
            False:入队失败
        '''
        if self.__num == self.__size:  # 如果队列满了
            return False
        else:
            self.__tail.data = data
            self.__tail = self.__tail.next
            self.__num += 1
            return True

    def dequeue(self):
        '''循环链式队列出队.
        返回:
            data:出队Node节点存储数据
        '''
        if self.__num == 0:  # 如果当前队列为空
            return None
        else:
            data = self.__head.data
            self.__head = self.__head.next
            self.__num -= 1
            return data

    def print_all(self):
        '''打印当前循环链表存储的数据.'''
        if self.__num == 0:
            print('当前循环队列里面还没有数据.')
            return

        node = self.__head
        index = 0
        while index < self.__num - 1:
            print(str(node.data) + '-->', end='')
            node = node.next
            index += 1
        print(str(node.data))
