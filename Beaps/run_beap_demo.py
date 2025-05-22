import math
import random
from Beaps import beap

def demo_beap():
    """
    Demonstration of Beap data structure operations
    """
    print("=== Beap Demonstration ===")
    
    # Create a beap
    print("\nCreating a new Beap...")
    bp = beap()
    
    # Insert elements
    print("\nInserting elements...")
    data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(f"Data to insert: {data}")
    bp.build_beap(data)
    
    print(f"Beap after insertion: {bp.beap_list}")
    
    # Check if the beap property is maintained
    print("\nChecking Beap property:")
    bp.checker()
    
    # Find min and max
    print(f"\nMinimum value: {bp.min_beap()}")
    print(f"Maximum value: {bp.max_beap()}")
    
    # Search operations
    print("\nSearch operations:")
    value_to_search = 5
    result = bp.search(value_to_search)
    print(f"Search for value {value_to_search}: Found at index {result}")
    
    # Insert a new element
    print("\nInsert operation:")
    new_value = 11
    bp.insert(new_value)
    print(f"After inserting {new_value}: {bp.beap_list}")
    bp.checker()
    
    # Extract an element
    print("\nExtract operation:")
    value_to_extract = 5
    print(f"Extracting value {value_to_extract}...")
    bp.extract(value_to_extract)
    print(f"Beap after extraction: {bp.beap_list}")
    bp.checker()

if __name__ == "__main__":
    demo_beap() 