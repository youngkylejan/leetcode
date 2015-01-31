# Best Time to Buy and Sell Stock III

**Greedy, Array**

**1.	first solution (Greedy)**

> maintain two array  
> one to record the maxProfit in each position while scanning from start to end  
> one to record the maxProfit in each position while scanning from end to start  
> **the most profit will be the max sum of maxProfits in specific position in two arrays**  

**2.	second solution (Dynamic Programming)**
> global[i][j] => the best profit, with j transactions in ith day  
> local[i][j] => the best profit, with j transactions in ith day and the last transaction is executed in ith day  
> global[i][j] = max(local[i][j], global[i-1][j])  
> local[i][j] = max(global[i-1][j-1] + max(current diff, 0), local[i-1][j] + current diff)  



