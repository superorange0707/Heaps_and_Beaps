import math
import random
from binary_heap import bin_heap

def demo_binary_heap():
    """
    Demonstration of Binary Heap data structure operations
    """
    print("=== Binary Heap Demonstration ===")
    
    # Create a binary heap
    print("\nCreating a new Binary Heap...")
    bh = bin_heap()
    
    # Insert elements
    print("\nInserting elements...")
    data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(f"Data to insert: {data}")
    bh.build_binheap(data)
    
    print(f"Heap after insertion: {bh.heap_list}")
    
    # Check if the heap property is maintained
    print("\nChecking Heap property:")
    bh.checker()
    
    # Find min and max
    print(f"\nMinimum value: {bh.heap_min()}")
    print(f"Maximum value: {bh.heap_max()}")
    
    # Search operations
    print("\nSearch operations:")
    value_to_search = 5
    result = bh.search(value_to_search)
    print(f"Search for value {value_to_search}: Found at index {result}")
    
    # Insert a new element
    print("\nInsert operation:")
    new_value = 11
    bh.insert(new_value)
    print(f"After inserting {new_value}: {bh.heap_list}")
    bh.checker()
    
    # Extract an element
    print("\nExtract operation:")
    value_to_extract = 5
    print(f"Extracting value {value_to_extract}...")
    bh.extract(value_to_extract)
    print(f"Heap after extraction: {bh.heap_list}")
    bh.checker()

if __name__ == "__main__":
    demo_binary_heap() 