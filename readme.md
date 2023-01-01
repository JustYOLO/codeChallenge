# Code Challenge!

Everyday, 1hour

# Day 1

**Q.** 1000.py like question: find faster method than using <code> a, b = input("").split(" ") </code>

**A.** 
```python
import sys
using_list = list(map(int, sys.stdin.readline().split(" ")))
```

This way will save time (faster than input()) and save the input as integer