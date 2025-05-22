
# Data Structures and Operations Report

## Binary Heap

### Overview
- A **binary heap** is a complete binary tree implemented as an array.
- It supports **Min-Heap** and **Max-Heap** operations.

### Key Operations

#### Min
- **Description**: Returns the root (minimum value in a Min-Heap).
- **Time Complexity**: `O(1)`

#### Max
- **Description**: Search through all leaf nodes (approx. `(n+1)/2`) to find the max.
- **Time Complexity**: `O(n)`

#### Search
- **Description**: Linear search over the array.
- **Time Complexity**: `O(n)`

#### Insert
- **Process**:
  1. Insert at the end of the array.
  2. Percolate up until the heap property is restored.
- **Time Complexity**: `O(log n)`

#### Extract
- **Process**:
  1. Find the node.
  2. Swap with last node and pop.
  3. Restore heap using `swapDown`.
- **Time Complexity**: `O(log n)`

---

## Beap (Bi-parental Heap)

### Overview
- A **Beap** is a 2D array-like structure with parent and child relationships spread diagonally.
- It supports efficient insertions and searches by using a level-based layout.

### Key Operations

#### Min
- **Description**: The root is the minimum.
- **Time Complexity**: `O(1)`

#### Max
- **Description**: Located at one of the leaf nodes (typically the last).
- **Time Complexity**: `O(n)`

#### Search
- **Process**:
  - Start from the first node of the last level.
  - Traverse diagonally based on comparisons.
  - Handle edge cases when right children are missing or out of bounds.
- **Time Complexity**: Worst-case is `O(sqrt(n))`

#### Insert
- **Process**:
  1. Insert at the end.
  2. Compare with left and right parents (depending on position).
  3. Percolate up as needed.
- **Time Complexity**: `O(log n)` (height-dependent)

#### Extract
- **Process**:
  1. Search for the value.
  2. Swap with the last node and pop.
  3. Restore beap using `swapDown`.
- **Time Complexity**: `O(log n)`

---

## Functional Testing

### Fixed Value Test
- Insert and delete operations tested on a fixed dataset:  
  `[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]`
- Results verified using a `checker` function.

---

## Performance and Complexity Testing

### Methodology
- Node count: 1,000 to 20,000 (step: 100)
- Random values used for insertion.
- Operations tested:
  - **Max**: Last node used for worst-case.
  - **Search**: Last node or last layer.
  - **Insert**: Constant insert value.
  - **Delete**: Root node removed.

### Results
- Plots generated using scattered points and fitted curves.
- Observed trends confirm expected theoretical complexities.

---

