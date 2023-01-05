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

# Day 2

Use <code>print(""" ascii art """)</code> to print ascii art.

# Day 3
Name Error in Python: Variable name is not exist <br>
**Example)**
```python
# challenge #2525
import sys

hours, mins = map(int, sys.stdin.readline().split(" "))
remain = int(sys.stdin.readline())

mins = mins + remain
if(mins >= 60): # if this false
    result_mins = mins % 60
    hours = hours + (mins // 60)
    if(hours >= 24):
        hours = hours - 24

print(hours, result_mins) # results_mins does not exist
```

***

Python have <code>max()</code> function. Use it well