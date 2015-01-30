# 4 Sum

**Two Pointers, HashMap**

there are two solutions of this question with similar concept

* **First Solution (Two Pointers)**  

sort the list, for each element in the list, choose a second element from length - 3 to 0  
use a start index pointer and a tail index pointer in the distance between first element and second element  

> + **Maintain a minDis variable which represents the minimum distance to target**  
> + current sum = num[i] + num[start] + num[tail] + num[j]  
> + current sum == 0, append the solution to the result  
> + current sum < target, element in the start index is small, start = start + 1  
> + current sum >= target, element in the tail index is large, tail = tail - 1  



* **Second Solution (Two Pointers, HashMap)**

> + sort the list  
> + for the whole conbinations of two numberput the pair of these indexes into hash, with the sum key  
> + maintain a two level loop for a two sum with index i and index j  
> + then find the corresponding target - (num[i] + num[j]) value in hashMap  
> + if exist this key, then get the value which are remained indexes, append to the solution result




