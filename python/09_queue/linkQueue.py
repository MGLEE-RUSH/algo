# 1.实现了链式队列的入队、出队操作
#
# Author:Lee

class Node():
    '''链式队列的Node节点.'''

    def __init__(self, data, next=None):
        '''Node节点的初始化操作.
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
            data:当前Node节点存储的数据
        '''
        return self.__data

    @data.setter
    def data(self, data):
        '''当前Node节点存储数据设置方法.
        参数:
            data:
        '''
        self.__data = data

    @property
    def next(self):
        '''当前Node节点指向的下一个节点的引用地址.
        返回:
            next:下一个Node节点的引用地址
        '''
        return self.__next

    @next.setter
    def next(self, next):
        '''当前Node节点指向下一个节点的引用地址的设置方法.
        参数:
            next:下一个Node节点的引用地址
        '''
        self.__next = next


class LinkQueue():
    '''链式队列'''

    def __init__(self):
        '''链式队列的初始化方法.'''
        self.__head = None
        self.__tail = None

    def enqueue(self, data):
        '''链式队列入栈.
        参数:
            data:入栈数据值
        '''
        node = Node(data)
        if self.__tail == None:  # 如果当前链式队列为空
            self.__tail = node
            self.__head = node
        else:
            self.__tail.next = node
            self.__tail = node

    def dequeue(self):
        '''链式队列出栈.
        返回:
            data:出栈节点存储的数据
        '''
        if self.__head == None:  # 如果当前链式队列为空
            return None
        else:
            node = self.__head
            if self.__head == self.__tail:
                self.__head = self.__tail = None
            else:
                self.__head = self.__head.next
            return node.data

    def print_all(self):
        '''打印当前队列.'''
        node = self.__head
        if node == None:
            print('当前链表队列还没有数据')
            return

        while node != self.__tail:
            print(str(node.data) + '-->', end='')
            node = node.next
        print(str(node.data))
