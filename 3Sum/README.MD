# 3 Sum

**Two Pointers**

sort the list, for each element in the list, scan its next element to the last element  
use a start index pointer and a tail index pointer  


> num[i] + num[start] + num[tail] == 0, append into the result  
> num[i] + num[start] + num[tail] < 0, element in the start index is small, start = start + 1  
> num[i] + num[start] + num[tail] > 0, element in the tail index is large, tail = tail - 1  
> **Remember to jump over the duplicate element**  