import math
import random

class bin_heap():
    # root is 0
    # parent:(i-1)//2
    # left child: 2*i+1
    # right child: 2*i+2

    def __init__(self):
        self.heap_list = []
        self.heap_size = 0  # size of the heap

    # build the min_binary heap, so the min of it is the root
    def heap_min(self):
        if self.heap_size == 0:
            return None
        else:
            return self.heap_list[0]

    # sort the array and maximum is the last index of the array
    def heap_max(self):
        if self.heap_size == 0:
            return None
        else:
            # search the maximum from the last node
            length = self.heap_size - 1
            array = self.heap_list
            max_heap =length
            for i in range(length, -1, -1):
                left_child = 2 * i + 1
                # search the maximum until the node has children
                if left_child > length:
                    if array[max_heap] < array[i - 1]:
                        max_heap = i-1
                else:
                    break
            return array[max_heap]

    # insert the element to the end, and compare it to its parent until the root node
    def insert(self, element):
        self.heap_list.append(element)

        # recompute the size of the heap
        self.heap_size = len(self.heap_list)

        # the index of element and index of it's parent
        i_element = self.heap_size - 1

        # compare it with its parent
        while i_element > 0:
            # i_parent = root
            if self.heap_list[i_element] < self.heap_list[(i_element-1)//2]:
                self.heap_list[i_element], self.heap_list[(i_element-1)//2] = self.heap_list[(i_element-1)//2], self.heap_list[i_element]
            else:
                break
            i_element = (i_element-1)//2

    # Iterate through the array to find the matching value, outputting the index
    def search(self, value):
        if self.heap_size == 0:
            return None
        else:
            length = self.heap_size
            for i in range(0, length):
                if self.heap_list[i] == value:
                    return i

    # compare the child and parent from top to bottom
    def swap_down(self, i):
        length = self.heap_size - 1
        array = self.heap_list
        leftchild = 2 * i + 1

        # when exists child
        while leftchild <= length:
            left_child = leftchild
            right_child = left_child + 1

            # choose the minimal child
            # exists right and left child
            if right_child <= length:
                if array[left_child] < array[right_child]:
                    min_index = left_child
                else:
                    min_index = right_child

            # only exists left child
            if left_child <= length and right_child > length:
                min_index = left_child

            # change the minimal node and parent node
            if array[min_index] < array[i]:
                array[min_index], array[i] = array[i], array[min_index]
                i = min_index

                # enter next layer of binary heap
                leftchild = min_index * 2 + 1
            else:
                break

    def extract(self, value):
        if self.heap_size == 0:
            return None
        else:
            length = self.heap_size - 1
            # get the index of the value
            index = self.search(value)
            remove_item = self.heap_list[index]
            # change the position of current index and last node,and delete the node
            self.heap_list[index], self.heap_list[length] = self.heap_list[length], self.heap_list[index]
            self.heap_list.pop()
            # recalculate the size
            self.heap_size = len(self.heap_list)
            # adjust the heap
            self.swap_down(index)
            print("the value:", remove_item, "has been extracted")

    def build_binheap(self, input_value):
        length = len(input_value)
        for i in range(0, length):
            self.insert(input_value[i])

    def checker(self):
        array = self.heap_list
        length = len(array)
        for i in range(0, length//2-1):
            if array[i] > array[2*i+1] or array[i] > array[2*i+2]:
                print(array[i],array[2*i+1],array[2*i+2])
                print("heap is wrong")
                return

        print("heap is correct")

