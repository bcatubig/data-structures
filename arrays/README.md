# arrays

## Pros

- Memory is contiguous

## Cons

- Running out of space in the array requires you to define a new array with a new size and then copy over the elements from the old array to the new array. This can be very slow.
- You may not need all elements that were requested
- Memory cannot be used by anyone else



## Lookups

|           | Arrays | Lists  |
| --------- | ------ | ------ |
| Reading   | `O(1)` | `O(n)` |
| Insertion | `O(n)` | `O(1)` |
| Deletion  | `O(N)` | `O(1)` |

