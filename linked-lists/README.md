# Linked Lists

## Single

### Pros

- Like a list, but can be dynamic
- Saves memory by only allocation memory for N items. A standard array requires you to define ahead of time how many elements you need.
- Can live anywhere in memory. Normal arrays require blocks of contiguous memory while a linked list does not.

### Cons

- Linear lookup time `O(n)`
  - When looking for an element, you have to start at the beginning.
  - A normal array is `O(1)` lookup time for an element.

## Double

### Pros

- Can be traversed in both forward and backwards direction
- Delete option is more efficient

### Cons

- Every node requires extra space for a previous pointer
- All operations require an extra pointer to be maintained
