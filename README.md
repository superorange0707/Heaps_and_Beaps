# Heaps and Beaps

A comprehensive implementation and performance comparison of Binary Heaps and Bi-parental Heaps (Beaps) data structures with **educational visualizations**.

## Project Overview

This project provides implementations of two heap data structures:
- **Binary Heap**: A complete binary tree implemented as an array
- **Beap (Bi-parental Heap)**: A 2D array-like structure with diagonal parent-child relationships

Both data structures are evaluated and compared across various operations. The project includes **step-by-step educational animations** for teaching and presentations.

## Features

### Data Structures
- Complete implementation of Binary Heap
- Complete implementation of Beap (Bi-parental Heap)

### Operations
Both data structures support:
- **Min/Max**: Find minimum/maximum values
- **Search**: Find a specific value
- **Insert**: Add a new value
- **Extract**: Remove a specific value

### 🎬 Educational Visualizations
- Step-by-step animated GIFs showing BEAP operations
- Color-coded nodes for clear visual progression
- Perfect for academic presentations and teaching

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
git clone https://github.com/superorange0707/Heaps_and_Beaps.git
cd Heaps_and_Beaps

# Install dependencies
pip install -r requirements.txt

# For visualizations (additional)
pip install pillow
```

## Quick Start

```bash
# Run demos
python Binary_Heaps/run_binary_heap_demo.py
python Beaps/run_beap_demo.py

# Generate educational animations
python Visualization/generate_beap_gifs.py

# Run performance comparison
python Evaluation/run_comparison.py
```

## Project Structure

- **Binary_Heaps/**: Binary heap implementation
  - `binary_heap.py`: Main Binary Heap implementation
  - `run_binary_heap_demo.py`: Demo script
- **Beaps/**: Beap implementation  
  - `Beaps.py`: Main Beap implementation
  - `run_beap_demo.py`: Demo script
- **Visualization/**: Educational animations and GIF generation
  - `visual.py`: Visualization engine
  - `generate_beap_gifs.py`: GIF generator
- **Benchmark/**: Performance testing
  - `Benchmark.py`: Benchmarking tools
- **Evaluation/**: Performance comparison
  - `run_comparison.py`: Comparison script
- **Paper and Summary/**: Academic documentation
  - `Implementation.py`: Core implementations
  - `Report.pdf`: Detailed analysis
  - `Heaps and Beaps.pdf`: Research paper
- **Report/**: Summary documentation
  - `report_summary.md`: Summary report

## Dependencies

- matplotlib, numpy, np3, scipy
- pillow (for visualizations)

## 🎓 Educational Animations

Generate 5 educational GIFs demonstrating BEAP operations:

**Figure 1: BEAP Structure Formation**
![BEAP Structure Formation](https://github.com/superorange0707/Heaps_and_Beaps/raw/main/Visualization/structure_demo.gif)

**Figure 2: BEAP Insertion with Bubble-up**
![BEAP Insertion Process](https://github.com/superorange0707/Heaps_and_Beaps/raw/main/Visualization/insert_demo.gif)

**Figure 3: BEAP Search Algorithm**
![BEAP Search Process](https://github.com/superorange0707/Heaps_and_Beaps/raw/main/Visualization/search_demo.gif)

**Figure 4: BEAP Extraction with Heapify**
![BEAP Extract Process](https://github.com/superorange0707/Heaps_and_Beaps/raw/main/Visualization/extract_demo.gif)

**Figure 5: BEAP Min/Max Operations**
![BEAP Min/Max Operations](https://github.com/superorange0707/Heaps_and_Beaps/raw/main/Visualization/minmax_demo.gif)

### Generate Your Own Animations

```bash
cd Visualization
python3 generate_beap_gifs.py
```

