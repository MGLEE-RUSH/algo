# 1.链式栈，实现了入栈和出栈；
#
# Author:Lee

class Node():
    '''链式栈的Node节点.'''

    def __init__(self, data, next=None):
        '''Node节点的初始化.
        参数:
            data:Node节点存储的数据
            next:下一个Node节点的引用地址
        '''
        self.__data = data
        self.__next = next

    @property
    def data(self):
        '''Node节点的存储数据.
        返回:
            data:当前Node节点存储的数据
        '''
        return self.__data

    @data.setter
    def data(self, data):
        '''Node节点存储数据的设置方法.
        参数:
            data:将要存储的数据
        '''
        self.__data = data

    @property
    def next(self):
        '''Node节点存储的下一个Node节点的引用地址.
        返回:
            next:下一个Node节点的引用地址
        '''
        return self.__next

    @next.setter
    def next(self, next):
        '''Node节点存储下一个Node节点的引用地址的设置方法.
        参数:
            next:下一个Node节点的引用地址
        '''
        self.__next = next


class LinkStack():
    '''链式栈'''

    def __init__(self):
        '''链式栈的初始化，由于链式栈自带自动扩充属性，所以不用像顺序栈那样在初始化的时候指定栈的大小.'''
        self.__head = None

    def push(self, data):
        '''入栈操作.
        参数:
            data:入栈的数据
        '''
        node = Node(data)

        if self.__head == None:  # 如果当前栈为空
            self.__head = node
        else:
            node.next = self.__head
            self.__head = node

    def pop(self):
        '''出栈操作.
        返回:
            data:当前栈顶Node存储的数据
            False:如果当前栈为空，则返回False
        '''
        if self.__head == None:  # 如果当前栈为空
            return False
        else:
            data = self.__head.data
            self.__head = self.__head.next
            return data
