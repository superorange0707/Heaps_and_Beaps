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



class beap():
    # root=0
    # the number of node in each layer <= the height of the layer-1. so the height is sqrt(2*index+0.75)-0.5
    # left_parent=i-height
    # right_parent=i-height+1
    # left_child=i+height
    # right_child=i+height+1
    def __init__(self):
        self.beap_list = []
        self.beap_size = 0

    def min_beap(self):
        if self.beap_size == 0:
            return None
        else:
            return self.beap_list[0]

    def getheight(self, index):
        height = math.ceil(math.sqrt(2*index+0.75)-0.5)
        return height

    # get the range of the current layer of the node
    def getrange(self, height):
        layer_left = height * (height - 1) // 2
        layer_right = height * (height + 1) // 2 - 1
        return layer_left, layer_right

    # the maximum of the beap appear in the node without child
    def max_beap(self):
        if self.beap_size == 0:
            return None
        else:
            # set the last node as the maximum firstly
            length = self.beap_size - 1
            array = self.beap_list
            max_beap = length
            # find the maximum from the last node to the node has children
            for i in range(length, -1, -1):
                h = self.getheight(i)
                left_child = i + h
                if left_child > length:
                    if array[max_beap] < array[i - 1]:
                        max_beap = i-1
                else:
                    break
            return array[max_beap]

    def max_parent(self, index):
        height = self.getheight(index)
        left_range, right_range = self.getrange(height - 1)
        left_parent = index - height
        right_parent = index - height + 1

        # The node is the first node of the current layer， only exits right parent
        if left_parent < left_range:
            return right_parent

        # The node is the last node of the current layer, only exits left parent
        elif right_parent > right_range:
            return left_parent

        # exits both left and right parent, find the max parent to replace
        else:
            if self.beap_list[left_parent] > self.beap_list[right_parent]:
                return left_parent
            else:
                return right_parent

    # insert the node to the last place in the beap and compare it to its parent until the root node
    def insert(self, element):
        self.beap_list.append(element)

        # recompute the size of the heap
        self.beap_size = len(self.beap_list)

        # the index of element and index of it's parent
        i_element = self.beap_size - 1
        mp_index = self.max_parent(i_element)
        while mp_index >= 0:
            if self.beap_list[i_element] < self.beap_list[mp_index]:
                self.beap_list[i_element], self.beap_list[mp_index] = self.beap_list[mp_index], self.beap_list[i_element]
                i_element = mp_index
                mp_index = self.max_parent(i_element)
            else:
                break

    def search(self, value):
        if self.beap_size == 0:
            return None
        else:
            # search from the first node of the last layer
            length = self.beap_size - 1
            # get the range of last layer
            height = self.getheight(length)
            left_range, right_range = self.getrange(height)
            # get the right parent of first node in the last layer
            # because search form the left node,so left parent is the current node of the next layer.
            right_parent = left_range - height + 1

            # search the value in the beap
            while 1:
                # if the value smaller than the right parent, the current node goes to the previous layer
                if value < self.beap_list[left_range]:
                    left_range = right_parent
                    height_index = self.getheight(left_range)
                    right_parent = left_range - height_index + 1

                # If the value is greater than the current node then go to the right child of the node
                # there are two case of right child
                if value > self.beap_list[left_range]:
                    height_i = self.getheight(left_range)
                    rc_leftrange = left_range + height_i + 1

                    # if the current node exists right child
                    if rc_leftrange <= length:
                        left_range = rc_leftrange
                        height_i = self.getheight(left_range)
                        right_parent = left_range - height_i + 1

                    # if the current node doesn't have right child, go the right parent of previous layer
                    else:
                        last_height = self.getheight(left_range) - 1
                        # get range of previous layer
                        last_leftrange, last_rightrange = self.getrange(last_height)
                        # enter the previous layer
                        right_parent = left_range - height_i + 1
                        left_range = right_parent
                        # recalculate the right parent of current ndoe
                        height_i = self.getheight(left_range)
                        right_parent = left_range - height_i + 1

                        # when current node >the right range, it means it's the latest node of search in the beap
                        if left_range > last_rightrange:
                            return None

                # find the index of value
                if value == self.beap_list[left_range]:
                    return left_range

                # if the index of value is 0, it will output in the last sentence.
                # if appear 0 again, it means it can't find the value.
                if left_range == 0:
                    return None

    # adjust beap, from index to the bottom
    def swap_down(self, i):
        length = self.beap_size - 1
        array = self.beap_list
        height = self.getheight(i)
        leftchild = i + height

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
                # recalculate the height of the current node
                height_i = self.getheight(i)
                # enter next layer of binary heap
                leftchild = i + height_i
            else:
                break

    def extract(self, value):
        if self.beap_size == 0:
            return None
        else:
            length = self.beap_size - 1
            # get the index of value
            index = self.search(value)
            remove_item = self.beap_list[index]
            # exchange the position of index node and last node
            self.beap_list[index], self.beap_list[length] = self.beap_list[length], self.beap_list[index]
            self.beap_list.pop()
            # recalculate the size of beap
            self.beap_size = len(self.beap_list)
            self.swap_down(index)
            print("the value:", remove_item, "has been extracted")

    def build_beap(self, input_value):
        length = len(input_value)
        for i in range(0, length):
            self.insert(input_value[i])

    def checker(self):
        array = self.beap_list
        length = len(array)
        h = self.getheight(length-1)
        for i in range(0, h):
            height = self.getheight(i)
            if array[i] > array[i+height] or array[i] > array[i+height+1]:
                print(array[i],array[i+height],array[i+height+1])
                print("beap is wrong")
                return

        print("heap is correct")
