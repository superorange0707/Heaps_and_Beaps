import math
import random
import time
import sys
import os

# Add parent directory to path to import from Beaps and Binary_Heaps packages
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Beaps.Beaps import beap
from Binary_Heaps.binary_heap import bin_heap

def compare_operations(size=1000, value_to_search=500, value_to_insert=2000, value_to_extract=250):
    """
    Compare the performance of Beap and Binary Heap operations
    
    Args:
        size: Number of elements to initialize the data structures with
        value_to_search: Value to search for in the comparison
        value_to_insert: Value to insert in the comparison
        value_to_extract: Value to extract in the comparison
    """
    # Generate random data
    data = random.sample(range(0, size*2), size)
    
    # Ensure the value_to_search, value_to_insert, and value_to_extract are in the data
    if value_to_search not in data:
        data[0] = value_to_search
    if value_to_extract not in data:
        data[1] = value_to_extract
    
    # Create instances
    bp = beap()
    bh = bin_heap()
    
    print(f"=== Performance Comparison with {size} elements ===\n")
    
    # Build structures
    print("Building data structures...")
    
    start_time = time.time()
    bp.build_beap(data.copy())
    beap_build_time = (time.time() - start_time) * 1000
    
    start_time = time.time()
    bh.build_binheap(data.copy())
    binheap_build_time = (time.time() - start_time) * 1000
    
    print(f"Beap build time: {beap_build_time:.2f} ms")
    print(f"Binary Heap build time: {binheap_build_time:.2f} ms")
    print(f"Ratio (Beap/BinHeap): {beap_build_time/binheap_build_time:.2f}x\n")
    
    # Min operation
    print("Minimum value retrieval...")
    
    start_time = time.time()
    bp.min_beap()
    beap_min_time = (time.time() - start_time) * 1000
    
    start_time = time.time()
    bh.heap_min()
    binheap_min_time = (time.time() - start_time) * 1000
    
    print(f"Beap min time: {beap_min_time:.2f} ms")
    print(f"Binary Heap min time: {binheap_min_time:.2f} ms")
    print(f"Ratio (Beap/BinHeap): {beap_min_time/binheap_min_time:.2f}x\n")
    
    # Max operation
    print("Maximum value retrieval...")
    
    start_time = time.time()
    bp.max_beap()
    beap_max_time = (time.time() - start_time) * 1000
    
    start_time = time.time()
    bh.heap_max()
    binheap_max_time = (time.time() - start_time) * 1000
    
    print(f"Beap max time: {beap_max_time:.2f} ms")
    print(f"Binary Heap max time: {binheap_max_time:.2f} ms")
    print(f"Ratio (Beap/BinHeap): {beap_max_time/binheap_max_time:.2f}x\n")
    
    # Search operation
    print(f"Search for value {value_to_search}...")
    
    start_time = time.time()
    bp.search(value_to_search)
    beap_search_time = (time.time() - start_time) * 1000
    
    start_time = time.time()
    bh.search(value_to_search)
    binheap_search_time = (time.time() - start_time) * 1000
    
    print(f"Beap search time: {beap_search_time:.2f} ms")
    print(f"Binary Heap search time: {binheap_search_time:.2f} ms")
    print(f"Ratio (BinHeap/Beap): {binheap_search_time/beap_search_time:.2f}x\n")
    
    # Insert operation
    print(f"Insert value {value_to_insert}...")
    
    # Make copies to avoid altering the original structures
    bp_copy = beap()
    bp_copy.build_beap(data.copy())
    bh_copy = bin_heap()
    bh_copy.build_binheap(data.copy())
    
    start_time = time.time()
    bp_copy.insert(value_to_insert)
    beap_insert_time = (time.time() - start_time) * 1000
    
    start_time = time.time()
    bh_copy.insert(value_to_insert)
    binheap_insert_time = (time.time() - start_time) * 1000
    
    print(f"Beap insert time: {beap_insert_time:.2f} ms")
    print(f"Binary Heap insert time: {binheap_insert_time:.2f} ms")
    print(f"Ratio (Beap/BinHeap): {beap_insert_time/binheap_insert_time:.2f}x\n")
    
    # Extract operation
    print(f"Extract value {value_to_extract}...")
    
    # Redirect print output temporarily to suppress extract function's print statements
    original_stdout = sys.stdout
    sys.stdout = open(os.devnull, 'w')
    
    start_time = time.time()
    bp.extract(value_to_extract)
    beap_extract_time = (time.time() - start_time) * 1000
    
    start_time = time.time()
    bh.extract(value_to_extract)
    binheap_extract_time = (time.time() - start_time) * 1000
    
    # Restore stdout
    sys.stdout = original_stdout
    
    print(f"Beap extract time: {beap_extract_time:.2f} ms")
    print(f"Binary Heap extract time: {binheap_extract_time:.2f} ms")
    print(f"Ratio (Beap/BinHeap): {beap_extract_time/binheap_extract_time:.2f}x\n")
    
    print("=== Summary ===")
    print("Operation    | Beap (ms)    | Binary Heap (ms) | Advantage")
    print("-------------|--------------|-----------------|----------")
    print(f"Build        | {beap_build_time:.2f}         | {binheap_build_time:.2f}            | {'Beap' if beap_build_time < binheap_build_time else 'Binary Heap'}")
    print(f"Min          | {beap_min_time:.2f}         | {binheap_min_time:.2f}            | {'Beap' if beap_min_time < binheap_min_time else 'Binary Heap'}")
    print(f"Max          | {beap_max_time:.2f}         | {binheap_max_time:.2f}            | {'Beap' if beap_max_time < binheap_max_time else 'Binary Heap'}")
    print(f"Search       | {beap_search_time:.2f}         | {binheap_search_time:.2f}            | {'Beap' if beap_search_time < binheap_search_time else 'Binary Heap'}")
    print(f"Insert       | {beap_insert_time:.2f}         | {binheap_insert_time:.2f}            | {'Beap' if beap_insert_time < binheap_insert_time else 'Binary Heap'}")
    print(f"Extract      | {beap_extract_time:.2f}         | {binheap_extract_time:.2f}            | {'Beap' if beap_extract_time < binheap_extract_time else 'Binary Heap'}")
    
    # Return the results as a dictionary for potential further analysis
    return {
        "build": {"beap": beap_build_time, "binary_heap": binheap_build_time},
        "min": {"beap": beap_min_time, "binary_heap": binheap_min_time},
        "max": {"beap": beap_max_time, "binary_heap": binheap_max_time},
        "search": {"beap": beap_search_time, "binary_heap": binheap_search_time},
        "insert": {"beap": beap_insert_time, "binary_heap": binheap_insert_time},
        "extract": {"beap": beap_extract_time, "binary_heap": binheap_extract_time}
    }

if __name__ == "__main__":
    print("Heaps and Beaps Performance Comparison Tool")
    print("===========================================")
    
    # Parse command line arguments if needed
    size = 1000
    if len(sys.argv) > 1:
        try:
            size = int(sys.argv[1])
        except ValueError:
            print(f"Invalid size argument: {sys.argv[1]}. Using default size of 1000.")
    
    compare_operations(size=size) 