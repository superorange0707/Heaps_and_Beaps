# Heaps and Beaps

A comprehensive implementation and performance comparison of Binary Heaps and Bi-parental Heaps (Beaps) data structures.

## Project Overview

This project provides implementations of two heap data structures:
- **Binary Heap**: A complete binary tree implemented as an array
- **Beap (Bi-parental Heap)**: A 2D array-like structure with diagonal parent-child relationships

Both data structures are evaluated and compared across various operations to assess their performance characteristics.

## Features

### Data Structures
- Complete implementation of Binary Heap
- Complete implementation of Beap (Bi-parental Heap)

### Operations
Both data structures support the following operations:
- **Min**: Find the minimum value
- **Max**: Find the maximum value
- **Search**: Find a specific value
- **Insert**: Add a new value
- **Extract**: Remove a specific value

### Performance Analysis
- Benchmarking for all operations
- Comparison between Binary Heap and Beap
- Visualization of performance characteristics

## Performance Summary

| Operation | Binary Heap | Beap |
|-----------|-------------|------|
| Min       | O(1)        | O(1) |
| Max       | O(n)        | O(n) |
| Search    | O(n)        | O(sqrt(n)) |
| Insert    | O(log n)    | O(log n) |
| Extract   | O(log n)    | O(log n) |

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/Heaps_and_Beaps.git
cd Heaps_and_Beaps

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Binary Heap Example
```python
from Binary_Heaps.binary_heap import bin_heap

# Create a binary heap
bh = bin_heap()

# Build a heap from a list
bh.build_binheap([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

# Operations
min_value = bh.heap_min()      # Get minimum value
max_value = bh.heap_max()      # Get maximum value
index = bh.search(5)           # Search for a value
bh.insert(11)                  # Insert a value
bh.extract(0)                  # Extract a value
```

### Beap Example
```python
from Beaps.Beaps import beap

# Create a beap
bp = beap()

# Build a beap from a list
bp.build_beap([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

# Operations
min_value = bp.min_beap()      # Get minimum value
max_value = bp.max_beap()      # Get maximum value
index = bp.search(5)           # Search for a value
bp.insert(11)                  # Insert a value
bp.extract(0)                  # Extract a value
```

### Quick Demo

To quickly see how each data structure works, you can run the provided demo files:

```bash
# Run the Binary Heap demo
python Binary_Heaps/run_binary_heap_demo.py

# Run the Beap demo
python Beaps/run_beap_demo.py

# Run a performance comparison
python Evaluation/run_comparison.py [size]  # Optional size parameter, defaults to 1000
```

### Running Benchmarks
```python
from Benchmark.Benchmark import Test

# Create a test instance
test = Test()

# Run specific benchmarks
test.extensive_searchcompare()   # Compare search performance
test.extensive_maxcompare()      # Compare max operation performance
test.extensive_insertcompare()   # Compare insert performance
test.extensive_extractcompare()  # Compare extract performance
```

## Project Structure

- **Binary_Heaps/**: Binary heap implementation
  - `binary_heap.py`: Main Binary Heap implementation
  - `run_binary_heap_demo.py`: Demonstration script
- **Beaps/**: Beap implementation
  - `Beaps.py`: Main Beap implementation
  - `run_beap_demo.py`: Demonstration script
- **Benchmark/**: Performance testing and comparison
- **Evaluation/**: Evaluation results for both data structures
  - `run_comparison.py`: Script to compare performance of both implementations
- **Report/**: Documentation and analysis report

## Dependencies

- matplotlib
- numpy
- np3
- scipy

