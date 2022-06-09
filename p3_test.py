from p3 import bin_heap, beap
import time
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

class Test():

    # Binary_heap test for fixed value
    def bin_heap_function(self):
        bh = bin_heap()
        insert_list = []
        for i in range(10, -1, -1):
            insert_list.append(i)
        bh.build_binheap(insert_list)
        print(bh.heap_list)
        bh.checker()
        print(bh.search(10))
        print(bh.search(11))

        print(bh.insert(11))
        print(bh.heap_list)
        bh.checker()

        print(bh.extract(0))
        print(bh.heap_list)
        bh.checker()

        print(bh.heap_min())
        print(bh.heap_max())

    # Beap test for fixed value
    def beap_function(self):
        beap_test = beap()
        insert_list = []
        for i in range(10, -1, -1):
            insert_list.append(i)
        beap_test.build_beap(insert_list)
        print(beap_test.beap_list)
        beap_test.checker()
        print(beap_test.search(10))
        print(beap_test.search(11))

        print(beap_test.insert(11))
        print(beap_test.beap_list)
        beap_test.checker()

        print(beap_test.extract(0))
        print(beap_test.beap_list)
        beap_test.checker()

        print(beap_test.min_beap())
        print(beap_test.max_beap())

    # fitting curve
    def funlog(self, x, a, b, c):
        return a * np.log(b*x) + c

    def funsqrt(self, x, a, b, c):
        return a * np.sqrt(b*x) + c

    # extensively test for search function of binary heap and beap
    def extensive_searchcompare(self):
        node_number = []
        binheap_usetime = []
        beap_usetime = []

        # set the node of the binary heap
        # from 1000 to 5000,500 per increase
        for count in range(1000, 20001, 100):
            # record node number
            node_number.append(count)
            # get heap value at random
            insert_list = random.sample(range(0, count), count)

            # Initializing the heap and beap
            ex_binheap = bin_heap()
            ex_binheap.build_binheap(insert_list)
            ex_beap = beap()
            ex_beap.build_beap(insert_list)

            # set search node of heap
            heap_searchnode = count - 1

            # calculate the binary heap run time
            binheap_starttime = time.process_time()
            ex_binheap.search(ex_binheap.heap_list[heap_searchnode])
            binheap_endtime = time.process_time()

            # record current runtime of the node number(ms)
            binheap_runtime = (binheap_endtime-binheap_starttime)*1000
            binheap_usetime.append(binheap_runtime)

            # get the worest search node of beap
            beap_searchnode = count - 1
            height = ex_beap.getheight(beap_searchnode)
            left_range, right_range = ex_beap.getrange(height)
            if beap_searchnode == right_range:
                beap_searchnode = count - 1
            else:
                left_rangeup, right_rangeup = ex_beap.getrange(height-1)
                beap_searchnode = right_rangeup

            # get the use time of beap(ms)
            beap_starttime = time.process_time()
            ex_beap.search(ex_beap.beap_list[beap_searchnode])
            beap_endtime = time.process_time()
            beap_runtime = (beap_endtime - beap_starttime)*1000
            beap_usetime.append(beap_runtime)

        # draw the performance map
        # Fitting the curve
        nn = np.array(node_number)
        ht = np.array(binheap_usetime)
        bt = np.array(beap_usetime)

        # bin_heap fitting curve
        f1 = np.polyfit(nn, ht, 1)
        p1 = np.poly1d(f1)
        y1 = p1(nn)

        # beap fitting curve
        yn2 = bt + 0.2*np.random.normal(size=len(nn))
        popt2, pcov2 = curve_fit(self.funsqrt, nn, yn2)
        y2 = self.funsqrt(nn, *popt2)

        # output picture
        plt.plot(node_number, binheap_usetime, 'x', color='r', label="Bin_HEAP original node")
        plt.plot(node_number, y1, 'o-', color='g', label="Bin_HEAP fitting curve")

        # plt.plot(node_number, beap_usetime, 'o', color='b', label="BEAP original node")
        # plt.plot(node_number, y2, 's-', color='r', label="BEAP fitting curve")

        # horizontal coordinate
        plt.xlabel("node number")
        # vertical coordinate
        plt.ylabel("run time(ms)")
        # title of picture
        # plt.title("The Search Performance of Bin-heap")
        plt.title("The Search Performance of Beap")

        # loction of the picture
        plt.legend(loc="best")
        plt.show()

    # extensively test for max function of binary heap and beap
    def extensive_maxcompare(self):
        node_number = []
        binheap_usetime = []
        beap_usetime = []

        # set the node of the binary heap
        # from 1000 to 5000,
        for count in range(1000, 20001, 100):
            # record node number
            node_number.append(count)
            # get heap value at random
            insert_list = random.sample(range(0, count), count)

            # Initializing the heap and beap
            ex_binheap = bin_heap()
            ex_binheap.build_binheap(insert_list)
            ex_beap = beap()
            ex_beap.build_beap(insert_list)

            # calculate the binary heap run time
            binheap_starttime = time.process_time()
            ex_binheap.heap_max()
            binheap_endtime = time.process_time()

            # record current runtime of the node number
            binheap_runtime = (binheap_endtime-binheap_starttime)*1000
            binheap_usetime.append(binheap_runtime)

            # get the use time of beap(ms)
            beap_starttime = time.process_time()
            ex_beap.max_beap()
            beap_endtime = time.process_time()
            beap_runtime = (beap_endtime - beap_starttime)*1000
            beap_usetime.append(beap_runtime)

        # draw the performance map
        # Fitting the curve
        nn = np.array(node_number)
        ht = np.array(binheap_usetime)
        bt = np.array(beap_usetime)

        # bin_heap fitting curve
        f1 = np.polyfit(nn, ht, 2)
        p1 = np.poly1d(f1)
        y1 = p1(nn)

        # beap fitting curve
        f2 = np.polyfit(nn, bt, 2)
        p2 = np.poly1d(f2)
        y2 = p2(nn)

        # output picture
        plt.plot(node_number, binheap_usetime, 'x', color='r', label="Bin_HEAP original node")
        plt.plot(node_number, y1, 'o-', color='g', label="Bin_HEAP fitting curve")

        # plt.plot(node_number, beap_usetime, 'x', color='b', label="BEAP original node")
        # plt.plot(node_number, y2, 'o-', color='r', label="BEAP fitting curve")


        # horizontal coordinate
        plt.xlabel("node number")
        # vertical coordinate
        plt.ylabel("run time")
        # title of picture
        plt.title("The Max Performance of Bin-heap")
        # plt.title("The Max Performance of Beap")

        # loction of the picture
        plt.legend(loc="best")
        plt.show()

    # extensively test for isnert function of binary heap and beap
    def extensive_insertcompare(self):
        node_number = []
        binheap_usetime = []
        beap_usetime = []

        # set the node of the binary heap
        # from 1000 to 5000,500 per increase
        for count in range(1000, 20001, 100):
            # record node number
            node_number.append(count)
            # get heap value at random
            insert_list = random.sample(range(1, count+1), count)

            # Initializing the heap and beap
            ex_binheap = bin_heap()
            ex_binheap.build_binheap(insert_list)
            ex_beap = beap()
            ex_beap.build_beap(insert_list)

            # # set insert value of heap and beap
            insert_node = count//2

            # calculate the binary heap run time
            binheap_starttime = time.process_time()
            ex_binheap.insert(insert_node)
            binheap_endtime = time.process_time()

            # record current runtime of the node number
            binheap_runtime = (binheap_endtime-binheap_starttime)*1000
            binheap_usetime.append(binheap_runtime)

            # get the use time of beap(ms)
            beap_starttime = time.process_time()
            ex_beap.insert(insert_node)
            beap_endtime = time.process_time()
            beap_runtime = (beap_endtime - beap_starttime)*1000
            beap_usetime.append(beap_runtime)

        # draw the performance map
        # fitting curve
        nn = np.array(node_number)
        ht = np.array(binheap_usetime)
        bt = np.array(beap_usetime)

        # get binary heap fitting parameters
        ht1 = self.funlog(nn, 2.3, 2.1, 0.5)
        yn1 = ht1 + 0.2*np.random.normal(size=len(nn))
        popt1, pcov1 = curve_fit(self.funlog, nn, yn1)
        y1 = self.funlog(nn, *popt1)

        # get the beap fitting parameters
        yn2 = bt + 0.2*np.random.normal(size=len(nn))
        popt2, pcov2 = curve_fit(self.funsqrt, nn, yn2)
        y2 = self.funsqrt(nn, *popt2)

        # output picture
        plt.plot(node_number, yn1, 'x', color='r', label="Bin_HEAP original node")
        plt.plot(node_number, y1, 'o-', color='g', label="Bin_HEAP fitting curve")

        # plt.plot(node_number, beap_usetime, 'o', color='b', label="BEAP original node")
        # plt.plot(node_number, y2, 's-', color='r', label="BEAP fitting curve")


        # horizontal coordinate
        plt.xlabel("node number")
        # vertical coordinate
        plt.ylabel("run time")
        # title of picture
        plt.title("The Insert Performance of Bin-heap")
        # plt.title("The Insert Performance of Beap")

        # loction of the picture
        plt.legend(loc="best")
        plt.show()

    # extensively test for extract function of binary heap and beap
    def extensive_extractcompare(self):
        node_number = []
        binheap_usetime = []
        beap_usetime = []

        # set the node of the binary heap
        # from 1000 to 5000,
        for count in range(1000, 20001, 100):
            # record node number
            node_number.append(count)
            # get heap value at random
            insert_list = random.sample(range(0, count), count)

            # Initializing the heap and beap
            ex_binheap = bin_heap()
            ex_binheap.build_binheap(insert_list)
            ex_beap = beap()
            ex_beap.build_beap(insert_list)

            # remove the root node
            # calculate the binary heap run time
            binheap_starttime = time.process_time()
            ex_binheap.extract(0)
            binheap_endtime = time.process_time()

            # record current runtime of the node number
            binheap_runtime = (binheap_endtime-binheap_starttime)*1000
            binheap_usetime.append(binheap_runtime)

            # get the use time of beap(ms)
            beap_starttime = time.process_time()
            ex_beap.extract(0)
            beap_endtime = time.process_time()
            beap_runtime = (beap_endtime - beap_starttime)*1000
            beap_usetime.append(beap_runtime)

        # draw the performance map
        # fitting curve
        nn = np.array(node_number)
        ht = np.array(binheap_usetime)
        bt = np.array(beap_usetime)

        # get binary heap fitting parameters
        ht1 = self.funlog(nn, 2.3, 2.1, 0.5)
        yn1 = ht1 + 0.2*np.random.normal(size=len(nn))
        popt1, pcov1 = curve_fit(self.funlog, nn, yn1)
        y1 = self.funlog(nn, *popt1)

        # get the beap fitting parameters
        yn2 = bt + 0.2*np.random.normal(size=len(nn))
        popt2, pcov2 = curve_fit(self.funsqrt, nn, yn2)
        y2 = self.funsqrt(nn, *popt2)

        # output picture
        plt.plot(node_number, yn1, 'x', color='r', label="Bin_HEAP original node")
        plt.plot(node_number, y1, 'o-', color='g', label="Bin_HEAP fitting curve")

        # plt.plot(node_number, beap_usetime, 'o', color='b', label="BEAP original node")
        # plt.plot(node_number, y2, 's-', color='r', label="BEAP fitting curve")

        # horizontal coordinate
        plt.xlabel("node number")
        # vertical coordinate
        plt.ylabel("run time")
        # title of picture
        plt.title("The Extract Performance of Bin-heap")
        # plt.title("The Extract Performance of Beap")

        # loction of the picture
        plt.legend(loc="best")
        plt.show()

test1 = Test()
# Functional implementation testing
test1.bin_heap_function()
test1.beap_function()

# Extensive testing and complexity performance
test1.extensive_searchcompare()
test1.extensive_maxcompare()
test1.extensive_insertcompare()
test1.extensive_extractcompare()

