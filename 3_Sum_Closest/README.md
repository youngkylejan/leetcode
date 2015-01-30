# 3 Sum Closest

**Two Pointers**

sort the list, for each element in the list, scan its next element to the last element  
use a start index pointer and a tail index pointer  

> **Maintain a minDis variable which represents the minimum distance to target**  
> current sum = num[i] + num[start] + num[tail]  
> abs(current sum - target) < minDis, current sum will be the newest result  
> current sum < target, element in the start index is small, start = start + 1  
> current sum >= target, element in the tail index is large, tail = tail - 1  
