1. Assigning the least integer value to an variable in python
```python
we can simply use 
-sys.maxsize - 1 : for min value, similar to java's Integer.MIN_VALUE
float('-inf') : for negative infinity, float based
```
```python
import sys

print(float('-inf') < -sys.maxsize - 1)  # True: negative infinity < any finite integer
print(float('-inf') + 1)                 # Still -inf, mathematical property

```
