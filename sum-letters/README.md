# sum-letters

## Problem statement:
Each letter stands for a different digit between `0` and `9`.

```EARTH + VENUS + URANUS = SATURN```

What is the value of `EARTH`?

## Solution:
- There are multiple solutions, here are the 2 of them I found.
```
 ~ $ python3 code.py 
Calculating...
✔️ Solution found!
Table: {'T': 1, 'A': 2, 'R': 5, 'V': 9, 'E': 7, 'H': 4, 'U': 6, 'N': 0, 'S': 8}
Result: sum(72514, 97068, 652068) = 821650
Answer: EARTH = 72514
Permutations checked: 423182
Elapsed time: 1.77 s

 ~ $ python3 code.py 
Calculating...
✔️ Solution found!
Table: {'U': 1, 'R': 5, 'A': 6, 'V': 0, 'S': 2, 'T': 3, 'E': 9, 'H': 4, 'N': 8}
Result: sum(96534, 9812, 156812) = 263158
Answer: EARTH = 96534
Permutations checked: 544340
Elapsed time: 2.25 s

```
